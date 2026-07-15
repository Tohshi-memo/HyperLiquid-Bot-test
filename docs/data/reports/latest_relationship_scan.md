# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T12:52:31.787298+00:00`
- Price records: `672`
- Market context records: `6818`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `0.8499` n `176` status `ready` deltaP `-1.5467` edge `0.4945` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.3659` n `176` status `ready` deltaP `10.9217` edge `0.1445` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.255` n `199` status `ready` deltaP `5.7142` edge `0.0152` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.4005` n `199` status `ready` deltaP `-0.4115` edge `-0.0001` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4874` n `199` status `ready` deltaP `3.2551` edge `0.0141` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.8064` n `199` status `ready` deltaP `-3.7583` edge `-0.0041` maxDD `-0.9382`
- `market_context_high->metal_1h` score `-0.9857` n `199` status `ready` deltaP `-6.3454` edge `-0.0102` maxDD `-1.9098`
- `market_context_high->commodity_1h` score `-1.0352` n `199` status `ready` deltaP `-1.898` edge `-0.0053` maxDD `-2.1314`
- `market_context_high->fx_4h` score `-1.3483` n `187` status `ready` deltaP `5.3728` edge `-0.0023` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.3488` n `187` status `ready` deltaP `-2.1668` edge `-0.0095` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.6234` n `187` status `ready` deltaP `2.4235` edge `-0.0283` maxDD `-6.3458`
- `market_context_high->equity_1h` score `-1.7072` n `199` status `ready` deltaP `0.2295` edge `-0.0311` maxDD `-4.6821`
- `market_context_high->unknown_1h` score `-1.7635` n `199` status `ready` deltaP `-5.6931` edge `-0.0189` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.8442` n `187` status `ready` deltaP `-5.3272` edge `-0.0308` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.2837` n `187` status `ready` deltaP `-0.9399` edge `-0.082` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.4762` n `187` status `ready` deltaP `-13.5785` edge `0.0374` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-3.478` n `187` status `ready` deltaP `-1.4771` edge `-0.0777` maxDD `-20.6678`
- `market_context_high->fx_24h` score `-4.466` n `176` status `ready` deltaP `-9.7853` edge `-0.0033` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-4.9915` n `187` status `ready` deltaP `-0.1777` edge `-0.1849` maxDD `-29.3079`
- `market_context_high->metal_24h` score `-9.643` n `176` status `ready` deltaP `-21.9697` edge `-0.2413` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
