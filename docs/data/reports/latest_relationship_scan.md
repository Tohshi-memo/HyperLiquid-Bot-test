# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T17:52:33.042434+00:00`
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

- `market_context_high->unknown_4h` score `73.2747` n `88` status `ready` deltaP `8.8969` edge `6.0917` maxDD `-0.9161`
- `market_context_high->equity_24h` score `26.8928` n `88` status `ready` deltaP `23.9267` edge `2.3207` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.21` n `53` status `ready` deltaP `34.106` edge `0.819` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.2755` n `88` status `ready` deltaP `37.7999` edge `1.3184` maxDD `-33.4213`
- `market_context_high->index_24h` score `4.9223` n `88` status `ready` deltaP `24.0372` edge `0.2962` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.4041` n `88` status `ready` deltaP `31.2026` edge `0.2143` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `3.8704` n `53` status `ready` deltaP `38.4693` edge `0.1037` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.4229` n `53` status `ready` deltaP `18.914` edge `0.3079` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.4135` n `53` status `ready` deltaP `17.8652` edge `0.2366` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `2.5838` n `53` status `ready` deltaP `23.815` edge `0.0819` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.2659` n `53` status `ready` deltaP `21.2034` edge `0.0911` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.909` n `53` status `ready` deltaP `23.1951` edge `0.0299` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.6139` n `53` status `ready` deltaP `21.9253` edge `0.2246` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3125` n `53` status `ready` deltaP `17.176` edge `0.025` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.6443` n `53` status `ready` deltaP `18.1928` edge `0.0665` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.6252` n `53` status `ready` deltaP `16.9952` edge `0.0648` maxDD `-6.1688`
- `market_context_high->metal_1h` score `-0.0932` n `88` status `ready` deltaP `6.0425` edge `0.0196` maxDD `-1.4122`
- `news_risk_high->commodity_1h` score `-0.3638` n `53` status `ready` deltaP `-3.5476` edge `0.0268` maxDD `-0.3438`
- `market_context_high->fx_24h` score `-0.5059` n `88` status `ready` deltaP `14.2361` edge `0.0229` maxDD `-3.4642`
- `market_context_high->commodity_1h` score `-0.5742` n `88` status `ready` deltaP `1.1908` edge `-0.0133` maxDD `-1.7935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
