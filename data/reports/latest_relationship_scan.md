# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T02:37:27.307144+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11509`

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

- `news_risk_high->unknown_4h` score `366.1034` n `83` status `ready` deltaP `-21.6629` edge `30.7425` maxDD `-4.1571`
- `news_risk_high->unknown_24h` score `38.8332` n `78` status `ready` deltaP `21.1806` edge `3.0949` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `24.4083` n `78` status `ready` deltaP `47.7698` edge `1.7546` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `20.7445` n `78` status `ready` deltaP `39.7303` edge `1.6109` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.9893` n `78` status `ready` deltaP `49.8531` edge `1.1775` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.3709` n `78` status `ready` deltaP `59.6821` edge `0.3173` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.8288` n `78` status `ready` deltaP `38.4882` edge `0.3579` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.7909` n `52` status `ready` deltaP `38.0208` edge `0.2291` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.7909` n `52` status `ready` deltaP `38.0208` edge `0.2291` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.4917` n `149` status `ready` deltaP `31.3094` edge `0.2181` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.4908` n `52` status `ready` deltaP `32.6255` edge `-0.0057` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4908` n `52` status `ready` deltaP `32.6255` edge `-0.0057` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.356` n `149` status `ready` deltaP `29.8506` edge `0.0189` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.7456` n `52` status `ready` deltaP `24.1557` edge `0.0194` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.7456` n `52` status `ready` deltaP `24.1557` edge `0.0194` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.6453` n `149` status `ready` deltaP `20.658` edge `0.0412` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.8087` n `83` status `ready` deltaP `19.053` edge `0.0395` maxDD `-0.6935`
- `market_context_high->commodity_1h` score `0.7658` n `149` status `ready` deltaP `12.9175` edge `0.0154` maxDD `-0.3491`
- `risk_on_high->crypto_alt_4h` score `0.3209` n `52` status `ready` deltaP `9.5451` edge `0.139` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.3209` n `52` status `ready` deltaP `9.5451` edge `0.139` maxDD `-6.2526`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
