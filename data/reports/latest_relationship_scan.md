# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T23:48:16.784839+00:00`
- Price records: `672`
- Market context records: `8353`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5886`

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

- `news_risk_high->unknown_24h` score `6252.0518` n `52` status `ready` deltaP `35.1896` edge `520.8118` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.6407` n `52` status `ready` deltaP `26.5244` edge `0.5196` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.91` n `52` status `ready` deltaP `20.8314` edge `0.1345` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7926` n `52` status `ready` deltaP `23.1707` edge `0.0973` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.1902` n `52` status `ready` deltaP `10.4362` edge `0.2806` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7646` n `52` status `ready` deltaP `13.3579` edge `0.1014` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7022` n `52` status `ready` deltaP `11.7112` edge `0.1035` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6912` n `52` status `ready` deltaP `17.9409` edge `0.2364` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8352` n `52` status `ready` deltaP `7.6337` edge `0.0655` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2349` n `52` status `ready` deltaP `4.445` edge `0.0188` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0712` n `52` status `ready` deltaP `5.1935` edge `0.0026` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.2336` n `52` status `ready` deltaP `2.0498` edge `0.0072` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5608` n `52` status `ready` deltaP `2.9784` edge `0.004` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2484` n `52` status `ready` deltaP `-9.6154` edge `-0.0447` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.2687` n `52` status `ready` deltaP `-23.0369` edge `-0.0533` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.7381` n `52` status `ready` deltaP `-25.8547` edge `-0.1121` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.0605` n `52` status `ready` deltaP `-31.5431` edge `-0.214` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.908` n `52` status `ready` deltaP `-9.3082` edge `-0.3363` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.0575` n `52` status `ready` deltaP `-24.0785` edge `-0.294` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.7273` n `52` status `ready` deltaP `-16.9871` edge `-1.3282` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
