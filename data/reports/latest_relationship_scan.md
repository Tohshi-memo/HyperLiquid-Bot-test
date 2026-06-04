# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T15:22:27.518566+00:00`
- Price records: `672`
- Market context records: `2878`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6912`

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

- `market_context_high->crypto_alt_24h` score `7.8928` n `142` status `ready` deltaP `7.2159` edge `1.0013` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `4.6183` n `142` status `ready` deltaP `9.1989` edge `0.37` maxDD `-1.7175`
- `market_context_high->equity_24h` score `4.4604` n `142` status `ready` deltaP `8.5607` edge `0.515` maxDD `-12.6963`
- `market_context_high->index_24h` score `2.2194` n `142` status `ready` deltaP `10.759` edge `0.2113` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.6944` n `142` status `ready` deltaP `15.5516` edge `0.3469` maxDD `-12.4171`
- `market_context_high->unknown_4h` score `0.7942` n `142` status `ready` deltaP `6.0331` edge `0.1313` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.7531` n `142` status `ready` deltaP `15.435` edge `0.0778` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0072` n `142` status `ready` deltaP `4.6471` edge `0.0175` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.0709` n `142` status `ready` deltaP `4.0314` edge `0.0403` maxDD `-3.1801`
- `market_context_high->equity_4h` score `-0.083` n `142` status `ready` deltaP `4.4014` edge `0.1017` maxDD `-5.7037`
- `market_context_high->crypto_alt_4h` score `-0.5349` n `142` status `ready` deltaP `14.4903` edge `0.2929` maxDD `-28.7261`
- `market_context_high->commodity_1h` score `-0.5898` n `142` status `ready` deltaP `-0.5819` edge `0.0036` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.6652` n `142` status `ready` deltaP `-2.0346` edge `0.0025` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6816` n `142` status `ready` deltaP `-0.3163` edge `-0.0007` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.7115` n `142` status `ready` deltaP `4.6471` edge `0.0538` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.7648` n `142` status `ready` deltaP `-2.0009` edge `0.0329` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.8259` n `142` status `ready` deltaP `4.6745` edge `0.0499` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.0898` n `142` status `ready` deltaP `4.1244` edge `0.0248` maxDD `-10.0279`
- `market_context_high->fx_4h` score `-1.2917` n `142` status `ready` deltaP `-5.1249` edge `0.0044` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3855` n `142` status `ready` deltaP `-1.8852` edge `-0.0157` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
