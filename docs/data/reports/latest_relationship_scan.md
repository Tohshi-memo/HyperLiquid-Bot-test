# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T18:07:36.795623+00:00`
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

- `market_context_high->unknown_4h` score `73.6565` n `88` status `ready` deltaP `9.0493` edge `6.1225` maxDD `-0.9161`
- `market_context_high->equity_24h` score `26.5729` n `88` status `ready` deltaP `23.7531` edge `2.2952` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.1607` n `53` status `ready` deltaP `33.9536` edge `0.8159` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.1729` n `88` status `ready` deltaP `37.6262` edge `1.3064` maxDD `-33.4213`
- `market_context_high->index_24h` score `4.8748` n `88` status `ready` deltaP `23.8636` edge `0.2934` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.4089` n `88` status `ready` deltaP `31.2026` edge `0.2147` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `3.891` n `53` status `ready` deltaP `38.6218` edge `0.1044` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.3919` n `53` status `ready` deltaP `17.7155` edge `0.2358` maxDD `-3.6997`
- `news_risk_high->crypto_major_4h` score `3.3867` n `53` status `ready` deltaP `18.7615` edge `0.3059` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `2.5862` n `53` status `ready` deltaP `23.815` edge `0.0821` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.249` n `53` status `ready` deltaP `21.051` edge `0.0907` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.9234` n `53` status `ready` deltaP `23.3448` edge `0.0301` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.5989` n `53` status `ready` deltaP `21.7729` edge `0.2237` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3006` n `53` status `ready` deltaP `17.0263` edge `0.025` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.6451` n `53` status `ready` deltaP `18.1928` edge `0.0666` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.6291` n `53` status `ready` deltaP `16.9952` edge `0.0653` maxDD `-6.1688`
- `market_context_high->metal_1h` score `-0.0789` n `88` status `ready` deltaP `6.1922` edge `0.0198` maxDD `-1.4122`
- `news_risk_high->commodity_1h` score `-0.3446` n `53` status `ready` deltaP `-3.3979` edge `0.0274` maxDD `-0.3438`
- `market_context_high->fx_24h` score `-0.4861` n `88` status `ready` deltaP `14.4097` edge `0.0234` maxDD `-3.4642`
- `market_context_high->commodity_1h` score `-0.5617` n `88` status `ready` deltaP `1.3405` edge `-0.0127` maxDD `-1.7935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
