# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T08:07:28.924631+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4964`

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

- `market_context_high->unknown_4h` score `222.2191` n `62` status `ready` deltaP `7.8777` edge `18.4801` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `175.4704` n `74` status `ready` deltaP `1.1531` edge `14.6563` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `13.7719` n `46` status `ready` deltaP `31.388` edge `1.0657` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `12.7269` n `46` status `ready` deltaP `37.8306` edge `0.8736` maxDD `-4.5519`
- `news_risk_high->crypto_major_4h` score `11.124` n `65` status `ready` deltaP `40.1736` edge `0.6795` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `10.9532` n `59` status `ready` deltaP `28.229` edge `0.7346` maxDD `-0.1353`
- `news_risk_high->crypto_alt_4h` score `7.5145` n `65` status `ready` deltaP `24.5122` edge `0.5972` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.2607` n `62` status `ready` deltaP `22.0594` edge `0.445` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.4545` n `62` status `ready` deltaP `20.3187` edge `0.448` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.7207` n `59` status `ready` deltaP `31.8891` edge `0.1808` maxDD `0.0`
- `market_context_high->equity_24h` score `3.9791` n `46` status `ready` deltaP `8.9217` edge `0.3718` maxDD `-6.3081`
- `news_risk_high->equity_4h` score `3.9701` n `65` status `ready` deltaP `27.4367` edge `0.2092` maxDD `-2.9013`
- `news_risk_high->index_4h` score `3.2196` n `65` status `ready` deltaP `35.1149` edge `0.0604` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `3.0407` n `65` status `ready` deltaP `13.3095` edge `0.2002` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.6681` n `74` status `ready` deltaP `17.426` edge `0.1512` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.5646` n `65` status `ready` deltaP `21.9747` edge `0.1088` maxDD `-0.993`
- `market_context_high->crypto_alt_1h` score `2.2384` n `74` status `ready` deltaP `13.8251` edge `0.169` maxDD `-3.6376`
- `news_risk_high->index_1h` score `2.1944` n `65` status `ready` deltaP `26.9645` edge `0.0181` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.5607` n `65` status `ready` deltaP `4.719` edge `0.1505` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.2559` n `46` status `ready` deltaP `23.687` edge `0.1049` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
