# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T14:52:32.256531+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11760`

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

- `market_context_high->unknown_4h` score `73.6806` n `88` status `ready` deltaP `8.1347` edge `6.1306` maxDD `-0.9161`
- `market_context_high->equity_24h` score `30.1386` n `88` status `ready` deltaP `26.0101` edge `2.5773` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.7362` n `53` status `ready` deltaP `35.478` edge `0.8537` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `9.3076` n `88` status `ready` deltaP `39.3624` edge `1.4403` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.4106` n `88` status `ready` deltaP `26.1205` edge `0.323` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.3213` n `88` status `ready` deltaP `31.2026` edge `0.2074` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.7831` n `53` status `ready` deltaP `19.9811` edge `0.3308` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6594` n `53` status `ready` deltaP `18.464` edge `0.2531` maxDD `-3.6997`
- `news_risk_high->metal_4h` score `3.6124` n `53` status `ready` deltaP `36.6401` edge `0.0944` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `2.9048` n `53` status `ready` deltaP `25.187` edge `0.0995` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.3521` n `53` status `ready` deltaP `21.9656` edge `0.0932` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.924` n `53` status `ready` deltaP `23.4497` edge `0.2542` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.7317` n `53` status `ready` deltaP `21.3987` edge `0.0271` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3736` n `53` status `ready` deltaP `17.7748` edge `0.0261` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.6911` n `53` status `ready` deltaP `18.7916` edge `0.0685` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.6837` n `53` status `ready` deltaP `17.7437` edge `0.0673` maxDD `-6.1688`
- `market_context_high->metal_1h` score `-0.2705` n `88` status `ready` deltaP `4.2461` edge `0.0168` maxDD `-1.4122`
- `news_risk_high->commodity_1h` score `-0.2858` n `53` status `ready` deltaP `-3.5476` edge `0.0333` maxDD `-0.3438`
- `market_context_high->crypto_major_24h` score `-0.3157` n `88` status `ready` deltaP `17.5663` edge `1.0191` maxDD `-80.6681`
- `market_context_high->commodity_1h` score `-0.5235` n `88` status `ready` deltaP `1.1908` edge `-0.0068` maxDD `-1.7935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
