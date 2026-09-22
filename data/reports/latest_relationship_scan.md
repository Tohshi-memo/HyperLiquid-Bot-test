# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T00:37:38.232474+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9964`

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

- `market_context_high->unknown_4h` score `36.7184` n `53` status `ready` deltaP `5.5827` edge `3.0293` maxDD `-0.1988`
- `market_context_high->crypto_major_24h` score `18.5256` n `51` status `ready` deltaP `12.0404` edge `1.8621` maxDD `-28.8854`
- `news_risk_high->crypto_major_24h` score `10.8788` n `101` status `ready` deltaP `-0.0155` edge `1.5925` maxDD `-46.1999`
- `market_context_high->equity_24h` score `9.1834` n `51` status `ready` deltaP `5.2696` edge `0.906` maxDD `-11.0675`
- `news_risk_high->crypto_alt_24h` score `6.3632` n `101` status `ready` deltaP `0.3695` edge `1.0159` maxDD `-32.7147`
- `market_context_high->crypto_alt_24h` score `3.686` n `51` status `ready` deltaP `10.4064` edge `0.6308` maxDD `-29.1077`
- `market_context_high->index_24h` score `3.3771` n `51` status `ready` deltaP `9.2626` edge `0.2715` maxDD `-1.1461`
- `news_risk_high->crypto_alt_4h` score `3.0752` n `101` status `ready` deltaP `14.9556` edge `0.2775` maxDD `-7.675`
- `news_risk_high->commodity_24h` score `2.528` n `101` status `ready` deltaP `31.1829` edge `0.2468` maxDD `-3.4467`
- `news_risk_high->crypto_alt_1h` score `2.3553` n `101` status `ready` deltaP `14.435` edge `0.1466` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.1428` n `101` status `ready` deltaP `16.3276` edge `0.1955` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.6264` n `101` status `ready` deltaP `15.932` edge `0.0816` maxDD `-2.8494`
- `news_risk_high->fx_4h` score `0.5276` n `101` status `ready` deltaP `11.9943` edge `0.0276` maxDD `-0.421`
- `news_risk_high->metal_1h` score `0.4412` n `101` status `ready` deltaP `12.8016` edge `0.0116` maxDD `-0.8144`
- `market_context_high->equity_1h` score `0.3662` n `53` status `ready` deltaP `2.5337` edge `0.0384` maxDD `-0.3155`
- `market_context_high->index_1h` score `0.3396` n `53` status `ready` deltaP `6.6659` edge `0.0093` maxDD `-0.0354`
- `market_context_high->index_4h` score `0.2678` n `53` status `ready` deltaP `12.6294` edge `0.0032` maxDD `-0.9115`
- `market_context_high->fx_1h` score `0.242` n `53` status `ready` deltaP `7.4427` edge `0.0062` maxDD `-0.1854`
- `news_risk_high->metal_4h` score `0.1979` n `101` status `ready` deltaP `13.4403` edge `0.0323` maxDD `-2.0994`
- `market_context_high->metal_24h` score `0.1729` n `51` status `ready` deltaP `17.0241` edge `-0.0757` maxDD `-0.2042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
