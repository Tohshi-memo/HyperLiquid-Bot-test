# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T11:22:20.373790+00:00`
- Price records: `672`
- Market context records: `2037`
- Flow alert records: `7756`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9105`

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

- `market_context_high->crypto_major_4h` score `8.8835` n `205` status `ready` deltaP `30.7927` edge `0.588` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.3814` n `205` status `ready` deltaP `24.5427` edge `0.6493` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.9113` n `205` status `ready` deltaP `18.9939` edge `0.4409` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.9771` n `205` status `ready` deltaP `17.2561` edge `0.2425` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.5356` n `205` status `ready` deltaP `12.4777` edge `0.1434` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.445` n `205` status `ready` deltaP `12.9269` edge `0.1026` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `1.4364` n `203` status `ready` deltaP `17.2117` edge `0.537` maxDD `-35.8966`
- `market_context_high->crypto_alt_1h` score `1.2629` n `205` status `ready` deltaP `10.0825` edge `0.1494` maxDD `-4.9097`
- `market_context_high->equity_24h` score `0.5744` n `203` status `ready` deltaP `16.3214` edge `0.4289` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.443` n `203` status `ready` deltaP `4.6887` edge `0.1285` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.208` n `205` status `ready` deltaP `6.9104` edge `0.0501` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.0565` n `205` status `ready` deltaP `4.0456` edge `0.0497` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.2822` n `205` status `ready` deltaP `2.7034` edge `0.0175` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.5511` n `203` status `ready` deltaP `10.6` edge `0.0217` maxDD `-2.7303`
- `market_context_high->metal_1h` score `-0.8179` n `205` status `ready` deltaP `4.1076` edge `0.0232` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8398` n `205` status `ready` deltaP `-1.1421` edge `0.0004` maxDD `-0.3548`
- `market_context_high->metal_4h` score `-1.093` n `205` status `ready` deltaP `9.1769` edge `0.11` maxDD `-11.9812`
- `market_context_high->fx_4h` score `-1.5282` n `205` status `ready` deltaP `-5.6707` edge `-0.0014` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.7908` n `203` status `ready` deltaP `9.87` edge `0.1335` maxDD `-20.5491`
- `market_context_high->crypto_major_24h` score `-1.8503` n `203` status `ready` deltaP `16.6182` edge `0.5936` maxDD `-62.3533`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
