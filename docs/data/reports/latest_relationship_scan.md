# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T02:52:29.189606+00:00`
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

- `risk_on_high->unknown_4h` score `7.7227` n `107` status `ready` deltaP `19.763` edge `0.5736` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.7227` n `107` status `ready` deltaP `19.763` edge `0.5736` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.6655` n `150` status `ready` deltaP `15.9187` edge `0.4355` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `1.5192` n `107` status `ready` deltaP `3.2221` edge `0.1628` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.5192` n `107` status `ready` deltaP `3.2221` edge `0.1628` maxDD `-1.9475`
- `risk_on_high->equity_24h` score `1.4816` n `107` status `ready` deltaP `17.2784` edge `0.4247` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `1.4816` n `107` status `ready` deltaP `17.2784` edge `0.4247` maxDD `-19.9806`
- `market_context_high->unknown_1h` score `1.3603` n `150` status `ready` deltaP `2.3374` edge `0.1608` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `0.8089` n `59` status `ready` deltaP `0.6876` edge `0.0975` maxDD `-1.1072`
- `news_risk_high->fx_4h` score `0.1695` n `59` status `ready` deltaP `10.7922` edge `0.0015` maxDD `-0.7461`
- `risk_on_high->metal_1h` score `0.1528` n `107` status `ready` deltaP `12.8435` edge `0.0052` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1528` n `107` status `ready` deltaP `12.8435` edge `0.0052` maxDD `-1.699`
- `risk_on_high->index_1h` score `0.0753` n `107` status `ready` deltaP `7.6445` edge `0.0032` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0753` n `107` status `ready` deltaP `7.6445` edge `0.0032` maxDD `-0.5605`
- `risk_on_high->index_4h` score `0.053` n `107` status `ready` deltaP `19.8684` edge `0.0074` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.053` n `107` status `ready` deltaP `19.8684` edge `0.0074` maxDD `-3.6448`
- `risk_on_high->equity_1h` score `-0.1613` n `107` status `ready` deltaP `7.5676` edge `0.0118` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.1613` n `107` status `ready` deltaP `7.5676` edge `0.0118` maxDD `-2.3009`
- `market_context_high->commodity_1h` score `-0.2027` n `150` status `ready` deltaP `6.2974` edge `0.0061` maxDD `-1.5315`
- `news_risk_high->index_1h` score `-0.216` n `59` status `ready` deltaP `2.243` edge `-0.0073` maxDD `-0.8275`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
