# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T22:42:22.679595+00:00`
- Price records: `672`
- Market context records: `6132`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `10.5332` n `30` status `ready` deltaP `39.1666` edge `0.6314` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.7867` n `30` status `ready` deltaP `68.9236` edge `0.1894` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3335` n `32` status `ready` deltaP `45.1982` edge `0.0644` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3787` n `32` status `ready` deltaP `28.5928` edge `0.0215` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.2386` n `32` status `ready` deltaP `13.5292` edge `0.1153` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6393` n `32` status `ready` deltaP `8.6265` edge `0.0706` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.4757` n `195` status `ready` deltaP `4.3598` edge `0.1023` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.1093` n `30` status `ready` deltaP `8.5416` edge `0.0162` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.284` n `195` status `ready` deltaP `1.2851` edge `-0.0004` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.5599` n `30` status `ready` deltaP `14.0973` edge `-0.1201` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6926` n `195` status `ready` deltaP `2.9323` edge `0.0104` maxDD `-3.4996`
- `market_context_high->unknown_4h` score `-0.7193` n `195` status `ready` deltaP `-2.6118` edge `0.2107` maxDD `-11.925`
- `market_context_high->commodity_1h` score `-0.7727` n `195` status `ready` deltaP `-2.2885` edge `-0.0045` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7941` n `32` status `ready` deltaP `-3.2934` edge `-0.0301` maxDD `-1.6464`
- `market_context_high->equity_1h` score `-0.7993` n `195` status `ready` deltaP `-0.5589` edge `0.0128` maxDD `-4.2573`
- `news_risk_high->crypto_major_24h` score `-0.8068` n `30` status `ready` deltaP `9.5139` edge `-0.0889` maxDD `-4.2368`
- `market_context_high->metal_1h` score `-0.856` n `195` status `ready` deltaP `2.0912` edge `-0.0054` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.9367` n `195` status `ready` deltaP `3.6105` edge `0.0311` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9593` n `195` status `ready` deltaP `4.3145` edge `0.025` maxDD `-9.807`
- `market_context_high->metal_24h` score `-1.0068` n `195` status `ready` deltaP `14.9947` edge `0.0278` maxDD `-11.8809`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
