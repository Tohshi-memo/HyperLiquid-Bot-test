# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T14:07:19.154106+00:00`
- Price records: `556`
- Market context records: `652`
- Flow alert records: `1851`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `795`

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

- `market_context_high->crypto_major_24h` score `7.5128` n `146` status `ready` deltaP `19.8243` edge `0.5273` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.0582` n `146` status `ready` deltaP `8.6629` edge `0.4519` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1544` n `146` status `ready` deltaP `8.0326` edge `0.0138` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3568` n `146` status `ready` deltaP `1.3748` edge `0.0029` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4048` n `146` status `ready` deltaP `2.5072` edge `0.047` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.629` n `146` status `ready` deltaP `0.5574` edge `0.001` maxDD `-2.8282`
- `market_context_high->crypto_alt_1h` score `-1.2163` n `146` status `ready` deltaP `5.5068` edge `-0.0066` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2196` n `146` status `ready` deltaP `-1.8148` edge `-0.0085` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.2213` n `146` status `ready` deltaP `-4.6704` edge `-0.0103` maxDD `-2.1602`
- `market_context_high->crypto_major_1h` score `-1.6456` n `146` status `ready` deltaP `5.7847` edge `-0.0034` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.0845` n `146` status `ready` deltaP `3.9548` edge `0.0569` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.1159` n `146` status `ready` deltaP `0.5163` edge `-0.0275` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.2832` n `146` status `ready` deltaP `14.5104` edge `0.0836` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.92` n `146` status `ready` deltaP `-9.0033` edge `0.0162` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.1056` n `146` status `ready` deltaP `-4.1862` edge `0.1192` maxDD `-13.0076`
- `market_context_high->equity_4h` score `-3.3201` n `146` status `ready` deltaP `-3.7748` edge `-0.0363` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4356` n `146` status `ready` deltaP `-5.0502` edge `-0.0567` maxDD `-9.0076`
- `market_context_high->fx_24h` score `-4.5411` n `146` status `ready` deltaP `-5.882` edge `-0.0258` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.7021` n `146` status `ready` deltaP `-11.4996` edge `-0.0547` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.9318` n `146` status `ready` deltaP `0.3653` edge `-0.2256` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
