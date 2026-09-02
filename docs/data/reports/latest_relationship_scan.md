# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T00:37:29.402930+00:00`
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

- `risk_on_high->unknown_4h` score `7.0587` n `107` status `ready` deltaP `19.4581` edge `0.5203` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.0587` n `107` status `ready` deltaP `19.4581` edge `0.5203` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.6053` n `151` status `ready` deltaP `15.7507` edge `0.4316` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `1.8061` n `107` status `ready` deltaP `3.0724` edge `0.1877` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.8061` n `107` status `ready` deltaP `3.0724` edge `0.1877` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.6753` n `151` status `ready` deltaP `2.4349` edge `0.1864` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.0958` n `59` status `ready` deltaP `0.5379` edge `0.1224` maxDD `-1.1072`
- `risk_on_high->equity_24h` score `0.6426` n `107` status `ready` deltaP `15.7159` edge `0.3652` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `0.6426` n `107` status `ready` deltaP `15.7159` edge `0.3652` maxDD `-19.9806`
- `news_risk_high->fx_4h` score `0.1391` n `59` status `ready` deltaP `10.4873` edge `0.001` maxDD `-0.7461`
- `risk_on_high->metal_1h` score `0.0967` n `107` status `ready` deltaP `12.095` edge `0.003` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0967` n `107` status `ready` deltaP `12.095` edge `0.003` maxDD `-1.699`
- `risk_on_high->index_1h` score `0.0551` n `107` status `ready` deltaP `7.3451` edge `0.0026` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0551` n `107` status `ready` deltaP `7.3451` edge `0.0026` maxDD `-0.5605`
- `risk_on_high->index_4h` score `-0.0109` n `107` status `ready` deltaP `18.9538` edge `0.0053` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `-0.0109` n `107` status `ready` deltaP `18.9538` edge `0.0053` maxDD `-3.6448`
- `risk_on_high->commodity_24h` score `-0.167` n `107` status `ready` deltaP `6.5226` edge `0.0414` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `-0.167` n `107` status `ready` deltaP `6.5226` edge `0.0414` maxDD `-0.5706`
- `risk_on_high->equity_1h` score `-0.1753` n `107` status `ready` deltaP `7.5676` edge `0.01` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.1753` n `107` status `ready` deltaP `7.5676` edge `0.01` maxDD `-2.3009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
