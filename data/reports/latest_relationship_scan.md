# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T23:34:57.843583+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10145`

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

- `market_context_high->unknown_1h` score `84.1687` n `47` status `ready` deltaP `9.8166` edge `6.9557` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `46.7417` n `47` status `ready` deltaP `30.4226` edge `3.7316` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.868` n `47` status `ready` deltaP `24.782` edge `2.4451` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.6049` n `47` status `ready` deltaP `33.7212` edge `1.9445` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `8.6409` n `114` status `ready` deltaP `-2.5948` edge `0.7618` maxDD `-0.9543`
- `market_context_high->index_24h` score `8.097` n `47` status `ready` deltaP `37.367` edge `0.4386` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.3266` n `47` status `ready` deltaP `36.4473` edge `0.1414` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.4031` n `71` status `ready` deltaP `31.7121` edge `0.107` maxDD `-1.7857`
- `news_risk_high->crypto_alt_1h` score `3.0075` n `114` status `ready` deltaP `15.4297` edge `0.1987` maxDD `-1.7416`
- `market_context_high->index_4h` score `2.9061` n `47` status `ready` deltaP `33.4166` edge `0.0348` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.3745` n `47` status `ready` deltaP `16.992` edge `0.1264` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.072` n `114` status `ready` deltaP `15.343` edge `0.1263` maxDD `-2.4737`
- `news_risk_high->metal_1h` score `1.4425` n `114` status `ready` deltaP `18.7835` edge `0.0235` maxDD `-0.6142`
- `news_risk_high->fx_4h` score `1.0912` n `102` status `ready` deltaP `18.2747` edge `0.0327` maxDD `-0.421`
- `news_risk_high->crypto_major_4h` score `0.9711` n `102` status `ready` deltaP `12.1622` edge `0.213` maxDD `-13.719`
- `market_context_high->index_1h` score `0.9595` n `47` status `ready` deltaP `14.6101` edge `0.0104` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9079` n `47` status `ready` deltaP `11.3167` edge `0.0405` maxDD `-1.5564`
- `news_risk_high->crypto_alt_4h` score `0.8244` n `102` status `ready` deltaP `6.0198` edge `0.2737` maxDD `-15.9436`
- `news_risk_high->metal_24h` score `0.2907` n `71` status `ready` deltaP `19.7257` edge `0.0506` maxDD `-7.2536`
- `news_risk_high->fx_24h` score `0.264` n `71` status `ready` deltaP `16.8696` edge `0.0845` maxDD `-1.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
