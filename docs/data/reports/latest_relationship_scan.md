# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T17:52:24.184569+00:00`
- Price records: `672`
- Market context records: `2374`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `news_risk_high->crypto_alt_24h` score `21.9188` n `43` status `ready` deltaP `50.2099` edge `1.5507` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `17.8702` n `43` status `ready` deltaP `48.0216` edge `1.213` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.1879` n `43` status `ready` deltaP `29.7925` edge `1.0985` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.8778` n `43` status `ready` deltaP `19.7674` edge `0.9161` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.1287` n `43` status `ready` deltaP `27.9877` edge `0.5134` maxDD `-1.4744`
- `market_context_high->crypto_major_24h` score `7.6007` n `136` status `ready` deltaP `19.1176` edge `0.8952` maxDD `-25.1408`
- `market_context_high->unknown_24h` score `5.6377` n `136` status `ready` deltaP `23.8154` edge `0.3522` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `5.6367` n `147` status `ready` deltaP `24.0336` edge `0.4905` maxDD `-10.1468`
- `news_risk_high->index_24h` score `5.307` n `43` status `ready` deltaP `13.4448` edge `0.3945` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.7676` n `147` status `ready` deltaP `19.0943` edge `0.5379` maxDD `-15.4319`
- `market_context_high->unknown_4h` score `4.7468` n `147` status `ready` deltaP `20.15` edge `0.3222` maxDD `-1.8773`
- `news_risk_high->commodity_4h` score `3.7506` n `43` status `ready` deltaP `32.0051` edge `0.3346` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4615` n `43` status `ready` deltaP `36.7087` edge `0.0622` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `1.9723` n `43` status `ready` deltaP `25.2977` edge `0.0141` maxDD `-0.1382`
- `market_context_high->index_4h` score `1.6961` n `147` status `ready` deltaP `18.3933` edge `0.1013` maxDD `-2.2732`
- `market_context_high->index_24h` score `1.6086` n `136` status `ready` deltaP `12.3162` edge `0.1037` maxDD `-1.4737`
- `market_context_high->crypto_major_1h` score `1.5636` n `155` status `ready` deltaP `13.6073` edge `0.159` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `1.2522` n `155` status `ready` deltaP `9.943` edge `0.1568` maxDD `-6.1656`
- `news_risk_high->unknown_4h` score `1.0648` n `43` status `ready` deltaP `13.5529` edge `0.0707` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `0.9491` n `43` status `ready` deltaP `19.2487` edge `-0.0023` maxDD `-1.7548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
