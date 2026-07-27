# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T09:37:29.438319+00:00`
- Price records: `672`
- Market context records: `8079`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->equity_24h` score `20.2016` n `85` status `ready` deltaP `36.6887` edge `1.5299` maxDD `-4.9489`
- `news_risk_high->equity_4h` score `8.8094` n `35` status `ready` deltaP `35.9016` edge `0.4994` maxDD `-0.037`
- `market_context_high->equity_4h` score `8.3938` n `87` status `ready` deltaP `32.4205` edge `0.5313` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.2664` n `85` status `ready` deltaP `35.8752` edge `0.4497` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.9327` n `35` status `ready` deltaP `28.2839` edge `0.3408` maxDD `-0.7975`
- `news_risk_high->equity_1h` score `3.3948` n `42` status `ready` deltaP `27.6447` edge `0.1302` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.2953` n `87` status `ready` deltaP `31.5881` edge `0.0828` maxDD `-0.5022`
- `market_context_high->index_24h` score `3.0017` n `85` status `ready` deltaP `19.0152` edge `0.1904` maxDD `-1.3621`
- `news_risk_high->unknown_1h` score `2.7715` n `42` status `ready` deltaP `2.994` edge `0.2387` maxDD `-0.8826`
- `news_risk_high->index_4h` score `2.6218` n `35` status `ready` deltaP `22.4912` edge `0.0876` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.363` n `87` status `ready` deltaP `21.7585` edge `0.1141` maxDD `-0.979`
- `market_context_high->equity_1h` score `2.3299` n `87` status `ready` deltaP `14.4263` edge `0.1413` maxDD `-2.1322`
- `market_context_high->fx_24h` score `2.3138` n `85` status `ready` deltaP `30.9104` edge `0.0571` maxDD `-0.6283`
- `news_risk_high->crypto_alt_4h` score `1.6113` n `35` status `ready` deltaP `17.6176` edge `0.1595` maxDD `-2.9634`
- `news_risk_high->fx_4h` score `1.5206` n `35` status `ready` deltaP `20.7839` edge `0.0188` maxDD `-0.1179`
- `news_risk_high->metal_4h` score `1.2448` n `35` status `ready` deltaP `12.169` edge `0.0694` maxDD `-0.7433`
- `market_context_high->index_1h` score `1.129` n `87` status `ready` deltaP `14.9718` edge `0.021` maxDD `-0.4716`
- `market_context_high->commodity_24h` score `0.9466` n `85` status `ready` deltaP `26.0373` edge `0.2111` maxDD `-14.3993`
- `market_context_high->metal_1h` score `0.7703` n `87` status `ready` deltaP `10.9247` edge `0.0292` maxDD `-0.6936`
- `market_context_high->crypto_alt_4h` score `0.6162` n `87` status `ready` deltaP `4.8097` edge `0.131` maxDD `-3.9374`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
