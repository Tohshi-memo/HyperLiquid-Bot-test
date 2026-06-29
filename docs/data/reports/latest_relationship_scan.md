# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T16:37:29.600434+00:00`
- Price records: `672`
- Market context records: `5161`
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

- `market_context_high->unknown_24h` score `30.09` n `63` status `ready` deltaP `33.5814` edge `2.3026` maxDD `-0.8515`
- `market_context_high->unknown_4h` score `6.0843` n `137` status `ready` deltaP `19.9116` edge `0.4765` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.6266` n `137` status `ready` deltaP `14.2747` edge `0.4503` maxDD `-9.46`
- `market_context_high->crypto_alt_24h` score `4.5964` n `63` status `ready` deltaP `19.1965` edge `0.8` maxDD `-23.4292`
- `market_context_high->crypto_major_24h` score `4.3351` n `63` status `ready` deltaP `17.2123` edge `0.8072` maxDD `-22.6266`
- `market_context_high->unknown_1h` score `3.9129` n `149` status `ready` deltaP `10.248` edge `0.3219` maxDD `-2.7986`
- `market_context_high->crypto_major_4h` score `3.7898` n `137` status `ready` deltaP `13.1198` edge `0.4576` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `2.0357` n `63` status `ready` deltaP `20.2381` edge `0.158` maxDD `-5.1955`
- `market_context_high->metal_24h` score `0.9411` n `63` status `ready` deltaP `0.9424` edge `0.2452` maxDD `-5.4668`
- `market_context_high->crypto_major_1h` score `0.8488` n `149` status `ready` deltaP `8.0376` edge `0.1417` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.8297` n `149` status `ready` deltaP `5.565` edge `0.1282` maxDD `-5.0257`
- `market_context_high->equity_4h` score `0.4396` n `137` status `ready` deltaP `7.6642` edge `0.1494` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.3187` n `149` status `ready` deltaP `7.7231` edge `0.0716` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0214` n `149` status `ready` deltaP `5.1883` edge `0.014` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.1069` n `149` status `ready` deltaP `4.6769` edge `0.0143` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.1952` n `149` status `ready` deltaP `2.9428` edge `0.0006` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.4533` n `137` status `ready` deltaP `3.7831` edge `0.0284` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5104` n `137` status `ready` deltaP `4.5832` edge `0.0074` maxDD `-1.6047`
- `market_context_high->fx_24h` score `-0.5259` n `63` status `ready` deltaP `6.002` edge `0.0057` maxDD `-0.8294`
- `market_context_high->commodity_1h` score `-0.5317` n `149` status `ready` deltaP `1.6055` edge `0.002` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
