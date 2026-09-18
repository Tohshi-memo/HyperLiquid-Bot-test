# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T07:22:36.778994+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8284`

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

- `market_context_high->unknown_4h` score `39.8464` n `149` status `ready` deltaP `-0.0061` edge `3.3439` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.7251` n `52` status `ready` deltaP `-7.2467` edge `1.2146` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.7251` n `52` status `ready` deltaP `-7.2467` edge `1.2146` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.8888` n `52` status `ready` deltaP `50.0` edge `0.4074` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8888` n `52` status `ready` deltaP `50.0` edge `0.4074` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5897` n `149` status `ready` deltaP `43.2886` edge `0.3964` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.8775` n `52` status `ready` deltaP `32.8447` edge `0.0558` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8775` n `52` status `ready` deltaP `32.8447` edge `0.0558` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7772` n `149` status `ready` deltaP `29.347` edge `0.0776` maxDD `-0.345`
- `news_risk_high->crypto_alt_4h` score `2.7593` n `73` status `ready` deltaP `17.2673` edge `0.4537` maxDD `-12.8718`
- `market_context_high->commodity_1h` score `1.2224` n `149` status `ready` deltaP `17.1091` edge `0.0255` maxDD `-0.3491`
- `risk_on_high->fx_24h` score `1.1929` n `52` status `ready` deltaP `20.6463` edge `-0.034` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.1929` n `52` status `ready` deltaP `20.6463` edge `-0.034` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.058` n `149` status `ready` deltaP `17.8714` edge `-0.0094` maxDD `-0.0593`
- `news_risk_high->equity_4h` score `0.8312` n `73` status `ready` deltaP `12.2473` edge `0.1086` maxDD `-3.3619`
- `risk_on_high->commodity_1h` score `0.5991` n `52` status `ready` deltaP `10.1912` edge `0.0172` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5991` n `52` status `ready` deltaP `10.1912` edge `0.0172` maxDD `-0.1507`
- `news_risk_high->equity_1h` score `0.4186` n `85` status `ready` deltaP `11.7964` edge `0.0272` maxDD `-1.8403`
- `news_risk_high->fx_4h` score `0.1352` n `73` status `ready` deltaP `5.6987` edge `0.024` maxDD `-0.2398`
- `market_context_high->fx_1h` score `0.0112` n `149` status `ready` deltaP `3.9033` edge `0.0012` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
