# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T12:07:25.101636+00:00`
- Price records: `672`
- Market context records: `6389`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11074`

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

- `news_risk_high->crypto_alt_24h` score `14.0525` n `32` status `ready` deltaP `37.1528` edge `0.9381` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.4849` n `32` status `ready` deltaP `54.1667` edge `0.1793` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.3665` n `32` status `ready` deltaP `37.8472` edge `0.1321` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `4.2825` n `32` status `ready` deltaP `17.5347` edge `0.5101` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.9852` n `32` status `ready` deltaP `41.2348` edge `0.0618` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4099` n `32` status `ready` deltaP `29.0419` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4718` n `32` status `ready` deltaP `14.128` edge `0.1412` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8294` n `32` status `ready` deltaP `10.4229` edge `0.083` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.4684` n `216` status `ready` deltaP `14.7302` edge `0.0415` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.1718` n `216` status `ready` deltaP `9.0673` edge `0.0215` maxDD `-0.4108`
- `market_context_high->unknown_1h` score `0.1154` n `227` status `ready` deltaP `-6.2808` edge `0.1523` maxDD `-3.7317`
- `news_risk_high->unknown_1h` score `-0.1722` n `32` status `ready` deltaP `7.2792` edge `-0.0284` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.2281` n `146` status `ready` deltaP `19.6205` edge `0.0968` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.4694` n `227` status `ready` deltaP `2.2475` edge `0.0026` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.6616` n `32` status `ready` deltaP `-1.497` edge `-0.0251` maxDD `-1.6464`
- `market_context_high->index_1h` score `-0.6749` n `227` status `ready` deltaP `-2.5898` edge `0.0027` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.6928` n `227` status `ready` deltaP `-2.7309` edge `-0.0023` maxDD `-2.1314`
- `news_risk_high->index_24h` score `-0.7401` n `32` status `ready` deltaP `0.5208` edge `-0.0112` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.7406` n `227` status `ready` deltaP `-1.0242` edge `-0.0015` maxDD `-0.9376`
- `market_context_high->equity_4h` score `-0.759` n `216` status `ready` deltaP `8.3898` edge `0.0507` maxDD `-8.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
