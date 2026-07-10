# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T10:52:28.628580+00:00`
- Price records: `672`
- Market context records: `6276`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11100`

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

- `news_risk_high->crypto_alt_24h` score `15.1489` n `32` status `ready` deltaP `43.058` edge `0.9901` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.9658` n `32` status `ready` deltaP `50.692` edge `0.1592` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2097` n `32` status `ready` deltaP `44.1311` edge `0.0612` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.0168` n `32` status `ready` deltaP `16.4901` edge `0.483` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.5464` n `32` status `ready` deltaP `25.5515` edge `0.0624` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3224` n `32` status `ready` deltaP `27.994` edge `0.0208` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.85` n `205` status `ready` deltaP `2.7421` edge `0.2367` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3049` n `32` status `ready` deltaP `13.3795` edge `0.1248` maxDD `-2.0691`
- `market_context_high->unknown_4h` score `1.2545` n `193` status `ready` deltaP `-1.1445` edge `0.3654` maxDD `-11.925`
- `news_risk_high->crypto_alt_1h` score `0.7857` n `32` status `ready` deltaP `10.5726` edge `0.0764` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.0563` n `193` status `ready` deltaP `5.927` edge `0.0569` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.2176` n `32` status `ready` deltaP `8.4991` edge `0.0026` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3132` n `205` status `ready` deltaP `0.7989` edge `-0.0009` maxDD `-0.5659`
- `market_context_high->metal_24h` score `-0.3989` n `191` status `ready` deltaP `16.4559` edge `0.096` maxDD `-11.8809`
- `market_context_high->metal_4h` score `-0.4075` n `193` status `ready` deltaP `4.8907` edge `0.0287` maxDD `-3.417`
- `market_context_high->commodity_1h` score `-0.5128` n `205` status `ready` deltaP `-0.0168` edge `0.0034` maxDD `-0.682`
- `news_risk_high->metal_1h` score `-0.6772` n `32` status `ready` deltaP `-2.0958` edge `-0.0231` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.6819` n `205` status `ready` deltaP `7.2952` edge `0.0392` maxDD `-9.3536`
- `market_context_high->metal_1h` score `-0.8112` n `205` status `ready` deltaP `2.0505` edge `-0.0014` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.8168` n `205` status `ready` deltaP `5.3155` edge `0.0366` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
