# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T14:07:29.658795+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11060`

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

- `market_context_high->unknown_1h` score `65.563` n `47` status `ready` deltaP `8.0201` edge `5.4172` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.3929` n `47` status `ready` deltaP `30.9434` edge `4.0324` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.7668` n `47` status `ready` deltaP `24.782` edge `2.52` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2363` n `47` status `ready` deltaP `34.5892` edge `1.908` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.7585` n `47` status `ready` deltaP `34.9364` edge `0.4266` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.3219` n `47` status `ready` deltaP `36.7945` edge `0.1387` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `2.9963` n `57` status `ready` deltaP `26.6265` edge `0.107` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.5584` n `47` status `ready` deltaP `29.9105` edge `0.0292` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.132` n `47` status `ready` deltaP `15.0103` edge `0.1194` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `0.9638` n `47` status `ready` deltaP `9.688` edge `0.0825` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9019` n `47` status `ready` deltaP `11.167` edge `0.041` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.8852` n `47` status `ready` deltaP `13.8616` edge `0.0092` maxDD `-0.2275`
- `news_risk_high->crypto_alt_1h` score `0.8081` n `111` status `ready` deltaP `8.4305` edge `0.1022` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4602` n `47` status `ready` deltaP `9.9598` edge `0.0076` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.136` n `47` status `ready` deltaP `3.854` edge `0.0674` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.0157` n `47` status `ready` deltaP `3.4272` edge `0.0108` maxDD `-0.1976`
- `news_risk_high->index_1h` score `0.0097` n `111` status `ready` deltaP `3.7601` edge `0.006` maxDD `-0.3863`
- `news_risk_high->metal_1h` score `0.0016` n `111` status `ready` deltaP `8.5451` edge `0.0061` maxDD `-0.7016`
- `news_risk_high->equity_1h` score `-0.0689` n `111` status `ready` deltaP `1.9664` edge `0.0288` maxDD `-2.0595`
- `news_risk_high->crypto_major_1h` score `-0.0847` n `111` status `ready` deltaP `3.164` edge `0.0474` maxDD `-3.3776`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
