# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T12:52:18.004892+00:00`
- Price records: `672`
- Market context records: `1631`
- Flow alert records: `6606`
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

- `market_context_high->metal_24h` score `10.2553` n `184` status `ready` deltaP `26.897` edge `0.9179` maxDD `-12.7414`
- `market_context_high->index_24h` score `3.2502` n `184` status `ready` deltaP `19.0274` edge `0.2818` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.4169` n `186` status `ready` deltaP `11.7494` edge `0.1492` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `1.2664` n `186` status `ready` deltaP `16.3573` edge `0.3295` maxDD `-17.0956`
- `market_context_high->equity_24h` score `0.616` n `184` status `ready` deltaP `17.5468` edge `0.4242` maxDD `-33.1875`
- `market_context_high->crypto_major_4h` score `0.5766` n `186` status `ready` deltaP `12.1373` edge `0.2639` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.249` n `197` status `ready` deltaP `1.5805` edge `0.0599` maxDD `-4.1892`
- `market_context_high->fx_24h` score `-0.3207` n `184` status `ready` deltaP `7.4071` edge `0.0288` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.5345` n `197` status `ready` deltaP `1.126` edge `0.0288` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.5517` n `197` status `ready` deltaP `-0.6305` edge `-0.0033` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6428` n `197` status `ready` deltaP `0.7057` edge `0.0049` maxDD `-1.7205`
- `market_context_high->crypto_major_24h` score `-0.6941` n `184` status `ready` deltaP `23.0606` edge `0.647` maxDD `-62.3533`
- `market_context_high->index_4h` score `-0.8519` n `186` status `ready` deltaP `0.2258` edge `0.0364` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.8959` n `197` status `ready` deltaP `-1.4932` edge `0.0282` maxDD `-5.9819`
- `market_context_high->commodity_1h` score `-0.9958` n `197` status `ready` deltaP `1.1632` edge `0.0014` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.3593` n `197` status `ready` deltaP `2.5365` edge `0.0034` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.4385` n `186` status `ready` deltaP `8.1921` edge `0.0947` maxDD `-12.5349`
- `market_context_high->crypto_alt_24h` score `-2.0275` n `184` status `ready` deltaP `23.2725` edge `0.8568` maxDD `-88.8062`
- `market_context_high->fx_4h` score `-2.0311` n `186` status `ready` deltaP `-9.4` edge `-0.0137` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-4.1214` n `186` status `ready` deltaP `7.7651` edge `-0.1681` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
