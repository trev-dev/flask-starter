const path = require('path')
const MiniCssExtract = require('mini-css-extract-plugin')

const base = {
  entry: './src/ts/index.ts',
  output: {
    path: path.resolve(__dirname, 'flaskr', 'static', 'js'),
    filename: 'site.js'
  },
  module: {
    rules: [
      {
        test: /\.s(c|a)ss$/,
        use: [
          MiniCssExtract.loader,
          { loader: 'css-loader', options: { importLoaders: 2 } },
          'postcss-loader',
          'sass-loader'
        ]
      },
      {
        test: /\.tsx?$/,
        loader: 'ts-loader',
        exclude: /node_modules/
      },

    ]
  },
  plugins: [
    new MiniCssExtract({
      filename: '../css/styles.css'
    })
  ]
}

const dev = {
  ...base,
  mode: 'development',
  devtool: 'inline-source-map',
  watch: true
}

const prod = {
  ...base,
  mode: 'production',
}

function getConfig(env) {
  const { production } = env
  const config = production !== undefined ? prod : dev 
  return config
}

module.exports = getConfig