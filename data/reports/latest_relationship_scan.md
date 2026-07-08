# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T21:07:42.374798+00:00`
- Price records: `672`
- Market context records: `6124`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `10.0838` n `30` status `ready` deltaP `38.125` edge `0.6009` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.8904` n `30` status `ready` deltaP `69.9653` edge `0.1911` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3067` n `32` status `ready` deltaP `44.8933` edge `0.0642` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3919` n `32` status `ready` deltaP `28.7425` edge `0.0216` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.2986` n `32` status `ready` deltaP `13.9783` edge `0.12` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7008` n `32` status `ready` deltaP `9.0756` edge `0.0755` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.6027` n `195` status `ready` deltaP `5.122` edge `0.1078` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.0644` n `30` status `ready` deltaP `8.7152` edge `0.0208` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2754` n `195` status `ready` deltaP `1.4348` edge `-0.0003` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.5227` n `30` status `ready` deltaP `14.0973` edge `-0.117` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.7193` n `195` status `ready` deltaP `2.7799` edge `0.008` maxDD `-3.4996`
- `market_context_high->equity_1h` score `-0.7495` n `195` status `ready` deltaP `0.0399` edge `0.0152` maxDD `-4.2573`
- `market_context_high->commodity_1h` score `-0.7499` n `195` status `ready` deltaP `-1.9891` edge `-0.0046` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7871` n `32` status `ready` deltaP `-3.1437` edge `-0.0302` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8452` n `195` status `ready` deltaP `2.2409` edge `-0.0055` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.8751` n `195` status `ready` deltaP `4.0596` edge `0.036` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.8993` n `195` status `ready` deltaP `4.7636` edge `0.0297` maxDD `-9.807`
- `market_context_high->index_4h` score `-1.0123` n `195` status `ready` deltaP `0.0219` edge `0.0165` maxDD `-1.381`
- `news_risk_high->index_1h` score `-1.1365` n `32` status `ready` deltaP `-10.2732` edge `-0.0209` maxDD `-1.1725`
- `market_context_high->metal_24h` score `-1.2022` n `195` status `ready` deltaP `13.953` edge `0.0097` maxDD `-11.8809`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
