# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T16:07:27.575350+00:00`
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

- `market_context_high->unknown_4h` score `40.0258` n `149` status `ready` deltaP `-0.4634` edge `3.3619` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `16.9284` n `38` status `ready` deltaP `25.996` edge `1.3753` maxDD `-9.3661`
- `risk_on_high->unknown_4h` score `13.9045` n `52` status `ready` deltaP `-7.704` edge `1.2326` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.9045` n `52` status `ready` deltaP `-7.704` edge `1.2326` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.616` n `52` status `ready` deltaP `48.0903` edge `0.3974` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.616` n `52` status `ready` deltaP `48.0903` edge `0.3974` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.3169` n `149` status `ready` deltaP `41.3789` edge `0.3864` maxDD `-0.8682`
- `news_risk_high->crypto_major_24h` score `6.4116` n `38` status `ready` deltaP `-6.451` edge `1.0645` maxDD `-13.2931`
- `news_risk_high->crypto_alt_4h` score `3.036` n `95` status `ready` deltaP `20.7301` edge `0.4661` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.7315` n `52` status `ready` deltaP `32.235` edge `0.0477` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7315` n `52` status `ready` deltaP `32.235` edge `0.0477` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.6312` n `149` status `ready` deltaP `28.7373` edge `0.0695` maxDD `-0.345`
- `market_context_high->commodity_1h` score `1.0917` n `149` status `ready` deltaP `16.0612` edge `0.0216` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `0.6996` n `95` status `ready` deltaP `12.5337` edge `0.1003` maxDD `-4.1995`
- `risk_on_high->fx_24h` score `0.5969` n `52` status `ready` deltaP `15.6116` edge `-0.0501` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.5969` n `52` status `ready` deltaP `15.6116` edge `-0.0501` maxDD `-0.0054`
- `risk_on_high->commodity_1h` score `0.4685` n `52` status `ready` deltaP `9.1433` edge `0.0133` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4685` n `52` status `ready` deltaP `9.1433` edge `0.0133` maxDD `-0.1507`
- `market_context_high->fx_24h` score `0.462` n `149` status `ready` deltaP `12.8367` edge `-0.0255` maxDD `-0.0593`
- `news_risk_high->equity_1h` score `0.3676` n `95` status `ready` deltaP `10.739` edge `0.0277` maxDD `-1.8403`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
