# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T21:52:49.856171+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7982`

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

- `market_context_high->unknown_4h` score `92.2047` n `153` status `ready` deltaP `1.0172` edge `7.7105` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `21.7453` n `153` status `ready` deltaP `1.4745` edge `1.8512` maxDD `-1.5807`
- `market_context_high->fx_1h` score `0.277` n `153` status `ready` deltaP `8.4145` edge `0.0028` maxDD `-0.1986`
- `market_context_high->metal_24h` score `0.2459` n `112` status `ready` deltaP `23.5887` edge `0.1369` maxDD `-7.0108`
- `market_context_high->fx_4h` score `0.1006` n `153` status `ready` deltaP `9.0198` edge `0.0081` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.0246` n `112` status `ready` deltaP `16.3051` edge `0.012` maxDD `-4.5747`
- `market_context_high->metal_1h` score `-0.1392` n `153` status `ready` deltaP `8.1807` edge `0.0068` maxDD `-1.6682`
- `market_context_high->fx_24h` score `-0.1943` n `112` status `ready` deltaP `15.9321` edge `0.0261` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.2582` n `153` status `ready` deltaP `2.3023` edge `0.0132` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.558` n `153` status `ready` deltaP `0.4618` edge `-0.0009` maxDD `-1.8971`
- `market_context_high->commodity_4h` score `-0.5618` n `153` status `ready` deltaP `4.9916` edge `0.0428` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.8296` n `153` status `ready` deltaP `4.8325` edge `0.0195` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9376` n `153` status `ready` deltaP `7.6648` edge `-0.0003` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.7816` n `153` status `ready` deltaP `1.6046` edge `-0.0115` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.9399` n `153` status `ready` deltaP `0.0235` edge `-0.0004` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.3521` n `153` status `ready` deltaP `-5.7747` edge `-0.0232` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.4473` n `112` status `ready` deltaP `-2.6182` edge `-0.067` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.4758` n `153` status `ready` deltaP `0.6087` edge `-0.0739` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.0883` n `112` status `ready` deltaP `-14.4776` edge `-0.1251` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.5515` n `112` status `ready` deltaP `-5.99` edge `-0.2567` maxDD `-35.4638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
