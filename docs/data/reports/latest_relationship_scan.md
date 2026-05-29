# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T19:22:20.952362+00:00`
- Price records: `672`
- Market context records: `2273`
- Flow alert records: `8438`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9287`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `news_risk_high->crypto_alt_24h` score `21.053` n `43` status `ready` deltaP `51.2516` edge `1.4716` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.6595` n `43` status `ready` deltaP `41.598` edge `1.0716` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.1292` n `43` status `ready` deltaP `31.5286` edge `0.9987` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.9151` n `43` status `ready` deltaP `21.5035` edge `0.8243` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `8.6594` n `155` status `ready` deltaP `27.2423` edge `0.8079` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `8.3547` n `115` status `ready` deltaP `27.7626` edge `0.5523` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `8.3176` n `155` status `ready` deltaP `31.9708` edge `0.661` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `7.9182` n `43` status `ready` deltaP `31.8071` edge `0.4704` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.5951` n `155` status `ready` deltaP `22.2934` edge `0.3786` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `5.3732` n `115` status `ready` deltaP `15.2144` edge `0.9767` maxDD `-25.1408`
- `news_risk_high->index_24h` score `3.7723` n `43` status `ready` deltaP `12.5767` edge `0.2724` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.749` n `43` status `ready` deltaP `32.0051` edge `0.3344` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.6087` n `43` status `ready` deltaP `37.2295` edge `0.071` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.3827` n `115` status `ready` deltaP `14.3765` edge `0.2378` maxDD `-1.4737`
- `news_risk_high->commodity_24h` score `3.327` n `43` status `ready` deltaP `3.2461` edge `0.3373` maxDD `-3.202`
- `market_context_high->index_4h` score `2.5909` n `155` status `ready` deltaP `24.3135` edge `0.1364` maxDD `-2.2732`
- `market_context_high->equity_4h` score `2.4035` n `155` status `ready` deltaP `18.8611` edge `0.215` maxDD `-5.9024`
- `market_context_high->crypto_alt_1h` score `2.3484` n `159` status `ready` deltaP `13.9711` edge `0.2213` maxDD `-6.1656`
- `news_risk_high->fx_4h` score `2.0601` n `43` status `ready` deltaP `26.3648` edge `0.0143` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `2.0163` n `159` status `ready` deltaP `13.9711` edge `0.1943` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
