# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T16:57:00.095643+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9354`

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

- `market_context_high->unknown_4h` score `46.5018` n `46` status `ready` deltaP `7.0122` edge `3.8284` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `30.1571` n `46` status `ready` deltaP `14.055` edge `2.435` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2716` n `46` status `ready` deltaP `12.3189` edge `1.2839` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `15.2505` n `46` status `ready` deltaP `13.5417` edge `1.1806` maxDD `0.0`
- `market_context_high->index_24h` score `5.5632` n `46` status `ready` deltaP `20.1314` edge `0.3381` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `3.0756` n `101` status `ready` deltaP `37.2593` edge `0.2765` maxDD `-3.4467`
- `news_risk_high->crypto_major_24h` score `2.44` n `101` status `ready` deltaP `-11.3002` edge `0.9645` maxDD `-46.1999`
- `news_risk_high->crypto_alt_1h` score `2.0771` n `101` status `ready` deltaP `12.938` edge `0.1334` maxDD `-2.058`
- `market_context_high->index_4h` score `1.8704` n `46` status `ready` deltaP `22.2494` edge `0.0209` maxDD `-0.0692`
- `news_risk_high->crypto_alt_4h` score `1.7792` n `101` status `ready` deltaP `10.23` edge `0.201` maxDD `-7.675`
- `news_risk_high->crypto_major_1h` score `1.3758` n `101` status `ready` deltaP `14.2853` edge `0.0717` maxDD `-2.8494`
- `market_context_high->metal_24h` score `1.1821` n `46` status `ready` deltaP `23.3092` edge `-0.0335` maxDD `-0.2042`
- `news_risk_high->crypto_major_4h` score `1.1475` n `101` status `ready` deltaP `13.1263` edge `0.1339` maxDD `-8.0625`
- `news_risk_high->fx_4h` score `1.133` n `101` status `ready` deltaP `18.0919` edge `0.0374` maxDD `-0.421`
- `market_context_high->equity_1h` score `0.8376` n `46` status `ready` deltaP `7.3614` edge `0.045` maxDD `-0.2751`
- `news_risk_high->metal_1h` score `0.6676` n `101` status `ready` deltaP `15.3465` edge `0.0135` maxDD `-0.8144`
- `market_context_high->equity_4h` score `0.6607` n `46` status `ready` deltaP `5.8524` edge `0.0467` maxDD `-0.4529`
- `market_context_high->index_1h` score `0.6579` n `46` status `ready` deltaP `10.5051` edge `0.0101` maxDD `-0.0249`
- `news_risk_high->metal_24h` score `0.5692` n `101` status `ready` deltaP `19.4994` edge `0.0274` maxDD `-2.4203`
- `news_risk_high->fx_24h` score `0.4253` n `101` status `ready` deltaP `18.9408` edge `0.0872` maxDD `-1.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
