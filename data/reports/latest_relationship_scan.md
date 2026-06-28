# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T04:37:28.241778+00:00`
- Price records: `672`
- Market context records: `5006`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10258`

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

- `market_context_high->unknown_1h` score `15.4051` n `93` status `ready` deltaP `4.1176` edge `1.3064` maxDD `-1.674`
- `market_context_high->unknown_4h` score `11.0831` n `93` status `ready` deltaP `22.5167` edge `0.8757` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.6905` n `93` status `ready` deltaP `17.5568` edge `0.5156` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.2178` n `93` status `ready` deltaP `14.0261` edge `0.4807` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `4.6547` n `74` status `ready` deltaP `29.467` edge `0.2257` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.3157` n `93` status `ready` deltaP `14.0014` edge `0.1242` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8776` n `93` status `ready` deltaP `8.1868` edge `0.0759` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8105` n `93` status `ready` deltaP `6.2536` edge `0.1176` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.5096` n `93` status `ready` deltaP `3.8831` edge `0.1776` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3233` n `93` status `ready` deltaP `5.8045` edge `0.0379` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1243` n `93` status `ready` deltaP `4.5119` edge `0.0881` maxDD `-5.5126`
- `market_context_high->index_4h` score `-0.0669` n `93` status `ready` deltaP `4.4764` edge `0.0407` maxDD `-1.0893`
- `market_context_high->fx_24h` score `-0.1432` n `74` status `ready` deltaP `7.8219` edge `0.0057` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.2683` n `93` status `ready` deltaP `2.4564` edge `0.0152` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5694` n `93` status `ready` deltaP `2.062` edge `0.0129` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.7978` n `93` status `ready` deltaP `4.0028` edge `-0.0037` maxDD `-5.021`
- `market_context_high->fx_4h` score `-0.984` n `93` status `ready` deltaP `-3.7634` edge `-0.0022` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.7342` n `93` status `ready` deltaP `-11.6992` edge `-0.0055` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-4.0949` n `74` status `ready` deltaP `1.2153` edge `0.0124` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.2114` n `74` status `ready` deltaP `5.274` edge `-0.0642` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
