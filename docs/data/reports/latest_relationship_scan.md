# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T10:52:31.147826+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9175`

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

- `market_context_high->unknown_4h` score `32.7769` n `58` status `ready` deltaP `1.23` edge `2.7382` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `21.6872` n `101` status `ready` deltaP `9.3595` edge `2.4307` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `16.1432` n `101` status `ready` deltaP `9.7445` edge `1.7684` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.6983` n `101` status `ready` deltaP `17.0898` edge `0.3152` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.3691` n `101` status `ready` deltaP `19.9861` edge `0.2733` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.4896` n `101` status `ready` deltaP `15.1835` edge `0.1528` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.8746` n `101` status `ready` deltaP `17.1296` edge `0.0943` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.2526` n `101` status `ready` deltaP `23.8913` edge `0.1319` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7707` n `58` status `ready` deltaP `5.7093` edge `0.0515` maxDD `-0.36`
- `market_context_high->index_1h` score `0.6693` n `58` status `ready` deltaP `10.128` edge `0.0138` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.5717` n `101` status `ready` deltaP `14.2986` edge `0.0125` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.3977` n `58` status `ready` deltaP `9.3744` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3792` n `101` status `ready` deltaP `10.47` edge `0.0254` maxDD `-0.421`
- `market_context_high->metal_1h` score `0.2938` n `58` status `ready` deltaP `5.8487` edge `0.0163` maxDD `-0.1314`
- `news_risk_high->metal_4h` score `0.2847` n `101` status `ready` deltaP `14.6598` edge `0.0314` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.2664` n `58` status `ready` deltaP `13.8667` edge `0.0054` maxDD `-1.0949`
- `news_risk_high->fx_1h` score `-0.1513` n `101` status `ready` deltaP `3.741` edge `0.0068` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.3041` n `101` status `ready` deltaP `1.3221` edge `0.0064` maxDD `-0.9112`
- `market_context_high->fx_4h` score `-0.3894` n `58` status `ready` deltaP `2.2761` edge `-0.0027` maxDD `-0.6588`
- `market_context_high->crypto_major_1h` score `-0.4104` n `58` status `ready` deltaP `-2.6894` edge `0.0556` maxDD `-2.7494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
