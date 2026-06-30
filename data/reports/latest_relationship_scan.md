# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T01:37:26.493721+00:00`
- Price records: `672`
- Market context records: `5203`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5644`

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

- `market_context_high->unknown_24h` score `17.265` n `97` status `ready` deltaP `33.7235` edge `1.2329` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `14.8335` n `97` status `ready` deltaP `29.8791` edge `1.4031` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `10.8491` n `97` status `ready` deltaP `30.194` edge `1.0415` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.2887` n `155` status `ready` deltaP `19.1168` edge `0.4155` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.6331` n `155` status `ready` deltaP `13.8464` edge `0.4537` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.4718` n `155` status `ready` deltaP `14.0696` edge `0.5081` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.4237` n `155` status `ready` deltaP `8.5387` edge `0.2092` maxDD `-2.7986`
- `market_context_high->equity_4h` score `0.7324` n `155` status `ready` deltaP `8.1599` edge `0.1705` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.6284` n `155` status `ready` deltaP `4.803` edge `0.1165` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.6172` n `155` status `ready` deltaP `6.8524` edge `0.1303` maxDD `-6.9639`
- `market_context_high->fx_24h` score `0.5044` n `97` status `ready` deltaP `13.1049` edge `0.0442` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.1039` n `155` status `ready` deltaP `6.7172` edge `0.0604` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.066` n `155` status `ready` deltaP `4.8851` edge `0.0123` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0771` n `155` status `ready` deltaP `4.7102` edge `0.0179` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3001` n `155` status `ready` deltaP `1.0605` edge `-0.0003` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.5666` n `155` status `ready` deltaP `5.4485` edge `0.0282` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5836` n `155` status `ready` deltaP `3.4913` edge `0.0053` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.5884` n `155` status `ready` deltaP `0.875` edge `-0.0004` maxDD `-2.4692`
- `market_context_high->index_24h` score `-0.763` n `97` status `ready` deltaP `11.1719` edge `-0.0088` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.3605` n `155` status `ready` deltaP `-0.1023` edge `0.0266` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
