# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T02:52:25.176978+00:00`
- Price records: `672`
- Market context records: `5517`
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

- `market_context_high->equity_24h` score `3.1729` n `190` status `ready` deltaP `12.6609` edge `0.6879` maxDD `-31.6316`
- `market_context_high->crypto_major_24h` score `2.6736` n `190` status `ready` deltaP `16.2189` edge `0.5687` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.4517` n `193` status `ready` deltaP `13.8838` edge `0.341` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.9092` n `193` status `ready` deltaP `10.3153` edge `0.2542` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.8609` n `193` status `ready` deltaP `9.189` edge `0.2579` maxDD `-9.46`
- `market_context_high->fx_24h` score `0.3946` n `190` status `ready` deltaP `12.9312` edge `0.0394` maxDD `-1.0847`
- `market_context_high->equity_1h` score `0.2173` n `193` status `ready` deltaP `7.5355` edge `0.0644` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.001` n `193` status `ready` deltaP `5.3481` edge `0.0136` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.3401` n `193` status `ready` deltaP `0.7772` edge `0.0001` maxDD `-0.577`
- `market_context_high->crypto_alt_1h` score `-0.4667` n `193` status `ready` deltaP `0.6849` edge `0.0527` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.5758` n `193` status `ready` deltaP `2.2742` edge `0.0614` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.7177` n `193` status `ready` deltaP `0.3165` edge `0.0056` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.9088` n `193` status `ready` deltaP `2.6041` edge `0.005` maxDD `-1.5143`
- `market_context_high->index_4h` score `-1.0941` n `193` status `ready` deltaP `5.2272` edge `0.0349` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.6034` n `193` status `ready` deltaP `-4.1738` edge `-0.011` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.831` n `190` status `ready` deltaP `14.2708` edge `0.0688` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0359` n `193` status `ready` deltaP `-12.0853` edge `-0.0562` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.5757` n `193` status `ready` deltaP `-8.9433` edge `-0.0544` maxDD `-14.0497`
- `market_context_high->crypto_alt_24h` score `-7.229` n `190` status `ready` deltaP `7.2442` edge `0.219` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3212` n `190` status `ready` deltaP `-4.2379` edge `-0.1726` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
