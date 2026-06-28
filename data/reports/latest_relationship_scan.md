# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T12:07:25.553648+00:00`
- Price records: `672`
- Market context records: `5038`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10202`

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

- `market_context_high->unknown_1h` score `13.2607` n `97` status `ready` deltaP `2.6931` edge `1.1372` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.0429` n `93` status `ready` deltaP `22.3642` edge `0.7067` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.4503` n `93` status `ready` deltaP `16.4897` edge `0.5027` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.2972` n `93` status `ready` deltaP `14.1785` edge `0.4863` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.2148` n `93` status `ready` deltaP `12.9343` edge `0.1229` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8663` n `97` status `ready` deltaP `8.6302` edge `0.072` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.7749` n `97` status `ready` deltaP `6.4695` edge `0.1132` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.3742` n `93` status `ready` deltaP `2.3587` edge `0.1704` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3395` n `97` status `ready` deltaP `6.1871` edge `0.0367` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.2205` n `97` status `ready` deltaP `5.6871` edge `0.0926` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.0019` n `74` status `ready` deltaP `10.2525` edge `0.0076` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.219` n `93` status `ready` deltaP `2.7996` edge `0.0392` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.261` n `97` status `ready` deltaP `2.4616` edge `0.0161` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5808` n `97` status `ready` deltaP `1.9955` edge `0.0124` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.7641` n `93` status `ready` deltaP `4.1552` edge `-0.0004` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0173` n `93` status `ready` deltaP `-4.3732` edge `-0.0024` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.6256` n `97` status `ready` deltaP `-10.3417` edge `-0.0055` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-3.6451` n `74` status `ready` deltaP `6.25` edge `0.0365` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.6772` n `74` status `ready` deltaP `0.0657` edge `-0.0892` maxDD `-27.5371`
- `market_context_high->unknown_24h` score `-5.6582` n `74` status `ready` deltaP `27.0364` edge `-0.6175` maxDD `-1.4072`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
