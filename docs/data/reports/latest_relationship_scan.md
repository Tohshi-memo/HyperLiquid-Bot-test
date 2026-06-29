# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T23:22:29.752061+00:00`
- Price records: `672`
- Market context records: `5192`
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

- `market_context_high->unknown_24h` score `19.8604` n `88` status `ready` deltaP `33.3017` edge `1.452` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `13.9685` n `88` status `ready` deltaP `27.8567` edge `1.3445` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `10.7307` n `88` status `ready` deltaP `28.488` edge `1.043` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.4973` n `155` status `ready` deltaP `19.879` edge `0.4278` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.4245` n `155` status `ready` deltaP `13.0842` edge `0.4414` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.3392` n `155` status `ready` deltaP `13.6123` edge `0.5001` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.6132` n `155` status `ready` deltaP `9.4369` edge `0.219` maxDD `-2.7986`
- `market_context_high->equity_4h` score `1.045` n `155` status `ready` deltaP `8.6172` edge `0.1935` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.5301` n `155` status `ready` deltaP `4.3539` edge `0.1113` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5153` n `155` status `ready` deltaP `6.4033` edge `0.1248` maxDD `-6.9639`
- `market_context_high->fx_24h` score `0.3142` n `88` status `ready` deltaP `12.137` edge `0.0348` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.213` n `155` status `ready` deltaP `7.316` edge `0.0655` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0181` n `155` status `ready` deltaP `5.3342` edge `0.0133` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0818` n `155` status `ready` deltaP `4.7102` edge `0.0173` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2565` n `155` status `ready` deltaP `1.809` edge `0.0003` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.4808` n `155` status `ready` deltaP `5.9058` edge `0.0323` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5005` n `155` status `ready` deltaP `4.8633` edge `0.0068` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.5876` n `155` status `ready` deltaP `0.875` edge `-0.0003` maxDD `-2.4692`
- `market_context_high->index_24h` score `-0.9493` n `88` status `ready` deltaP `8.7279` edge `-0.0164` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.2994` n `155` status `ready` deltaP `0.2026` edge `0.0324` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
