# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T18:17:53.511125+00:00`
- Price records: `672`
- Market context records: `5480`
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

- `market_context_high->crypto_major_24h` score `3.3612` n `190` status `ready` deltaP `16.2189` edge `0.626` maxDD `-29.6555`
- `market_context_high->equity_4h` score `2.8384` n `193` status `ready` deltaP `13.3641` edge `0.3113` maxDD `-7.4425`
- `market_context_high->crypto_major_4h` score `2.4385` n `193` status `ready` deltaP `13.8838` edge `0.3399` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.0979` n `193` status `ready` deltaP `10.5609` edge `0.2685` maxDD `-9.46`
- `market_context_high->equity_24h` score `1.5297` n `190` status `ready` deltaP `10.7511` edge `0.5637` maxDD `-31.6316`
- `market_context_high->equity_1h` score `0.6562` n `193` status `ready` deltaP `9.4816` edge `0.088` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.2554` n `193` status `ready` deltaP `7.7433` edge `0.019` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.2319` n `190` status `ready` deltaP `11.5424` edge `0.0351` maxDD `-1.0847`
- `market_context_high->fx_1h` score `-0.3136` n `193` status `ready` deltaP `1.2263` edge `0.0005` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.369` n `193` status `ready` deltaP `3.3105` edge `0.0147` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.3695` n `193` status `ready` deltaP `0.9843` edge `0.0588` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.5267` n `193` status `ready` deltaP `2.4239` edge `0.0645` maxDD `-6.9639`
- `market_context_high->index_4h` score `-0.6748` n `193` status `ready` deltaP `8.4284` edge `0.0485` maxDD `-2.874`
- `market_context_high->fx_4h` score `-0.8346` n `193` status `ready` deltaP `3.3663` edge `0.0061` maxDD `-1.5143`
- `market_context_high->commodity_1h` score `-1.5123` n `193` status `ready` deltaP `-3.4253` edge `-0.0084` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.7522` n `190` status `ready` deltaP `14.2708` edge `0.0789` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.6891` n `193` status `ready` deltaP `-8.5792` edge `-0.0351` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2384` n `193` status `ready` deltaP `-6.047` edge `-0.0456` maxDD `-14.0497`
- `market_context_high->metal_24h` score `-7.1972` n `190` status `ready` deltaP `-4.2379` edge `-0.1567` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-7.2602` n `190` status `ready` deltaP `7.2442` edge `0.2164` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
