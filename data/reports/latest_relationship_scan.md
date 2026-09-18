# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T16:22:31.627361+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8384`

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

- `market_context_high->unknown_4h` score `39.8386` n `149` status `ready` deltaP `-0.4634` edge `3.3463` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `17.7236` n `37` status `ready` deltaP `27.9561` edge `1.4285` maxDD `-9.3661`
- `risk_on_high->unknown_4h` score `13.7173` n `52` status `ready` deltaP `-7.704` edge `1.217` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.7173` n `52` status `ready` deltaP `-7.704` edge `1.217` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.5961` n `52` status `ready` deltaP `47.9167` edge `0.3969` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5961` n `52` status `ready` deltaP `47.9167` edge `0.3969` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.297` n `149` status `ready` deltaP `41.2053` edge `0.3859` maxDD `-0.8682`
- `news_risk_high->crypto_major_24h` score `7.0697` n `37` status `ready` deltaP `-5.3445` edge `1.1235` maxDD `-11.8527`
- `news_risk_high->crypto_alt_4h` score `3.4882` n `94` status `ready` deltaP `21.4063` edge `0.489` maxDD `-10.7605`
- `risk_on_high->commodity_4h` score `2.7315` n `52` status `ready` deltaP `32.235` edge `0.0477` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7315` n `52` status `ready` deltaP `32.235` edge `0.0477` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.6312` n `149` status `ready` deltaP `28.7373` edge `0.0695` maxDD `-0.345`
- `news_risk_high->equity_4h` score `1.2192` n `94` status `ready` deltaP `13.0643` edge `0.1045` maxDD `-4.1995`
- `market_context_high->commodity_1h` score `1.1061` n `149` status `ready` deltaP `16.2109` edge `0.0218` maxDD `-0.3491`
- `risk_on_high->fx_24h` score `0.5794` n `52` status `ready` deltaP `15.438` edge `-0.0504` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.5794` n `52` status `ready` deltaP `15.438` edge `-0.0504` maxDD `-0.0054`
- `news_risk_high->crypto_major_4h` score `0.5381` n `94` status `ready` deltaP `13.3595` edge `0.2748` maxDD `-17.9234`
- `risk_on_high->commodity_1h` score `0.4828` n `52` status `ready` deltaP `9.293` edge `0.0135` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4828` n `52` status `ready` deltaP `9.293` edge `0.0135` maxDD `-0.1507`
- `market_context_high->fx_24h` score `0.4446` n `149` status `ready` deltaP `12.6631` edge `-0.0258` maxDD `-0.0593`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
