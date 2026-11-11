# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T08:52:27.863743+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11722`

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

- `market_context_high->unknown_4h` score `81.3998` n `88` status `ready` deltaP `7.8298` edge `6.7759` maxDD `-0.9161`
- `market_context_high->equity_24h` score `33.3832` n `88` status `ready` deltaP `30.1767` edge `2.8199` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `13.1041` n `47` status `ready` deltaP `37.0816` edge `0.957` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.783` n `88` status `ready` deltaP `35.5429` edge `1.3985` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.9995` n `88` status `ready` deltaP `30.2872` edge `0.3443` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.1053` n `88` status `ready` deltaP `31.2026` edge `0.1894` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.9154` n `47` status `ready` deltaP `23.5859` edge `0.3178` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6081` n `52` status `ready` deltaP `17.8835` edge `0.2527` maxDD `-3.6997`
- `news_risk_high->metal_4h` score `3.5064` n `47` status `ready` deltaP `34.954` edge `0.0968` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `3.246` n `47` status `ready` deltaP `26.4368` edge `0.1196` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.0979` n `47` status `ready` deltaP `29.4726` edge `0.1053` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.3657` n `47` status `ready` deltaP `28.2985` edge `0.2785` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.5947` n `52` status `ready` deltaP `20.1059` edge `0.0243` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4099` n `52` status `ready` deltaP `18.3326` edge `0.0254` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7453` n `52` status `ready` deltaP `17.9525` edge `0.0476` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.5658` n `52` status `ready` deltaP `17.8028` edge `0.0518` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `-0.1863` n `52` status `ready` deltaP `-2.6946` edge `0.0359` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.3532` n `88` status `ready` deltaP `3.4976` edge `0.0149` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3817` n `88` status `ready` deltaP `2.9872` edge `-0.0006` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.7006` n `88` status `ready` deltaP `1.1225` edge `0.0133` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
