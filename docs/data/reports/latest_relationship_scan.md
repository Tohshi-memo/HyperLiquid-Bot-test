# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T22:07:32.042365+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9076`

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

- `news_risk_high->unknown_4h` score `467.8835` n `71` status `ready` deltaP `-12.3218` edge `39.1494` maxDD `-4.1571`
- `risk_on_high->commodity_24h` score `9.2272` n `52` status `ready` deltaP `50.0` edge `0.4356` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.2272` n `52` status `ready` deltaP `50.0` edge `0.4356` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.0766` n `58` status `ready` deltaP `26.5445` edge `0.634` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.9281` n `149` status `ready` deltaP `43.2886` edge `0.4246` maxDD `-0.8682`
- `news_risk_high->index_24h` score `4.7377` n `58` status `ready` deltaP `32.597` edge `0.1951` maxDD `-0.075`
- `news_risk_high->equity_24h` score `3.9715` n `58` status `ready` deltaP `20.067` edge `0.5528` maxDD `-6.5262`
- `news_risk_high->crypto_major_24h` score `3.818` n `58` status `ready` deltaP `12.913` edge `0.6029` maxDD `-13.2931`
- `risk_on_high->commodity_4h` score `3.0861` n `52` status `ready` deltaP `33.6069` edge `0.0681` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0861` n `52` status `ready` deltaP `33.6069` edge `0.0681` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.9858` n `149` status `ready` deltaP `30.1092` edge `0.0899` maxDD `-0.345`
- `news_risk_high->metal_24h` score `2.6548` n `58` status `ready` deltaP `19.5223` edge `0.1365` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `1.8468` n `52` status `ready` deltaP `26.3755` edge `-0.0177` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.8468` n `52` status `ready` deltaP `26.3755` edge `-0.0177` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.712` n `149` status `ready` deltaP `23.6006` edge `0.0069` maxDD `-0.0593`
- `news_risk_high->index_4h` score `1.6463` n `71` status `ready` deltaP `22.8122` edge `0.0317` maxDD `-0.3938`
- `market_context_high->commodity_1h` score `1.2979` n `149` status `ready` deltaP `17.7079` edge `0.0278` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.6746` n `52` status `ready` deltaP `10.79` edge `0.0195` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6746` n `52` status `ready` deltaP `10.79` edge `0.0195` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.223` n `149` status `ready` deltaP `10.6482` edge `0.0052` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
