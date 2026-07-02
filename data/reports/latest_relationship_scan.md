# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T23:22:28.386253+00:00`
- Price records: `672`
- Market context records: `5502`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11468`

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

- `market_context_high->crypto_major_24h` score `3.1044` n `190` status `ready` deltaP `16.2189` edge `0.6046` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.5439` n `193` status `ready` deltaP `14.646` edge `0.3436` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.4838` n `193` status `ready` deltaP `11.9921` edge `0.2909` maxDD `-7.4425`
- `market_context_high->equity_24h` score `2.3721` n `190` status `ready` deltaP `10.7511` edge `0.6339` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `2.0835` n `193` status `ready` deltaP `10.5609` edge `0.2673` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.5939` n `193` status `ready` deltaP `9.1822` edge `0.0848` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.3627` n `190` status `ready` deltaP `12.7576` edge `0.0379` maxDD `-1.0847`
- `market_context_high->index_1h` score `0.1811` n `193` status `ready` deltaP `6.9948` edge `0.0178` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2316` n `193` status `ready` deltaP `1.5831` edge `0.0663` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.3324` n `193` status `ready` deltaP `3.3221` edge `0.0747` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.3463` n `193` status `ready` deltaP `0.6275` edge `0.0003` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.5247` n `193` status `ready` deltaP `1.6638` edge `0.0127` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.7665` n `193` status `ready` deltaP `4.1285` edge `0.0067` maxDD `-1.5143`
- `market_context_high->index_4h` score `-0.858` n `193` status `ready` deltaP `6.904` edge `0.0434` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.5099` n `193` status `ready` deltaP `-3.2756` edge `-0.0092` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.7959` n `190` status `ready` deltaP `14.2708` edge `0.0733` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.852` n `193` status `ready` deltaP `-10.4085` edge `-0.0438` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.4921` n `193` status `ready` deltaP `-8.3336` edge `-0.0515` maxDD `-14.0497`
- `market_context_high->crypto_alt_24h` score `-7.1462` n `190` status `ready` deltaP `7.2442` edge `0.2259` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.2775` n `190` status `ready` deltaP `-4.2379` edge `-0.167` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
