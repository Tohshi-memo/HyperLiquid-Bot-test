# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T14:52:30.864575+00:00`
- Price records: `672`
- Market context records: `5154`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5612`

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

- `market_context_high->unknown_24h` score `30.2962` n `63` status `ready` deltaP `34.4494` edge `2.314` maxDD `-0.8515`
- `market_context_high->unknown_4h` score `6.5006` n `131` status `ready` deltaP `19.7752` edge `0.5121` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `5.3458` n `142` status `ready` deltaP `10.6245` edge `0.4388` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `5.1489` n `131` status `ready` deltaP `15.7943` edge `0.4837` maxDD `-9.46`
- `market_context_high->crypto_alt_24h` score `4.9936` n `63` status `ready` deltaP `19.8909` edge `0.8463` maxDD `-23.4292`
- `market_context_high->crypto_major_24h` score `4.8069` n `63` status `ready` deltaP `18.0803` edge `0.8619` maxDD `-22.6266`
- `market_context_high->crypto_major_4h` score `4.1422` n `131` status `ready` deltaP `14.42` edge `0.4783` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `2.0057` n `63` status `ready` deltaP `20.2381` edge `0.1555` maxDD `-5.1955`
- `market_context_high->metal_24h` score `0.9769` n `63` status `ready` deltaP `0.9424` edge `0.2498` maxDD `-5.4668`
- `market_context_high->equity_4h` score `0.9112` n `131` status `ready` deltaP `10.3053` edge `0.1711` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `0.7795` n `142` status `ready` deltaP `7.6959` edge `0.1382` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.7595` n `142` status `ready` deltaP `5.2564` edge `0.1244` maxDD `-5.0257`
- `market_context_high->equity_1h` score `-0.0451` n `142` status `ready` deltaP `6.3212` edge `0.0486` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.0633` n `142` status `ready` deltaP `5.0455` edge `0.0155` maxDD `-1.9139`
- `market_context_high->index_1h` score `-0.1537` n `142` status `ready` deltaP `3.0552` edge `0.0103` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.2189` n `142` status `ready` deltaP `2.5175` edge `0.0004` maxDD `-0.6194`
- `market_context_high->fx_24h` score `-0.3842` n `63` status `ready` deltaP `7.2173` edge `0.0094` maxDD `-0.8294`
- `market_context_high->index_4h` score `-0.5263` n `131` status `ready` deltaP `5.4122` edge `0.0318` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5895` n `131` status `ready` deltaP `3.2873` edge `0.0059` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6323` n `142` status `ready` deltaP `0.0443` edge `-0.0005` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
