# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T00:22:27.728353+00:00`
- Price records: `672`
- Market context records: `5197`
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

- `market_context_high->unknown_24h` score `18.5994` n `92` status `ready` deltaP `33.4994` edge `1.3456` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `14.549` n `92` status `ready` deltaP `28.8421` edge `1.3863` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `10.9632` n `92` status `ready` deltaP `29.3251` edge `1.0568` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.4263` n `155` status `ready` deltaP `19.7266` edge `0.4229` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.5537` n `155` status `ready` deltaP `13.694` edge `0.4481` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.4262` n `155` status `ready` deltaP `14.0696` edge `0.5043` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.5628` n `155` status `ready` deltaP `8.9878` edge `0.2178` maxDD `-2.7986`
- `market_context_high->equity_4h` score `0.8644` n `155` status `ready` deltaP `8.1599` edge `0.1815` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.5804` n `155` status `ready` deltaP `4.6533` edge `0.1135` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5752` n `155` status `ready` deltaP `6.8524` edge `0.1268` maxDD `-6.9639`
- `market_context_high->fx_24h` score `0.4039` n `92` status `ready` deltaP `12.6283` edge `0.039` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.1494` n `155` status `ready` deltaP `6.8669` edge `0.0632` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0493` n `155` status `ready` deltaP `5.0348` edge `0.0127` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0826` n `155` status `ready` deltaP `4.7102` edge `0.0172` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.258` n `155` status `ready` deltaP `1.809` edge `0.0001` maxDD `-0.6194`
- `market_context_high->fx_4h` score `-0.5369` n `155` status `ready` deltaP `4.2535` edge `0.0062` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.545` n `155` status `ready` deltaP `5.4485` edge `0.03` maxDD `-2.9391`
- `market_context_high->commodity_1h` score `-0.6055` n `155` status `ready` deltaP `0.5756` edge `-0.0006` maxDD `-2.4692`
- `market_context_high->index_24h` score `-0.8644` n `92` status `ready` deltaP `9.911` edge `-0.0134` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.3473` n `155` status `ready` deltaP `-0.1023` edge `0.0283` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
