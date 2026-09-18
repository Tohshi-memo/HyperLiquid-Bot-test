# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T15:22:33.668623+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8528`

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

- `market_context_high->unknown_4h` score `39.9622` n `149` status `ready` deltaP `-0.4634` edge `3.3566` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `14.4165` n `36` status `ready` deltaP `25.3472` edge `1.1703` maxDD `-9.3661`
- `risk_on_high->unknown_4h` score `13.8409` n `52` status `ready` deltaP `-7.704` edge `1.2273` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.8409` n `52` status `ready` deltaP `-7.704` edge `1.2273` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.6805` n `52` status `ready` deltaP `48.6111` edge `0.3993` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.6805` n `52` status `ready` deltaP `48.6111` edge `0.3993` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.3813` n `149` status `ready` deltaP `41.8997` edge `0.3883` maxDD `-0.8682`
- `news_risk_high->crypto_major_24h` score `4.4442` n `36` status `ready` deltaP `-8.8542` edge `0.8283` maxDD `-13.2931`
- `news_risk_high->crypto_alt_4h` score `3.187` n `95` status `ready` deltaP `21.1874` edge `0.4824` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.7581` n `52` status `ready` deltaP `32.3874` edge `0.0489` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7581` n `52` status `ready` deltaP `32.3874` edge `0.0489` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.6578` n `149` status `ready` deltaP `28.8897` edge `0.0707` maxDD `-0.345`
- `market_context_high->commodity_1h` score `1.0941` n `149` status `ready` deltaP `16.0612` edge `0.0218` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `0.7115` n `95` status `ready` deltaP `12.6861` edge `0.1008` maxDD `-4.1995`
- `risk_on_high->fx_24h` score `0.6542` n `52` status `ready` deltaP `16.1325` edge `-0.0488` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.6542` n `52` status `ready` deltaP `16.1325` edge `-0.0488` maxDD `-0.0054`
- `market_context_high->fx_24h` score `0.5193` n `149` status `ready` deltaP `13.3576` edge `-0.0242` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.4709` n `52` status `ready` deltaP `9.1433` edge `0.0135` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4709` n `52` status `ready` deltaP `9.1433` edge `0.0135` maxDD `-0.1507`
- `news_risk_high->equity_1h` score `0.3559` n `95` status `ready` deltaP `10.5893` edge `0.0272` maxDD `-1.8403`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
