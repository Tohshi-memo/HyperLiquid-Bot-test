# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T04:37:32.127597+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8616`

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

- `market_context_high->unknown_4h` score `39.8944` n `149` status `ready` deltaP `-0.0061` edge `3.3479` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.7731` n `52` status `ready` deltaP `-7.2467` edge `1.2186` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.7731` n `52` status `ready` deltaP `-7.2467` edge `1.2186` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.9596` n `52` status `ready` deltaP `50.0` edge `0.4133` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.9596` n `52` status `ready` deltaP `50.0` edge `0.4133` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.6605` n `149` status `ready` deltaP `43.2886` edge `0.4023` maxDD `-0.8682`
- `news_risk_high->crypto_alt_24h` score `3.3075` n `32` status `ready` deltaP `23.0903` edge `0.2596` maxDD `-9.3661`
- `risk_on_high->commodity_4h` score `2.9473` n `52` status `ready` deltaP `32.9972` edge `0.0606` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9473` n `52` status `ready` deltaP `32.9972` edge `0.0606` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.847` n `149` status `ready` deltaP `29.4995` edge `0.0824` maxDD `-0.345`
- `news_risk_high->index_24h` score `2.2017` n `32` status `ready` deltaP `17.1875` edge `0.0865` maxDD `-0.075`
- `news_risk_high->crypto_alt_4h` score `1.5148` n `68` status `ready` deltaP `13.6837` edge `0.3286` maxDD `-13.05`
- `risk_on_high->fx_24h` score `1.4057` n `52` status `ready` deltaP `22.5561` edge `-0.029` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.4057` n `52` status `ready` deltaP `22.5561` edge `-0.029` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.2708` n `149` status `ready` deltaP `19.7812` edge `-0.0044` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.2451` n `149` status `ready` deltaP `17.2588` edge `0.0264` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.6219` n `52` status `ready` deltaP `10.3409` edge `0.0181` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6219` n `52` status `ready` deltaP `10.3409` edge `0.0181` maxDD `-0.1507`
- `news_risk_high->equity_4h` score `0.4365` n `68` status `ready` deltaP `9.7292` edge `0.0552` maxDD `-3.3619`
- `news_risk_high->equity_1h` score `0.1797` n `78` status `ready` deltaP `8.2067` edge `0.0205` maxDD `-1.8403`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
