# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T14:07:27.070798+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11742`

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

- `market_context_high->unknown_4h` score `75.6582` n `88` status `ready` deltaP `8.1347` edge `6.2954` maxDD `-0.9161`
- `market_context_high->equity_24h` score `30.5691` n `88` status `ready` deltaP `26.5309` edge `2.6097` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.752` n `53` status `ready` deltaP `35.6304` edge `0.854` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `9.2446` n `88` status `ready` deltaP `38.8415` edge `1.4357` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.487` n `88` status `ready` deltaP `26.6414` edge `0.3259` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.2841` n `88` status `ready` deltaP `31.2026` edge `0.2043` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.6085` n `53` status `ready` deltaP `19.5237` edge `0.3193` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5634` n `53` status `ready` deltaP `18.0149` edge `0.2481` maxDD `-3.6997`
- `news_risk_high->metal_4h` score `3.5435` n `53` status `ready` deltaP `36.1827` edge `0.0917` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `3.0182` n `53` status `ready` deltaP `25.6443` edge `0.1059` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.3205` n `53` status `ready` deltaP `21.6607` edge `0.0926` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8765` n `53` status `ready` deltaP `23.4497` edge `0.2481` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.6814` n `53` status `ready` deltaP `20.9496` edge `0.0259` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3281` n `53` status `ready` deltaP `17.3257` edge `0.0253` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6119` n `53` status `ready` deltaP `17.4443` edge `0.0601` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6045` n `53` status `ready` deltaP `18.4922` edge `0.0594` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.2355` n `53` status `ready` deltaP `-3.0985` edge `0.0345` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.3209` n `88` status `ready` deltaP `3.797` edge `0.0156` maxDD `-1.4122`
- `market_context_high->crypto_major_24h` score `-0.4654` n `88` status `ready` deltaP `17.0455` edge `1.0101` maxDD `-80.6681`
- `market_context_high->commodity_1h` score `-0.4908` n `88` status `ready` deltaP `1.6399` edge `-0.0056` maxDD `-1.7935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
