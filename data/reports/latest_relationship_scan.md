# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T12:07:16.016934+00:00`
- Price records: `672`
- Market context records: `1115`
- Flow alert records: `5116`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8704`

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

- `market_context_high->crypto_major_24h` score `18.2766` n `150` status `ready` deltaP `39.4653` edge `1.3063` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `7.9045` n `150` status `ready` deltaP `15.8264` edge `0.6766` maxDD `-9.5387`
- `market_context_high->equity_24h` score `6.5685` n `150` status `ready` deltaP `16.5208` edge `0.4869` maxDD `-3.6396`
- `market_context_high->metal_24h` score `5.5619` n `150` status `ready` deltaP `-1.8889` edge `0.6428` maxDD `-6.3373`
- `market_context_high->index_24h` score `5.2235` n `150` status `ready` deltaP `15.4791` edge `0.3629` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.5894` n `168` status `ready` deltaP `9.1173` edge `0.138` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.8462` n `168` status `ready` deltaP `7.8324` edge `0.0866` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4893` n `168` status `ready` deltaP `7.6454` edge `0.0215` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2393` n `168` status `ready` deltaP `2.4308` edge `0.0415` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1232` n `168` status `ready` deltaP `8.1658` edge `0.0014` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `0.026` n `168` status `ready` deltaP `8.1518` edge `0.1411` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `0.0226` n `168` status `ready` deltaP `6.9825` edge `0.0319` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.2136` n `168` status `ready` deltaP `6.9504` edge `-0.0031` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.3113` n `168` status `ready` deltaP `2.6447` edge `0.0407` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.7049` n `168` status `ready` deltaP `1.2412` edge `0.001` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7364` n `168` status `ready` deltaP `-1.9247` edge `-0.0008` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-1.0286` n `168` status `ready` deltaP `5.5387` edge `0.1277` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.4202` n `168` status `ready` deltaP `6.2427` edge `-0.0479` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.1598` n `168` status `ready` deltaP `-11.1208` edge `-0.0142` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.3334` n `168` status `ready` deltaP `9.1609` edge `-0.2172` maxDD `-6.7322`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
