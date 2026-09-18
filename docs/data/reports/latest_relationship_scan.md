# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T10:07:32.700988+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8380`

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

- `market_context_high->unknown_4h` score `39.5988` n `149` status `ready` deltaP `-0.311` edge `3.3253` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.4775` n `52` status `ready` deltaP `-7.5516` edge `1.196` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.4775` n `52` status `ready` deltaP `-7.5516` edge `1.196` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.8696` n `52` status `ready` deltaP `50.0` edge `0.4058` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8696` n `52` status `ready` deltaP `50.0` edge `0.4058` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5705` n `149` status `ready` deltaP `43.2886` edge `0.3948` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `2.9394` n `84` status `ready` deltaP `19.6356` edge `0.461` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.8487` n `52` status `ready` deltaP `32.8447` edge `0.0534` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8487` n `52` status `ready` deltaP `32.8447` edge `0.0534` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7484` n `149` status `ready` deltaP `29.347` edge `0.0752` maxDD `-0.345`
- `news_risk_high->equity_4h` score `1.2997` n `84` status `ready` deltaP `16.4271` edge `0.1408` maxDD `-3.3619`
- `market_context_high->commodity_1h` score `1.1361` n `149` status `ready` deltaP `16.3606` edge `0.0233` maxDD `-0.3491`
- `risk_on_high->fx_24h` score `0.9705` n `52` status `ready` deltaP `18.7366` edge `-0.0398` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.9705` n `52` status `ready` deltaP `18.7366` edge `-0.0398` maxDD `-0.0054`
- `market_context_high->fx_24h` score `0.8356` n `149` status `ready` deltaP `15.9617` edge `-0.0152` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.5128` n `52` status `ready` deltaP `9.4427` edge `0.015` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5128` n `52` status `ready` deltaP `9.4427` edge `0.015` maxDD `-0.1507`
- `news_risk_high->fx_4h` score `0.3146` n `84` status `ready` deltaP `9.0447` edge `0.0247` maxDD `-0.2398`
- `news_risk_high->equity_1h` score `0.2772` n `95` status `ready` deltaP `9.8408` edge `0.0221` maxDD `-1.8403`
- `market_context_high->fx_1h` score `-0.0597` n `149` status `ready` deltaP `2.7057` edge `0.0001` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
