# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T21:07:32.057763+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11578`

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

- `market_context_high->unknown_4h` score `93.0808` n `88` status `ready` deltaP `8.5383` edge `7.7446` maxDD `-0.9161`
- `market_context_high->equity_24h` score `23.3644` n `88` status `ready` deltaP `21.8818` edge `2.0403` maxDD `-16.7984`
- `market_context_high->unknown_24h` score `12.1056` n `88` status `ready` deltaP `4.9937` edge `0.9896` maxDD `-0.4609`
- `news_risk_high->equity_4h` score `11.0948` n `53` status `ready` deltaP `34.1199` edge `0.8093` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `7.2624` n `88` status `ready` deltaP `35.6558` edge `1.2028` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.5146` n `88` status `ready` deltaP `31.8929` edge `0.2189` maxDD `-1.4245`
- `market_context_high->index_24h` score `4.366` n `88` status `ready` deltaP `22.0037` edge `0.2634` maxDD `-2.3671`
- `news_risk_high->metal_4h` score `4.0163` n `53` status `ready` deltaP `39.5281` edge `0.1088` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.4427` n `53` status `ready` deltaP `17.871` edge `0.239` maxDD `-3.6997`
- `news_risk_high->crypto_major_4h` score `3.3308` n `53` status `ready` deltaP `18.888` edge `0.3004` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `2.7135` n `53` status `ready` deltaP `24.4452` edge `0.0885` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.2344` n `53` status `ready` deltaP `21.0644` edge `0.0894` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.9947` n `53` status `ready` deltaP `24.0862` edge `0.0311` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.7395` n `53` status `ready` deltaP `22.6615` edge `0.2358` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2876` n `53` status `ready` deltaP `16.8797` edge `0.0249` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6217` n `53` status `ready` deltaP `16.8375` edge `0.0654` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6181` n `53` status `ready` deltaP `17.8822` edge `0.0652` maxDD `-7.0808`
- `market_context_high->metal_1h` score `-0.0075` n `88` status `ready` deltaP `6.9336` edge `0.0208` maxDD `-1.4122`
- `market_context_high->fx_24h` score `-0.2814` n `88` status `ready` deltaP `16.263` edge `0.0281` maxDD `-3.4642`
- `news_risk_high->commodity_1h` score `-0.2885` n `53` status `ready` deltaP `-2.9372` edge `0.029` maxDD `-0.3438`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
