# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T02:22:26.233655+00:00`
- Price records: `672`
- Market context records: `4997`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10448`

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

- `market_context_high->unknown_1h` score `16.5786` n `93` status `ready` deltaP `4.7164` edge `1.4002` maxDD `-1.674`
- `market_context_high->unknown_24h` score `6.2401` n `74` status `ready` deltaP `29.8142` edge `0.3555` maxDD `-1.4072`
- `market_context_high->crypto_major_4h` score `6.1822` n `87` status `ready` deltaP `17.944` edge `0.5441` maxDD `-7.8836`
- `market_context_high->crypto_alt_4h` score `5.137` n `87` status `ready` deltaP `12.4317` edge `0.4846` maxDD `-7.8181`
- `market_context_high->unknown_4h` score `1.6161` n `87` status `ready` deltaP `21.1943` edge `0.0956` maxDD `-5.5109`
- `market_context_high->metal_4h` score `1.1109` n `87` status `ready` deltaP `11.0352` edge `0.1269` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8465` n `93` status `ready` deltaP `7.8874` edge `0.0753` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8261` n `93` status `ready` deltaP `6.2536` edge `0.1189` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.6812` n `87` status `ready` deltaP `5.9224` edge `0.186` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.4574` n `87` status `ready` deltaP `6.3674` edge `0.0439` maxDD `-0.8587`
- `market_context_high->metal_1h` score `0.3604` n `93` status `ready` deltaP `6.2536` edge `0.038` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1664` n `93` status `ready` deltaP `4.961` edge `0.0905` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.2299` n `74` status `ready` deltaP `6.2594` edge `0.005` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.3197` n `93` status `ready` deltaP `1.7079` edge `0.0136` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.6066` n `93` status `ready` deltaP `1.6129` edge `0.0128` maxDD `-0.5946`
- `market_context_high->fx_4h` score `-0.8081` n `87` status `ready` deltaP `-0.8796` edge `-0.0007` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.339` n `87` status `ready` deltaP `3.2819` edge `-0.0082` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.7581` n `93` status `ready` deltaP `-11.9986` edge `-0.0055` maxDD `-0.5482`
- `market_context_high->commodity_24h` score `-4.056` n `74` status `ready` deltaP `6.8365` edge `-0.0547` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-4.198` n `74` status `ready` deltaP `-0.3472` edge `0.0096` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
