# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T06:52:20.861455+00:00`
- Price records: `672`
- Market context records: `1710`
- Flow alert records: `6831`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->unknown_24h` score `19.6332` n `139` status `ready` deltaP `17.7367` edge `2.0499` maxDD `-35.8966`
- `market_context_high->unknown_4h` score `6.4094` n `197` status `ready` deltaP `13.9547` edge `0.6682` maxDD `-11.1695`
- `market_context_high->metal_24h` score `6.4056` n `139` status `ready` deltaP `25.1848` edge `0.6085` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.837` n `197` status `ready` deltaP `21.6758` edge `0.525` maxDD `-16.3135`
- `market_context_high->crypto_major_4h` score `4.099` n `197` status `ready` deltaP `23.2458` edge `0.4575` maxDD `-13.3376`
- `market_context_high->index_24h` score `3.5542` n `139` status `ready` deltaP `16.4521` edge `0.3243` maxDD `-5.3574`
- `market_context_high->equity_4h` score `2.9214` n `197` status `ready` deltaP `16.3357` edge `0.244` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.219` n `139` status `ready` deltaP `15.3045` edge `0.4894` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.8933` n `197` status `ready` deltaP `7.8612` edge `0.1244` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.4674` n `197` status `ready` deltaP `8.4669` edge `0.0914` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.2613` n `197` status `ready` deltaP `5.2061` edge `0.0947` maxDD `-3.9439`
- `market_context_high->equity_1h` score `-0.0064` n `197` status `ready` deltaP `4.3527` edge `0.0513` maxDD `-2.8014`
- `market_context_high->crypto_alt_24h` score `-0.091` n `139` status `ready` deltaP `23.6738` edge `1.0155` maxDD `-88.8062`
- `market_context_high->metal_4h` score `-0.3153` n `197` status `ready` deltaP `12.8954` edge `0.1428` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.4783` n `197` status `ready` deltaP `0.7668` edge `0.0182` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.4858` n `197` status `ready` deltaP `5.8049` edge `0.0326` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6464` n `197` status `ready` deltaP `-2.8572` edge `-0.0006` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.8423` n `139` status `ready` deltaP `4.1871` edge `0.0068` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `-1.0685` n `139` status `ready` deltaP `21.8703` edge `0.5758` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-1.7837` n `197` status `ready` deltaP `-6.9078` edge `-0.0097` maxDD `-1.4313`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
