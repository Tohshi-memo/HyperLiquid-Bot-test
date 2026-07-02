# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T19:57:46.002684+00:00`
- Price records: `672`
- Market context records: `5488`
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

- `market_context_high->crypto_major_24h` score `3.3552` n `190` status `ready` deltaP `16.2189` edge `0.6255` maxDD `-29.6555`
- `market_context_high->equity_4h` score `3.0431` n `193` status `ready` deltaP `13.9738` edge `0.3243` maxDD `-7.4425`
- `market_context_high->crypto_major_4h` score `2.5611` n `193` status `ready` deltaP `14.0362` edge `0.3491` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.2351` n `193` status `ready` deltaP `10.8658` edge `0.2779` maxDD `-9.46`
- `market_context_high->equity_24h` score `1.8417` n `190` status `ready` deltaP `10.7511` edge `0.5897` maxDD `-31.6316`
- `market_context_high->equity_1h` score `0.6778` n `193` status `ready` deltaP `9.6313` edge `0.0888` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.265` n `193` status `ready` deltaP `7.893` edge `0.0188` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.2343` n `190` status `ready` deltaP `11.5424` edge `0.0353` maxDD `-1.0847`
- `market_context_high->crypto_alt_1h` score `-0.3132` n `193` status `ready` deltaP `1.2837` edge `0.0615` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.3299` n `193` status `ready` deltaP `0.9269` edge `0.0004` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.4121` n `193` status `ready` deltaP `2.8614` edge `0.0141` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.4823` n `193` status `ready` deltaP `2.5736` edge `0.0672` maxDD `-6.9639`
- `market_context_high->index_4h` score `-0.6094` n `193` status `ready` deltaP `8.8857` edge `0.0509` maxDD `-2.874`
- `market_context_high->fx_4h` score `-0.8322` n `193` status `ready` deltaP `3.3663` edge `0.0063` maxDD `-1.5143`
- `market_context_high->commodity_1h` score `-1.5303` n `193` status `ready` deltaP `-3.575` edge `-0.0089` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.7514` n `190` status `ready` deltaP `14.2708` edge `0.079` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.6883` n `193` status `ready` deltaP `-8.5792` edge `-0.035` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.356` n `193` status `ready` deltaP `-6.9616` edge `-0.0493` maxDD `-14.0497`
- `market_context_high->crypto_alt_24h` score `-7.1594` n `190` status `ready` deltaP `7.2442` edge `0.2248` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.2143` n `190` status `ready` deltaP `-4.2379` edge `-0.1589` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
