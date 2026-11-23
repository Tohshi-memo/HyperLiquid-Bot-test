# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T13:07:34.129756+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4458`

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

- `market_context_high->unknown_1h` score `25478.7344` n `56` status `ready` deltaP `-0.5347` edge `2123.2476` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `17228.4068` n `56` status `ready` deltaP `4.3554` edge `1435.6854` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1296.181` n `31` status `ready` deltaP `3.728` edge `108.0078` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1097.6806` n `31` status `ready` deltaP `4.701` edge `91.4477` maxDD `-0.119`
- `news_risk_high->equity_24h` score `45.0621` n `31` status `ready` deltaP `49.8264` edge `3.423` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `37.0005` n `31` status `ready` deltaP `48.6111` edge `2.7593` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.632` n `31` status `ready` deltaP `48.7847` edge `2.3941` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.3724` n `31` status `ready` deltaP `50.4369` edge `0.8056` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.3246` n `31` status `ready` deltaP `32.9564` edge `0.6889` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.1752` n `31` status `ready` deltaP `21.7299` edge `0.7901` maxDD `-5.2957`
- `news_risk_high->index_24h` score `7.0529` n `31` status `ready` deltaP `47.9167` edge `0.2683` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.2626` n `31` status `ready` deltaP `52.9962` edge `0.1814` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.1889` n `31` status `ready` deltaP `11.2903` edge `0.8599` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.7111` n `31` status `ready` deltaP `18.7898` edge `0.2027` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.2913` n `31` status `ready` deltaP `34.6332` edge `0.0694` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6639` n `31` status `ready` deltaP `31.244` edge `0.0222` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3387` n `31` status `ready` deltaP `8.9627` edge `0.2862` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9263` n `31` status `ready` deltaP `7.4657` edge `0.2329` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5423` n `31` status `ready` deltaP `29.2833` edge `0.0304` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4256` n `31` status `ready` deltaP `19.9793` edge `0.1053` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
