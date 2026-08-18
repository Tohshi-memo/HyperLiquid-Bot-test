# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T05:07:27.022815+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11837`

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

- `market_context_high->crypto_major_24h` score `3.2692` n `73` status `ready` deltaP `9.7078` edge `0.3285` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `0.613` n `73` status `ready` deltaP `12.6469` edge `0.1776` maxDD `-4.666`
- `market_context_high->metal_4h` score `0.5068` n `99` status `ready` deltaP `12.0165` edge `0.0197` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.2929` n `99` status `ready` deltaP `8.1671` edge `0.0852` maxDD `-3.1677`
- `market_context_high->metal_24h` score `0.1572` n `73` status `ready` deltaP `4.8384` edge `0.0703` maxDD `-2.49`
- `market_context_high->index_1h` score `0.0937` n `104` status `ready` deltaP `7.4735` edge `0.0034` maxDD `-0.2973`
- `market_context_high->commodity_4h` score `0.09` n `99` status `ready` deltaP `8.7199` edge `0.0344` maxDD `-2.4692`
- `market_context_high->equity_1h` score `0.0799` n `104` status `ready` deltaP `4.0074` edge `0.0314` maxDD `-1.496`
- `market_context_high->unknown_1h` score `-0.0118` n `104` status `ready` deltaP `7.8823` edge `-0.03` maxDD `-0.549`
- `market_context_high->fx_4h` score `-0.2235` n `99` status `ready` deltaP `3.1735` edge `0.0009` maxDD `-0.3904`
- `market_context_high->metal_1h` score `-0.3131` n `104` status `ready` deltaP `0.2994` edge `0.0007` maxDD `-0.7602`
- `market_context_high->fx_1h` score `-0.5053` n `104` status `ready` deltaP `-1.1746` edge `0.0019` maxDD `-0.2273`
- `market_context_high->crypto_alt_1h` score `-0.5253` n `104` status `ready` deltaP `0.0` edge `0.0149` maxDD `-2.5799`
- `market_context_high->crypto_alt_4h` score `-0.5555` n `99` status `ready` deltaP `6.1654` edge `0.0714` maxDD `-7.364`
- `market_context_high->commodity_1h` score `-0.6919` n `104` status `ready` deltaP `-4.2953` edge `0.0012` maxDD `-1.5684`
- `market_context_high->crypto_major_1h` score `-0.7066` n `104` status `ready` deltaP `-1.0479` edge `0.0058` maxDD `-3.1527`
- `market_context_high->equity_4h` score `-0.7757` n `99` status `ready` deltaP `-4.199` edge `0.019` maxDD `-2.5696`
- `market_context_high->index_4h` score `-0.8191` n `99` status `ready` deltaP `-1.646` edge `0.0047` maxDD `-0.2922`
- `market_context_high->unknown_24h` score `-0.8476` n `73` status `ready` deltaP `7.4049` edge `-0.0772` maxDD `-0.7574`
- `market_context_high->index_24h` score `-1.3916` n `73` status `ready` deltaP `0.9426` edge `-0.0855` maxDD `-3.2693`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
