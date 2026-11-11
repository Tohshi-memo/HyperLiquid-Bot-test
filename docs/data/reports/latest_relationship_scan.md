# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T21:28:20.107186+00:00`
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

- `market_context_high->unknown_4h` score `93.0484` n `88` status `ready` deltaP `8.5383` edge `7.7419` maxDD `-0.9161`
- `market_context_high->equity_24h` score `23.1045` n `88` status `ready` deltaP `21.7088` edge `2.0198` maxDD `-16.7984`
- `market_context_high->unknown_24h` score `16.5504` n `88` status `ready` deltaP `4.9937` edge `1.36` maxDD `-0.4609`
- `news_risk_high->equity_4h` score `11.1092` n `53` status `ready` deltaP `34.1199` edge `0.8105` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `7.1988` n `88` status `ready` deltaP `35.4828` edge `1.1958` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.5344` n `88` status `ready` deltaP `32.0659` edge `0.2194` maxDD `-1.4245`
- `market_context_high->index_24h` score `4.321` n `88` status `ready` deltaP `21.8307` edge `0.2608` maxDD `-2.3671`
- `news_risk_high->metal_4h` score `4.0199` n `53` status `ready` deltaP `39.5281` edge `0.1091` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.4497` n `53` status `ready` deltaP `17.9428` edge `0.2391` maxDD `-3.6997`
- `news_risk_high->crypto_major_4h` score `3.3622` n `53` status `ready` deltaP `19.04` edge `0.302` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `2.7147` n `53` status `ready` deltaP `24.4452` edge `0.0886` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.2356` n `53` status `ready` deltaP `21.0644` edge `0.0895` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.001` n `53` status `ready` deltaP `24.1645` edge `0.0311` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.7685` n `53` status `ready` deltaP `22.8135` edge `0.2385` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2947` n `53` status `ready` deltaP `16.9529` edge `0.025` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6305` n `53` status `ready` deltaP `16.9162` edge `0.066` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6246` n `53` status `ready` deltaP `17.9626` edge `0.0655` maxDD `-7.0808`
- `market_context_high->metal_1h` score `-0.0013` n `88` status `ready` deltaP `7.0119` edge `0.0208` maxDD `-1.4122`
- `market_context_high->fx_24h` score `-0.2627` n `88` status `ready` deltaP `16.436` edge `0.0285` maxDD `-3.4642`
- `news_risk_high->commodity_1h` score `-0.295` n `53` status `ready` deltaP `-3.0177` edge `0.029` maxDD `-0.3438`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
