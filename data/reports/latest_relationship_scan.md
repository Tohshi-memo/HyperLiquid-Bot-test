# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T09:52:27.416950+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9164`

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

- `market_context_high->unknown_4h` score `32.8549` n `58` status `ready` deltaP `1.23` edge `2.7447` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `22.2779` n `101` status `ready` deltaP `10.0539` edge `2.4753` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `16.8851` n `101` status `ready` deltaP `10.439` edge `1.8256` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.9127` n `101` status `ready` deltaP `17.6995` edge `0.329` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.5845` n `101` status `ready` deltaP `20.4434` edge `0.2882` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.5495` n `101` status `ready` deltaP `15.6326` edge `0.1548` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.9189` n `101` status `ready` deltaP `17.5787` edge `0.095` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.1834` n `101` status `ready` deltaP `23.3704` edge `0.1265` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.8151` n `58` status `ready` deltaP `6.1584` edge `0.0522` maxDD `-0.36`
- `market_context_high->index_1h` score `0.6813` n `58` status `ready` deltaP `10.2777` edge `0.0138` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.5322` n `101` status `ready` deltaP `13.8495` edge `0.0122` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.3714` n `58` status `ready` deltaP `9.075` edge `0.0061` maxDD `-0.1854`
- `news_risk_high->metal_4h` score `0.3273` n `101` status `ready` deltaP `15.1171` edge `0.0319` maxDD `-2.0994`
- `news_risk_high->fx_4h` score `0.3245` n `101` status `ready` deltaP `9.8602` edge `0.0249` maxDD `-0.421`
- `market_context_high->index_4h` score `0.2893` n `58` status `ready` deltaP `14.1716` edge `0.0063` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.2543` n `58` status `ready` deltaP `5.3996` edge `0.016` maxDD `-0.1314`
- `news_risk_high->fx_1h` score `-0.1777` n `101` status `ready` deltaP `3.4416` edge `0.0066` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.2598` n `101` status `ready` deltaP `1.7712` edge `0.0071` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.366` n `58` status `ready` deltaP `-2.2403` edge `0.0563` maxDD `-2.7494`
- `market_context_high->fx_4h` score `-0.425` n `58` status `ready` deltaP `1.6663` edge `-0.0032` maxDD `-0.6588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
