# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T20:22:35.229411+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9717`

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

- `market_context_high->unknown_1h` score `84.8251` n `47` status `ready` deltaP `10.116` edge `7.0084` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `45.1625` n `47` status `ready` deltaP `30.4226` edge `3.6` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.0316` n `47` status `ready` deltaP `24.782` edge `2.3754` maxDD `-2.7051`
- `market_context_high->equity_24h` score `24.9803` n `47` status `ready` deltaP `31.4642` edge `1.9075` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `8.7318` n `111` status `ready` deltaP `-4.5476` edge `0.7824` maxDD `-0.9543`
- `market_context_high->index_24h` score `7.8684` n `47` status `ready` deltaP `35.1101` edge `0.4346` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.0116` n `47` status `ready` deltaP `34.1903` edge `0.1302` maxDD `-0.2401`
- `news_risk_high->crypto_alt_1h` score `3.5708` n `111` status `ready` deltaP `17.4449` edge `0.2303` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.9145` n `47` status `ready` deltaP `33.4166` edge `0.0355` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.7462` n `111` status `ready` deltaP `17.8886` edge `0.1531` maxDD `-1.8141`
- `news_risk_high->crypto_major_4h` score `2.6824` n `105` status `ready` deltaP `17.2329` edge `0.3218` maxDD `-13.719`
- `news_risk_high->crypto_alt_4h` score `2.606` n `105` status `ready` deltaP `8.7747` edge `0.4038` maxDD `-15.9436`
- `market_context_high->equity_4h` score `2.3697` n `47` status `ready` deltaP `16.992` edge `0.126` maxDD `-1.3444`
- `news_risk_high->commodity_24h` score `2.2546` n `81` status `ready` deltaP `23.206` edge `0.093` maxDD `-1.7857`
- `news_risk_high->metal_1h` score `1.6593` n `111` status `ready` deltaP `21.0134` edge `0.0267` maxDD `-0.6142`
- `news_risk_high->fx_4h` score `1.6297` n `105` status `ready` deltaP `23.6411` edge `0.0418` maxDD `-0.421`
- `news_risk_high->crypto_major_24h` score `1.521` n `81` status `ready` deltaP `-3.9351` edge `1.1255` maxDD `-63.6743`
- `market_context_high->index_1h` score `0.999` n `47` status `ready` deltaP `15.0592` edge `0.0107` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9546` n `47` status `ready` deltaP `11.7658` edge `0.0414` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.762` n `81` status `ready` deltaP `22.6852` edge `0.0913` maxDD `-7.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
