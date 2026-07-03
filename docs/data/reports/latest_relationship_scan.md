# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T03:37:36.108012+00:00`
- Price records: `672`
- Market context records: `5520`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11432`

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

- `market_context_high->equity_24h` score `3.4354` n `190` status `ready` deltaP `13.1817` edge `0.7063` maxDD `-31.6316`
- `market_context_high->crypto_major_24h` score `2.7012` n `190` status `ready` deltaP `16.2189` edge `0.571` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.5813` n `193` status `ready` deltaP `13.8838` edge `0.3518` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `1.9605` n `193` status `ready` deltaP `9.189` edge `0.2662` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.9092` n `193` status `ready` deltaP `10.3153` edge `0.2542` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.397` n `190` status `ready` deltaP `12.9312` edge `0.0396` maxDD `-1.0847`
- `market_context_high->equity_1h` score `0.2545` n `193` status `ready` deltaP `7.6852` edge `0.0665` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0133` n `193` status `ready` deltaP `5.4978` edge `0.0138` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.3572` n `193` status `ready` deltaP `0.4778` edge `-0.0001` maxDD `-0.577`
- `market_context_high->crypto_alt_1h` score `-0.3707` n `193` status `ready` deltaP `0.9843` edge `0.0587` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.4691` n `193` status `ready` deltaP `2.5736` edge `0.0683` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.6985` n `193` status `ready` deltaP `0.4662` edge `0.0062` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.955` n `193` status `ready` deltaP `2.1468` edge `0.0042` maxDD `-1.5143`
- `market_context_high->index_4h` score `-1.0953` n `193` status `ready` deltaP `5.2272` edge `0.0348` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.6417` n `193` status `ready` deltaP `-4.6229` edge `-0.0112` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8279` n `190` status `ready` deltaP `14.2708` edge `0.0692` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0336` n `193` status `ready` deltaP `-12.0853` edge `-0.0559` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.5829` n `193` status `ready` deltaP `-8.9433` edge `-0.055` maxDD `-14.0497`
- `market_context_high->crypto_alt_24h` score `-7.139` n `190` status `ready` deltaP `7.2442` edge `0.2265` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.315` n `190` status `ready` deltaP `-4.2379` edge `-0.1718` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
