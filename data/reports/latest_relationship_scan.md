# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T08:07:18.567356+00:00`
- Price records: `672`
- Market context records: `1098`
- Flow alert records: `5067`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->crypto_major_24h` score `16.8868` n `150` status `ready` deltaP `36.6875` edge `1.209` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `6.2003` n `150` status `ready` deltaP `13.0486` edge `0.5531` maxDD `-9.5387`
- `market_context_high->equity_24h` score `6.0707` n `150` status `ready` deltaP `15.6527` edge `0.4512` maxDD `-3.6396`
- `market_context_high->metal_24h` score `5.2074` n `150` status `ready` deltaP `-2.9305` edge `0.6202` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.8141` n `150` status `ready` deltaP `15.1319` edge `0.3311` maxDD `-2.1308`
- `market_context_high->equity_4h` score `2.0294` n `168` status `ready` deltaP `11.5564` edge `0.1584` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.0571` n `168` status `ready` deltaP `9.5092` edge `0.093` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5133` n `168` status `ready` deltaP `7.7951` edge `0.0225` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.316` n `168` status `ready` deltaP `2.7302` edge `0.0459` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1376` n `168` status `ready` deltaP `8.3155` edge `0.0016` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0346` n `168` status `ready` deltaP `6.9825` edge `0.0329` maxDD `-4.1256`
- `market_context_high->crypto_major_4h` score `-0.0021` n `168` status `ready` deltaP `8.1518` edge `0.1375` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.1813` n `168` status `ready` deltaP `7.1001` edge `-0.0014` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.3161` n `168` status `ready` deltaP `2.6447` edge `0.0403` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.6936` n `168` status `ready` deltaP `-1.1762` edge `-0.0003` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.6985` n `168` status `ready` deltaP `1.3937` edge `0.0008` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.1627` n `168` status `ready` deltaP `4.624` edge `0.1166` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.2035` n `168` status `ready` deltaP `7.7671` edge `-0.04` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.1274` n `168` status `ready` deltaP `-10.6635` edge `-0.0131` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.2197` n `150` status `ready` deltaP `3.0833` edge `-0.0257` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
