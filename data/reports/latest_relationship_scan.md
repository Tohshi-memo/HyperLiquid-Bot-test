# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T03:22:26.819082+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11740`

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

- `market_context_high->unknown_4h` score `80.2462` n `88` status `ready` deltaP `7.525` edge `6.6818` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.5722` n `88` status `ready` deltaP `32.2601` edge `2.9051` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `10.7412` n `36` status `ready` deltaP `33.1809` edge `0.7861` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `7.5857` n `88` status `ready` deltaP `32.2443` edge `1.267` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1389` n `88` status `ready` deltaP `31.8497` edge `0.3455` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.7873` n `45` status `ready` deltaP `19.9135` edge `0.2541` maxDD `-3.6997`
- `news_risk_high->commodity_4h` score `3.1983` n `36` status `ready` deltaP `23.1707` edge `0.1374` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.1365` n `88` status `ready` deltaP `28.0776` edge `0.1295` maxDD `-1.4245`
- `news_risk_high->index_4h` score `2.3254` n `36` status `ready` deltaP `24.2717` edge `0.0756` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.0152` n `36` status `ready` deltaP `27.8285` edge `0.2367` maxDD `-10.1088`
- `news_risk_high->crypto_major_4h` score `1.6948` n `36` status `ready` deltaP `19.1904` edge `0.2381` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `1.5846` n `36` status `ready` deltaP `30.4032` edge `0.0381` maxDD `-1.0104`
- `news_risk_high->metal_1h` score `1.5229` n `45` status `ready` deltaP `19.7638` edge `0.0206` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3477` n `45` status `ready` deltaP `17.841` edge `0.0235` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.0188` n `45` status `ready` deltaP `21.8829` edge `0.0785` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.631` n `45` status `ready` deltaP `19.8104` edge `0.054` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.0991` n `45` status `ready` deltaP `-2.332` edge `0.0363` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.4336` n `88` status `ready` deltaP `3.1982` edge `0.0102` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4347` n `88` status `ready` deltaP `2.2387` edge `-0.0024` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.6878` n `88` status `ready` deltaP `1.5798` edge `0.0119` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
