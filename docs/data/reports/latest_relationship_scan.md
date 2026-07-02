# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T18:07:34.364596+00:00`
- Price records: `672`
- Market context records: `5479`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11467`

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

- `market_context_high->crypto_major_24h` score `3.3648` n `190` status `ready` deltaP `16.2189` edge `0.6263` maxDD `-29.6555`
- `market_context_high->equity_4h` score `2.7928` n `193` status `ready` deltaP `13.3641` edge `0.3075` maxDD `-7.4425`
- `market_context_high->crypto_major_4h` score `2.4325` n `193` status `ready` deltaP `13.8838` edge `0.3394` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.0749` n `193` status `ready` deltaP `10.4085` edge `0.2676` maxDD `-9.46`
- `market_context_high->equity_24h` score `1.4697` n `190` status `ready` deltaP `10.7511` edge `0.5587` maxDD `-31.6316`
- `market_context_high->equity_1h` score `0.661` n `193` status `ready` deltaP `9.4816` edge `0.0884` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.2566` n `193` status `ready` deltaP `7.7433` edge `0.0191` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.2319` n `190` status `ready` deltaP `11.5424` edge `0.0351` maxDD `-1.0847`
- `market_context_high->fx_1h` score `-0.3136` n `193` status `ready` deltaP `1.2263` edge `0.0005` maxDD `-0.577`
- `market_context_high->crypto_alt_1h` score `-0.3431` n `193` status `ready` deltaP `1.134` edge `0.06` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.3678` n `193` status `ready` deltaP `3.3105` edge `0.0148` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.5159` n `193` status `ready` deltaP `2.4239` edge `0.0654` maxDD `-6.9639`
- `market_context_high->index_4h` score `-0.6832` n `193` status `ready` deltaP `8.4284` edge `0.0478` maxDD `-2.874`
- `market_context_high->fx_4h` score `-0.8358` n `193` status `ready` deltaP `3.3663` edge `0.006` maxDD `-1.5143`
- `market_context_high->commodity_1h` score `-1.5111` n `193` status `ready` deltaP `-3.4253` edge `-0.0083` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.753` n `190` status `ready` deltaP `14.2708` edge `0.0788` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.6883` n `193` status `ready` deltaP `-8.5792` edge `-0.035` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.219` n `193` status `ready` deltaP `-5.8946` edge `-0.045` maxDD `-14.0497`
- `market_context_high->metal_24h` score `-7.1948` n `190` status `ready` deltaP `-4.2379` edge `-0.1564` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-7.2722` n `190` status `ready` deltaP `7.2442` edge `0.2154` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
