# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T12:52:26.493885+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11488`

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

- `market_context_high->unknown_4h` score `76.3086` n `88` status `ready` deltaP `8.1347` edge `6.3496` maxDD `-0.9161`
- `market_context_high->equity_24h` score `31.325` n `88` status `ready` deltaP `27.3989` edge `2.6669` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.9346` n `52` status `ready` deltaP `36.0225` edge `0.8666` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `9.1926` n `88` status `ready` deltaP `38.3207` edge `1.4325` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.6201` n `88` status `ready` deltaP `27.5094` edge `0.3312` maxDD `-2.3671`
- `market_context_high->metal_24h` score `4.2445` n `88` status `ready` deltaP `31.2026` edge `0.201` maxDD `-1.4245`
- `news_risk_high->equity_1h` score `3.5527` n `53` status `ready` deltaP `17.8652` edge `0.2482` maxDD `-3.6997`
- `news_risk_high->metal_4h` score `3.4902` n `52` status `ready` deltaP `35.4714` edge `0.092` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.2535` n `52` status `ready` deltaP `18.7617` edge `0.2948` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.1617` n `52` status `ready` deltaP `26.0436` edge `0.1152` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.3132` n `52` status `ready` deltaP `21.4939` edge `0.0931` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `1.6838` n `53` status `ready` deltaP `20.9496` edge `0.0261` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.655` n `52` status `ready` deltaP `22.7603` edge `0.2243` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.303` n `53` status `ready` deltaP `17.0263` edge `0.0252` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6688` n `53` status `ready` deltaP `18.1928` edge `0.0624` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6271` n `53` status `ready` deltaP `18.7916` edge `0.0603` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.1935` n `53` status `ready` deltaP `-2.7991` edge `0.036` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.3185` n `88` status `ready` deltaP `3.797` edge `0.0158` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4635` n `88` status `ready` deltaP `1.9393` edge `-0.0041` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.7219` n `88` status `ready` deltaP `2.1757` edge `-0.0093` maxDD `-2.4871`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
