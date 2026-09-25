# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T15:23:08.867153+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11076`

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

- `market_context_high->unknown_1h` score `63.2663` n `47` status `ready` deltaP `7.4213` edge `5.2298` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.4145` n `47` status `ready` deltaP `30.9434` edge `4.0342` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.84` n `47` status `ready` deltaP `24.782` edge `2.5261` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2663` n `47` status `ready` deltaP `34.5892` edge `1.9105` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.7537` n `47` status `ready` deltaP `34.9364` edge `0.4262` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.3322` n `47` status `ready` deltaP `36.9681` edge `0.1384` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.0155` n `57` status `ready` deltaP `26.6265` edge `0.1086` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.6338` n `47` status `ready` deltaP `30.6727` edge `0.0304` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.3309` n `47` status `ready` deltaP `15.7725` edge `0.1309` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.1146` n `47` status `ready` deltaP `10.2977` edge `0.091` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9643` n `47` status `ready` deltaP `11.4664` edge `0.0442` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.8668` n `111` status `ready` deltaP `8.8796` edge `0.1041` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.8625` n `47` status `ready` deltaP `13.5622` edge `0.0093` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.4206` n `47` status `ready` deltaP `9.5107` edge `0.0073` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.1732` n `47` status `ready` deltaP `4.1534` edge `0.0685` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.032` n `47` status `ready` deltaP `3.7266` edge `0.0109` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.0267` n `111` status `ready` deltaP `8.8445` edge `0.0062` maxDD `-0.7016`
- `market_context_high->crypto_major_4h` score `0.0156` n `47` status `ready` deltaP `3.6228` edge `0.0676` maxDD `-5.2359`
- `news_risk_high->index_1h` score `-0.0051` n `111` status `ready` deltaP `3.4607` edge `0.0061` maxDD `-0.3863`
- `news_risk_high->equity_1h` score `-0.0284` n `111` status `ready` deltaP `2.2658` edge `0.032` maxDD `-2.0595`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
