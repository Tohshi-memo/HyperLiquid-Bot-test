# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T18:37:32.769186+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11764`

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

- `market_context_high->unknown_4h` score `73.6589` n `88` status `ready` deltaP `9.0493` edge `6.1227` maxDD `-0.9161`
- `market_context_high->equity_24h` score `25.9139` n `88` status `ready` deltaP `23.4059` edge `2.2426` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.0523` n `53` status `ready` deltaP `33.6487` edge `0.8089` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `7.9794` n `88` status `ready` deltaP `37.279` edge `1.2839` maxDD `-33.4213`
- `market_context_high->index_24h` score `4.775` n `88` status `ready` deltaP `23.5164` edge `0.2874` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.4137` n `88` status `ready` deltaP `31.2026` edge `0.2151` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `3.8994` n `53` status `ready` deltaP `38.6218` edge `0.1051` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.3799` n `53` status `ready` deltaP `17.7155` edge `0.2348` maxDD `-3.6997`
- `news_risk_high->crypto_major_4h` score `3.3035` n `53` status `ready` deltaP `18.4567` edge `0.301` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `2.6068` n `53` status `ready` deltaP `23.9675` edge `0.0828` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.2296` n `53` status `ready` deltaP `20.8985` edge `0.0901` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.9258` n `53` status `ready` deltaP `23.3448` edge `0.0303` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.569` n `53` status `ready` deltaP `21.468` edge `0.2219` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2994` n `53` status `ready` deltaP `17.0263` edge `0.0249` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.6584` n `53` status `ready` deltaP `18.3425` edge `0.0673` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.6393` n `53` status `ready` deltaP `16.9952` edge `0.0666` maxDD `-6.1688`
- `market_context_high->metal_1h` score `-0.0765` n `88` status `ready` deltaP `6.1922` edge `0.02` maxDD `-1.4122`
- `news_risk_high->commodity_1h` score `-0.323` n `53` status `ready` deltaP `-3.2482` edge `0.0282` maxDD `-0.3438`
- `market_context_high->fx_24h` score `-0.4487` n `88` status `ready` deltaP `14.7569` edge `0.0242` maxDD `-3.4642`
- `market_context_high->commodity_1h` score `-0.5477` n `88` status `ready` deltaP `1.4902` edge `-0.0119` maxDD `-1.7935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
