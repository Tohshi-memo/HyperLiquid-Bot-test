# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T04:22:32.908248+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8730`

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

- `market_context_high->unknown_24h` score `1224.1432` n `114` status `ready` deltaP `10.9283` edge `101.9771` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `30.1157` n `114` status `ready` deltaP `-0.7006` edge `2.5682` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.7788` n `62` status `ready` deltaP `34.9233` edge `0.6024` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.1573` n `62` status `ready` deltaP `21.2579` edge `0.5058` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.3651` n `114` status `ready` deltaP `16.672` edge `0.2657` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.1096` n `62` status `ready` deltaP `21.875` edge `0.1133` maxDD `0.0`
- `news_risk_high->index_4h` score `2.7008` n `62` status `ready` deltaP `30.3256` edge `0.0491` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.1135` n `62` status `ready` deltaP `7.7796` edge `0.1598` maxDD `-1.5096`
- `news_risk_high->equity_24h` score `1.9` n `62` status `ready` deltaP `2.9234` edge `0.1488` maxDD `-0.1298`
- `news_risk_high->index_1h` score `1.8881` n `62` status `ready` deltaP `23.9763` edge `0.0125` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.6866` n `62` status `ready` deltaP `16.252` edge `0.092` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.2537` n `62` status `ready` deltaP `18.0468` edge `0.082` maxDD `-0.993`
- `market_context_high->crypto_alt_4h` score `1.2059` n `114` status `ready` deltaP `0.9975` edge `0.2662` maxDD `-7.1222`
- `market_context_high->crypto_major_24h` score `1.188` n `114` status `ready` deltaP `6.9718` edge `0.3499` maxDD `-16.7906`
- `news_risk_high->crypto_alt_1h` score `0.9715` n `62` status `ready` deltaP `2.7091` edge `0.1148` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.8873` n `62` status `ready` deltaP `28.9315` edge `0.0775` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.829` n `114` status `ready` deltaP `18.9533` edge `0.0184` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.7365` n `114` status `ready` deltaP `12.7298` edge `0.0049` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.5088` n `114` status `ready` deltaP `12.0908` edge `0.0318` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.236` n `114` status `ready` deltaP `7.1883` edge `0.0114` maxDD `-0.5059`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
