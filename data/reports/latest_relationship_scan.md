# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T12:07:35.433140+00:00`
- Price records: `672`
- Market context records: `5142`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5596`

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

- `market_context_high->unknown_24h` score `25.821` n `68` status `ready` deltaP `31.5462` edge `1.9757` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `6.6942` n `125` status `ready` deltaP `18.761` edge `0.535` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `6.2199` n `137` status `ready` deltaP `9.6857` edge `0.5179` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `4.8854` n `125` status `ready` deltaP `14.8402` edge `0.4681` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.5558` n `125` status `ready` deltaP `12.7451` edge `0.4406` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.9834` n `125` status `ready` deltaP `9.9622` edge `0.1794` maxDD `-7.4425`
- `market_context_high->commodity_24h` score `0.7636` n `68` status `ready` deltaP `15.6862` edge `0.1166` maxDD `-5.1955`
- `market_context_high->crypto_alt_1h` score `0.7577` n `137` status `ready` deltaP `5.399` edge `0.1233` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.7132` n `137` status `ready` deltaP `7.8128` edge `0.1319` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.6595` n `137` status `ready` deltaP `7.2709` edge `0.0658` maxDD `-2.745`
- `market_context_high->crypto_alt_24h` score `0.6342` n `68` status `ready` deltaP `17.3713` edge `0.5822` maxDD `-46.2794`
- `market_context_high->crypto_major_24h` score `0.036` n `68` status `ready` deltaP `15.7374` edge `0.582` maxDD `-48.0465`
- `market_context_high->index_1h` score `-0.0266` n `137` status `ready` deltaP `5.0625` edge `0.0144` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0671` n `137` status `ready` deltaP `4.856` edge `0.0156` maxDD `-1.8592`
- `market_context_high->index_4h` score `-0.3234` n `125` status `ready` deltaP `7.1829` edge `0.0369` maxDD `-2.9391`
- `market_context_high->metal_24h` score `-0.3299` n `68` status `ready` deltaP `-1.8587` edge `0.1732` maxDD `-10.0641`
- `market_context_high->fx_24h` score `-0.452` n `68` status `ready` deltaP `4.5751` edge `0.0014` maxDD `-0.8549`
- `market_context_high->commodity_1h` score `-0.5662` n `137` status `ready` deltaP `0.6829` edge `-0.0002` maxDD `-2.155`
- `market_context_high->fx_1h` score `-0.5814` n `137` status `ready` deltaP `-1.3571` edge `-0.0014` maxDD `-0.7944`
- `market_context_high->fx_4h` score `-0.8893` n `125` status `ready` deltaP `-1.2768` edge `0.0013` maxDD `-1.8772`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
