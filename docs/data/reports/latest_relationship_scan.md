# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T11:22:32.733822+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9954`

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

- `market_context_high->unknown_4h` score `47.089` n `46` status `ready` deltaP `7.3171` edge `3.8753` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `32.0731` n `46` status `ready` deltaP `17.8744` edge `2.5692` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `17.0943` n `46` status `ready` deltaP `17.0139` edge `1.3111` maxDD `0.0`
- `market_context_high->equity_24h` score `16.5294` n `46` status `ready` deltaP `13.1869` edge `1.2996` maxDD `-0.1382`
- `market_context_high->index_24h` score `5.5776` n `46` status `ready` deltaP `20.1314` edge `0.3393` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.356` n `101` status `ready` deltaP `-7.4808` edge `1.0987` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.1175` n `101` status `ready` deltaP `37.7802` edge `0.2784` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.4393` n `101` status `ready` deltaP `12.2117` edge `0.2428` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.2438` n `101` status `ready` deltaP `13.8362` edge `0.1413` maxDD `-2.058`
- `market_context_high->index_4h` score `2.1145` n `46` status `ready` deltaP `24.536` edge `0.026` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `1.9704` n `101` status `ready` deltaP `15.7178` edge `0.1852` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.5604` n `101` status `ready` deltaP `15.4829` edge `0.0791` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.3849` n `46` status `ready` deltaP `9.206` edge `0.0847` maxDD `-0.4529`
- `news_risk_high->fx_4h` score `0.9797` n `101` status `ready` deltaP `16.4151` edge `0.0358` maxDD `-0.421`
- `market_context_high->equity_1h` score `0.9648` n `46` status `ready` deltaP `7.6608` edge `0.0536` maxDD `-0.2751`
- `market_context_high->crypto_alt_4h` score `0.8837` n `46` status `ready` deltaP `7.9069` edge `0.0804` maxDD `-2.7574`
- `market_context_high->index_1h` score `0.7106` n `46` status `ready` deltaP `10.9542` edge `0.0115` maxDD `-0.0249`
- `market_context_high->metal_24h` score `0.695` n `46` status `ready` deltaP `20.0106` edge `-0.0521` maxDD `-0.2042`
- `news_risk_high->crypto_alt_24h` score `0.6133` n `101` status `ready` deltaP `-6.7485` edge `0.5842` maxDD `-32.7147`
- `news_risk_high->metal_1h` score `0.5813` n `101` status `ready` deltaP `14.2986` edge `0.0133` maxDD `-0.8144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
