# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T14:16:32.706010+00:00`
- Price records: `672`
- Market context records: `1849`
- Flow alert records: `7224`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4500`

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

- `market_context_high->crypto_alt_4h` score `6.6144` n `197` status `ready` deltaP `21.6696` edge `0.5212` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.0378` n `197` status `ready` deltaP `25.1177` edge `0.4603` maxDD `-4.9684`
- `market_context_high->metal_24h` score `5.9073` n `178` status `ready` deltaP `23.7711` edge `0.5764` maxDD `-12.7414`
- `market_context_high->unknown_4h` score `4.4235` n `197` status `ready` deltaP `17.7626` edge `0.4526` maxDD `-9.8581`
- `market_context_high->index_24h` score `2.9734` n `178` status `ready` deltaP `15.4378` edge `0.2677` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `2.6715` n `178` status `ready` deltaP `14.56` edge `0.6576` maxDD `-35.8966`
- `market_context_high->equity_4h` score `2.3264` n `197` status `ready` deltaP `14.6574` edge `0.2056` maxDD `-5.0894`
- `market_context_high->equity_24h` score `0.9316` n `178` status `ready` deltaP `12.4161` edge `0.4847` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.5393` n `197` status `ready` deltaP `10.7016` edge `0.0825` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.2665` n `199` status `ready` deltaP `4.8484` edge `0.0885` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.2239` n `178` status `ready` deltaP `19.2065` edge `0.7492` maxDD `-62.3533`
- `market_context_high->crypto_alt_1h` score `0.0771` n `199` status `ready` deltaP `4.7092` edge `0.0864` maxDD `-4.9097`
- `market_context_high->fx_24h` score `0.0213` n `178` status `ready` deltaP `12.4766` edge `0.0235` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1383` n `199` status `ready` deltaP `4.5377` edge `0.0376` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.4209` n `199` status `ready` deltaP `3.7365` edge `0.0352` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.5655` n `199` status `ready` deltaP `5.8323` edge `0.0222` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.6441` n `197` status `ready` deltaP `12.2872` edge `0.1336` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.6637` n `199` status `ready` deltaP `-0.4551` edge `0.0109` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.722` n `199` status `ready` deltaP `-4.2503` edge `-0.001` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0306` n `197` status `ready` deltaP `-5.641` edge `-0.0057` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
