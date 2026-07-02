# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T19:22:30.256712+00:00`
- Price records: `672`
- Market context records: `5485`
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

- `market_context_high->crypto_major_24h` score `3.3456` n `190` status `ready` deltaP `16.2189` edge `0.6247` maxDD `-29.6555`
- `market_context_high->equity_4h` score `2.9659` n `193` status `ready` deltaP `13.669` edge `0.3199` maxDD `-7.4425`
- `market_context_high->crypto_major_4h` score `2.4901` n `193` status `ready` deltaP `13.8838` edge `0.3442` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.1725` n `193` status `ready` deltaP `10.7134` edge `0.2737` maxDD `-9.46`
- `market_context_high->equity_24h` score `1.7373` n `190` status `ready` deltaP `10.7511` edge `0.581` maxDD `-31.6316`
- `market_context_high->equity_1h` score `0.6538` n `193` status `ready` deltaP `9.4816` edge `0.0878` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.253` n `193` status `ready` deltaP `7.7433` edge `0.0188` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.2331` n `190` status `ready` deltaP `11.5424` edge `0.0352` maxDD `-1.0847`
- `market_context_high->fx_1h` score `-0.3377` n `193` status `ready` deltaP `0.7772` edge `0.0004` maxDD `-0.577`
- `market_context_high->crypto_alt_1h` score `-0.3647` n `193` status `ready` deltaP `0.9843` edge `0.0592` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.4145` n `193` status `ready` deltaP `2.8614` edge `0.0139` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.5338` n `193` status `ready` deltaP `2.2742` edge `0.0649` maxDD `-6.9639`
- `market_context_high->index_4h` score `-0.6422` n `193` status `ready` deltaP `8.5808` edge `0.0502` maxDD `-2.874`
- `market_context_high->fx_4h` score `-0.831` n `193` status `ready` deltaP `3.3663` edge `0.0064` maxDD `-1.5143`
- `market_context_high->commodity_1h` score `-1.5147` n `193` status `ready` deltaP `-3.4253` edge `-0.0086` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.7499` n `190` status `ready` deltaP `14.2708` edge `0.0792` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.6906` n `193` status `ready` deltaP `-8.5792` edge `-0.0353` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3184` n `193` status `ready` deltaP `-6.6568` edge `-0.0482` maxDD `-14.0497`
- `market_context_high->crypto_alt_24h` score `-7.2026` n `190` status `ready` deltaP `7.2442` edge `0.2212` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.2089` n `190` status `ready` deltaP `-4.2379` edge `-0.1582` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
