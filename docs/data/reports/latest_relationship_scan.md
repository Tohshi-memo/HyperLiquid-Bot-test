# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T15:07:39.334673+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10036`

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

- `market_context_high->unknown_1h` score `87.8863` n `47` status `ready` deltaP `10.116` edge `7.2635` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `42.8602` n `47` status `ready` deltaP `30.2489` edge `3.4093` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.7392` n `47` status `ready` deltaP `24.782` edge `2.2677` maxDD `-2.7051`
- `market_context_high->equity_24h` score `24.1086` n `47` status `ready` deltaP `27.992` edge `1.858` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8389` n `47` status `ready` deltaP `34.9364` edge `0.4333` maxDD `-0.3705`
- `news_risk_high->crypto_major_24h` score `5.8132` n `96` status `ready` deltaP `2.2569` edge `1.6345` maxDD `-63.6743`
- `news_risk_high->crypto_alt_24h` score `3.9363` n `96` status `ready` deltaP `-0.1736` edge `1.2071` maxDD `-49.7699`
- `market_context_high->metal_24h` score `3.5821` n `47` status `ready` deltaP `30.8917` edge `0.1164` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.0956` n `47` status `ready` deltaP `35.2458` edge `0.0384` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.899` n `117` status `ready` deltaP `13.5179` edge `0.2005` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.6455` n `47` status `ready` deltaP `17.7542` edge `0.1439` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.4249` n `117` status `ready` deltaP `16.0628` edge `0.1385` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.7122` n `109` status `ready` deltaP `24.7469` edge `0.0413` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2229` n `96` status `ready` deltaP `29.3402` edge `0.1243` maxDD `-1.7159`
- `news_risk_high->metal_24h` score `1.1637` n `96` status `ready` deltaP `25.1736` edge `0.1262` maxDD `-7.2536`
- `news_risk_high->commodity_24h` score `1.0144` n `96` status `ready` deltaP `15.7986` edge `0.0971` maxDD `-2.431`
- `market_context_high->index_1h` score `0.9787` n `47` status `ready` deltaP `14.7598` edge `0.011` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9163` n `47` status `ready` deltaP `11.0173` edge `0.0432` maxDD `-1.5564`
- `news_risk_high->crypto_major_4h` score `0.71` n `109` status `ready` deltaP `14.4118` edge `0.2081` maxDD `-13.719`
- `news_risk_high->metal_1h` score `0.4906` n `117` status `ready` deltaP `15.4307` edge `0.0177` maxDD `-0.6142`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
