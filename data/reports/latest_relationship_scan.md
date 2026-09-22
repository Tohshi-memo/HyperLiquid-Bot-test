# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T11:37:26.527870+00:00`
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
- `market_context_high->crypto_major_24h` score `31.9884` n `46` status `ready` deltaP `17.7008` edge `2.5633` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `17.036` n `46` status `ready` deltaP `16.8403` edge `1.3074` maxDD `0.0`
- `market_context_high->equity_24h` score `16.4915` n `46` status `ready` deltaP `13.0133` edge `1.2976` maxDD `-0.1382`
- `market_context_high->index_24h` score `5.574` n `46` status `ready` deltaP `20.1314` edge `0.339` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.2713` n `101` status `ready` deltaP `-7.6544` edge `1.0928` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.1367` n `101` status `ready` deltaP `37.9538` edge `0.2797` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.4345` n `101` status `ready` deltaP `12.2117` edge `0.2424` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.2522` n `101` status `ready` deltaP `13.8362` edge `0.142` maxDD `-2.058`
- `market_context_high->index_4h` score `2.0987` n `46` status `ready` deltaP `24.3836` edge `0.0257` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `1.9307` n `101` status `ready` deltaP `15.5654` edge `0.1829` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.5628` n `101` status `ready` deltaP `15.4829` edge `0.0793` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.3512` n `46` status `ready` deltaP `9.0536` edge `0.0829` maxDD `-0.4529`
- `news_risk_high->fx_4h` score `0.9954` n `101` status `ready` deltaP `16.5675` edge `0.0361` maxDD `-0.421`
- `market_context_high->equity_1h` score `0.966` n `46` status `ready` deltaP `7.6608` edge `0.0537` maxDD `-0.2751`
- `market_context_high->crypto_alt_4h` score `0.8789` n `46` status `ready` deltaP `7.9069` edge `0.08` maxDD `-2.7574`
- `market_context_high->metal_24h` score `0.7257` n `46` status `ready` deltaP `20.1842` edge `-0.0507` maxDD `-0.2042`
- `market_context_high->index_1h` score `0.7226` n `46` status `ready` deltaP `11.1039` edge `0.0115` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5957` n `101` status `ready` deltaP `14.4483` edge `0.0135` maxDD `-0.8144`
- `news_risk_high->crypto_alt_24h` score `0.555` n `101` status `ready` deltaP `-6.9221` edge `0.5805` maxDD `-32.7147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
