# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T09:52:19.005357+00:00`
- Price records: `672`
- Market context records: `1934`
- Flow alert records: `7467`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7540`

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

- `market_context_high->crypto_alt_4h` score `7.0557` n `213` status `ready` deltaP `22.2819` edge `0.5539` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.4589` n `213` status `ready` deltaP `26.2267` edge `0.488` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.1679` n `213` status `ready` deltaP `15.8372` edge `0.3608` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.0209` n `213` status `ready` deltaP `13.4039` edge `0.1885` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `0.77` n `196` status `ready` deltaP `14.6861` edge `0.4983` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.5222` n `225` status `ready` deltaP `7.1743` edge `0.0943` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.4284` n `225` status `ready` deltaP `7.0013` edge `0.1004` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.3162` n `196` status `ready` deltaP `12.2626` edge `0.1872` maxDD `-12.7414`
- `market_context_high->index_24h` score `0.1682` n `196` status `ready` deltaP `4.2233` edge `0.1087` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.084` n `213` status `ready` deltaP `7.7092` edge `0.0645` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.2126` n `225` status `ready` deltaP `4.5689` edge `0.0312` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2513` n `196` status `ready` deltaP `10.1793` edge `0.0161` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.6158` n `225` status `ready` deltaP `-2.4491` edge `0.0006` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6847` n `225` status `ready` deltaP `0.0027` edge `0.0061` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7636` n `225` status `ready` deltaP `3.4784` edge `0.0125` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-0.9281` n `213` status `ready` deltaP `-4.3749` edge `-0.001` maxDD `-1.1056`
- `market_context_high->equity_24h` score `-1.0518` n `196` status `ready` deltaP `7.9791` edge `0.349` maxDD `-33.1875`
- `market_context_high->metal_4h` score `-1.3036` n `213` status `ready` deltaP `8.0026` edge `0.1072` maxDD `-12.5349`
- `market_context_high->unknown_1h` score `-1.4551` n `225` status `ready` deltaP `0.6341` edge `-0.0303` maxDD `-3.6151`
- `market_context_high->commodity_1h` score `-1.9507` n `225` status `ready` deltaP `1.5462` edge `-0.0046` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
