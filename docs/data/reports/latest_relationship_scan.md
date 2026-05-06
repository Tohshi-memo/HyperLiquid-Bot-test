# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T17:22:21.319438+00:00`
- Price records: `473`
- Market context records: `565`
- Flow alert records: `1593`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `4.8675` n `142` status `ready` deltaP `7.5186` edge `0.3603` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.013` n `142` status `ready` deltaP `9.8517` edge `0.2188` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.0094` n `146` status `ready` deltaP `9.8748` edge `0.0201` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3247` n `146` status `ready` deltaP `1.7955` edge `0.0042` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5487` n `146` status `ready` deltaP `1.9237` edge `0.0389` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6291` n `146` status `ready` deltaP `0.9589` edge `-0.0017` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1953` n `146` status `ready` deltaP `-1.4067` edge `-0.0092` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.1992` n `146` status `ready` deltaP `-3.9898` edge `-0.013` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3814` n `146` status `ready` deltaP `4.0424` edge `-0.0106` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.8527` n `142` status `ready` deltaP `-5.8169` edge `0.0839` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-1.9966` n `146` status `ready` deltaP `3.5122` edge `-0.0175` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.0319` n `146` status `ready` deltaP `1.4923` edge `-0.027` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.2296` n `146` status `ready` deltaP `2.7712` edge `0.0527` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-3.045` n `146` status `ready` deltaP `-2.4812` edge `-0.022` maxDD `-10.5498`
- `market_context_high->crypto_major_4h` score `-3.217` n `146` status `ready` deltaP `9.9922` edge `0.0359` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.271` n `146` status `ready` deltaP `-4.4032` edge `-0.0473` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5475` n `146` status `ready` deltaP `-5.93` edge `0.094` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.743` n `142` status `ready` deltaP `-10.0706` edge `0.0157` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.4293` n `142` status `ready` deltaP `-5.275` edge `-0.0391` maxDD `-19.1542`
- `market_context_high->unknown_4h` score `-5.3823` n `146` status `ready` deltaP `-0.1964` edge `-0.2594` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
