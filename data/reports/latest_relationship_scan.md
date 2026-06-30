# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T02:52:29.438916+00:00`
- Price records: `672`
- Market context records: `5208`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5650`

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

- `market_context_high->unknown_24h` score `15.8927` n `102` status `ready` deltaP `33.9256` edge `1.1172` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `14.8247` n `102` status `ready` deltaP `30.7292` edge `1.3967` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `10.5126` n `102` status `ready` deltaP `30.8925` edge `1.0088` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.2513` n `155` status `ready` deltaP `18.9644` edge `0.4134` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.5791` n `155` status `ready` deltaP `13.8464` edge `0.4492` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.4298` n `155` status `ready` deltaP `14.0696` edge `0.5046` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.5677` n `155` status `ready` deltaP `8.8381` edge `0.2192` maxDD `-2.7986`
- `market_context_high->crypto_alt_1h` score `0.6476` n `155` status `ready` deltaP `4.9527` edge `0.1171` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.6292` n `155` status `ready` deltaP `6.8524` edge `0.1313` maxDD `-6.9639`
- `market_context_high->fx_24h` score `0.556` n `102` status `ready` deltaP `13.4498` edge `0.0462` maxDD `-0.8294`
- `market_context_high->equity_4h` score `0.5436` n `155` status `ready` deltaP `7.855` edge `0.1568` maxDD `-7.4425`
- `market_context_high->equity_1h` score `-0.0196` n `155` status `ready` deltaP `5.9687` edge `0.0551` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.1044` n `155` status `ready` deltaP `4.4108` edge `0.0164` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.1391` n `155` status `ready` deltaP `4.1366` edge `0.0112` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.276` n `155` status `ready` deltaP `1.5096` edge `-0.0002` maxDD `-0.6194`
- `market_context_high->fx_4h` score `-0.5923` n `155` status `ready` deltaP `3.3389` edge `0.0052` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.6172` n `155` status `ready` deltaP `5.296` edge `0.025` maxDD `-2.9391`
- `market_context_high->commodity_1h` score `-0.625` n `155` status `ready` deltaP `0.2762` edge `-0.0011` maxDD `-2.4692`
- `market_context_high->index_24h` score `-0.6521` n `102` status `ready` deltaP `12.2243` edge `-0.0016` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.3621` n `155` status `ready` deltaP `-0.1023` edge `0.0264` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
