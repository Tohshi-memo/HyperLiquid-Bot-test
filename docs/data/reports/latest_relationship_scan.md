# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T06:37:26.427792+00:00`
- Price records: `672`
- Market context records: `7001`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11539`

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

- `market_context_high->fx_1h` score `-0.2546` n `237` status `ready` deltaP `2.1842` edge `0.0013` maxDD `-0.5468`
- `market_context_high->unknown_24h` score `-0.2742` n `224` status `ready` deltaP `-5.5556` edge `0.4569` maxDD `-18.7342`
- `market_context_high->crypto_alt_1h` score `-0.2749` n `237` status `ready` deltaP `2.5797` edge `0.034` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.6577` n `237` status `ready` deltaP `0.8091` edge `0.0014` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.6975` n `237` status `ready` deltaP `-1.7907` edge `-0.0007` maxDD `-2.1427`
- `market_context_high->crypto_major_1h` score `-0.9187` n `237` status `ready` deltaP `3.927` edge `0.0325` maxDD `-7.1523`
- `market_context_high->fx_4h` score `-0.9447` n `237` status `ready` deltaP `11.7828` edge `0.0067` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.2071` n `237` status `ready` deltaP `-2.0756` edge `-0.0146` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.3178` n `237` status `ready` deltaP `-1.3821` edge `-0.0105` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6678` n `237` status `ready` deltaP `-4.2805` edge `-0.0363` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.753` n `237` status `ready` deltaP `8.1243` edge `-0.009` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.8292` n `237` status `ready` deltaP `3.7355` edge `-0.004` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.9123` n `237` status `ready` deltaP `6.5478` edge `0.0095` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.5588` n `237` status `ready` deltaP `-5.6666` edge `0.0611` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-2.6796` n `237` status `ready` deltaP `2.0403` edge `0.0214` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.1551` n `237` status `ready` deltaP `1.8524` edge `0.0116` maxDD `-24.6094`
- `market_context_high->commodity_24h` score `-3.8989` n `224` status `ready` deltaP `-6.4485` edge `-0.0951` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.4521` n `224` status `ready` deltaP `-7.3661` edge `-0.0172` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.2883` n `237` status `ready` deltaP `5.6878` edge `-0.0506` maxDD `-66.7371`
- `market_context_high->index_24h` score `-11.7111` n `224` status `ready` deltaP `-0.8432` edge `-0.0888` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
