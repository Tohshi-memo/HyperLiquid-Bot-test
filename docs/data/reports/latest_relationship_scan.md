# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T17:37:20.284157+00:00`
- Price records: `672`
- Market context records: `1651`
- Flow alert records: `6665`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8844`

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

- `market_context_high->metal_24h` score `9.4767` n `169` status `ready` deltaP `28.0687` edge `0.8452` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.1007` n `187` status `ready` deltaP `21.742` edge `0.4632` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.71` n `169` status `ready` deltaP `20.0651` edge `0.3132` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `2.3577` n `187` status `ready` deltaP `17.6943` edge `0.3494` maxDD `-13.3376`
- `market_context_high->equity_4h` score `1.7478` n `187` status `ready` deltaP `11.9104` edge `0.1757` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.5993` n `169` status `ready` deltaP `19.0823` edge `0.4959` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `0.4835` n `169` status `ready` deltaP `24.8817` edge `0.733` maxDD `-62.3533`
- `market_context_high->crypto_alt_1h` score `0.3695` n `197` status `ready` deltaP `5.4987` edge `0.0965` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.3027` n `169` status `ready` deltaP `25.5359` edge `1.0359` maxDD `-88.8062`
- `market_context_high->equity_1h` score `-0.299` n `197` status `ready` deltaP `1.2485` edge `0.0342` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.429` n `187` status `ready` deltaP `0.4501` edge `0.0509` maxDD `-3.7119`
- `market_context_high->index_1h` score `-0.4976` n `197` status `ready` deltaP `-1.0228` edge `0.0062` maxDD `-1.7205`
- `market_context_high->fx_24h` score `-0.5002` n `169` status `ready` deltaP `6.214` edge `0.0218` maxDD `-1.3925`
- `market_context_high->crypto_major_1h` score `-0.5061` n `197` status `ready` deltaP `1.861` edge `0.0501` maxDD `-5.5244`
- `market_context_high->fx_1h` score `-0.5085` n `197` status `ready` deltaP `0.1558` edge `-0.003` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.8409` n `197` status `ready` deltaP `3.1756` edge `0.0046` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.8488` n `197` status `ready` deltaP `1.5943` edge `-0.0063` maxDD `-6.7191`
- `market_context_high->metal_4h` score `-1.418` n `187` status `ready` deltaP `7.818` edge `0.0989` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-2.0399` n `187` status `ready` deltaP `-9.5703` edge `-0.0133` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.2916` n `187` status `ready` deltaP `10.7424` edge `-0.1188` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
