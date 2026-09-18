# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T01:52:31.770061+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->unknown_4h` score `35.617` n `149` status `ready` deltaP `-0.4634` edge `2.9945` maxDD `-0.5326`
- `news_risk_high->unknown_4h` score `24.2525` n `68` status `ready` deltaP `-3.6316` edge `2.0661` maxDD `-0.3345`
- `risk_on_high->unknown_4h` score `9.4957` n `52` status `ready` deltaP `-7.704` edge `0.8652` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.4957` n `52` status `ready` deltaP `-7.704` edge `0.8652` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `9.0436` n `52` status `ready` deltaP `50.0` edge `0.4203` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.0436` n `52` status `ready` deltaP `50.0` edge `0.4203` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `7.9891` n `43` status `ready` deltaP `29.4856` edge `0.6071` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.7445` n `149` status `ready` deltaP `43.2886` edge `0.4093` maxDD `-0.8682`
- `news_risk_high->index_24h` score `3.654` n `43` status `ready` deltaP `25.9811` edge `0.1489` maxDD `-0.075`
- `news_risk_high->equity_24h` score `3.1722` n `43` status `ready` deltaP `6.2338` edge `0.4002` maxDD `-6.5262`
- `risk_on_high->commodity_4h` score `3.0257` n `52` status `ready` deltaP `33.3021` edge `0.0651` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0257` n `52` status `ready` deltaP `33.3021` edge `0.0651` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.9254` n `149` status `ready` deltaP `29.8044` edge `0.0869` maxDD `-0.345`
- `risk_on_high->fx_24h` score `1.6233` n `52` status `ready` deltaP `24.4658` edge `-0.0236` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.6233` n `52` status `ready` deltaP `24.4658` edge `-0.0236` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.4884` n `149` status `ready` deltaP `21.6909` edge `0.001` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.2296` n `149` status `ready` deltaP `17.1091` edge `0.0261` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.0084` n `43` status `ready` deltaP `6.892` edge `0.0835` maxDD `-0.6334`
- `news_risk_high->crypto_major_24h` score `1.007` n `43` status `ready` deltaP `0.8842` edge `0.3227` maxDD `-13.2931`
- `news_risk_high->equity_4h` score `0.8395` n `68` status `ready` deltaP `11.0474` edge `0.08` maxDD `-3.3619`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
