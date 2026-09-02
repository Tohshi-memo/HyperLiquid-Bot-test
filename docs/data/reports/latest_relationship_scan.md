# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T04:22:24.719229+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11475`

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

- `risk_on_high->unknown_4h` score `7.6281` n `107` status `ready` deltaP `19.9154` edge `0.5647` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.6281` n `107` status `ready` deltaP `19.9154` edge `0.5647` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.5709` n `150` status `ready` deltaP `16.0711` edge `0.4266` maxDD `-2.5597`
- `risk_on_high->equity_24h` score `2.0389` n `107` status `ready` deltaP `18.32` edge `0.4642` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `2.0389` n `107` status `ready` deltaP `18.32` edge `0.4642` maxDD `-19.9806`
- `risk_on_high->unknown_1h` score `1.4533` n `107` status `ready` deltaP `3.0724` edge `0.1583` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.4533` n `107` status `ready` deltaP `3.0724` edge `0.1583` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.2943` n `150` status `ready` deltaP `2.1877` edge `0.1563` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `0.743` n `59` status `ready` deltaP `0.5379` edge `0.093` maxDD `-1.1072`
- `news_risk_high->fx_4h` score `0.1987` n `59` status `ready` deltaP `11.0971` edge `0.0019` maxDD `-0.7461`
- `risk_on_high->metal_1h` score `0.1356` n `107` status `ready` deltaP `12.5441` edge `0.005` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1356` n `107` status `ready` deltaP `12.5441` edge `0.005` maxDD `-1.699`
- `risk_on_high->index_1h` score `0.1197` n `107` status `ready` deltaP `8.393` edge `0.0039` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.1197` n `107` status `ready` deltaP `8.393` edge `0.0039` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.083` n `107` status `ready` deltaP `20.3257` edge `0.0082` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.083` n `107` status `ready` deltaP `20.3257` edge `0.0082` maxDD `-3.6448`
- `risk_on_high->equity_1h` score `-0.1106` n `107` status `ready` deltaP `8.1664` edge `0.0143` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.1106` n `107` status `ready` deltaP `8.1664` edge `0.0143` maxDD `-2.3009`
- `market_context_high->equity_24h` score `-0.1426` n `150` status `ready` deltaP `15.1736` edge `0.3702` maxDD `-24.6594`
- `news_risk_high->index_1h` score `-0.1716` n `59` status `ready` deltaP `2.9915` edge `-0.0066` maxDD `-0.8275`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
