# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T00:52:26.676627+00:00`
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

- `risk_on_high->unknown_4h` score `7.0683` n `107` status `ready` deltaP `19.4581` edge `0.5211` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.0683` n `107` status `ready` deltaP `19.4581` edge `0.5211` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.6149` n `151` status `ready` deltaP `15.7507` edge `0.4324` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `1.7605` n `107` status `ready` deltaP `3.0724` edge `0.1839` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.7605` n `107` status `ready` deltaP `3.0724` edge `0.1839` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.6297` n `151` status `ready` deltaP `2.4349` edge `0.1826` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.0502` n `59` status `ready` deltaP `0.5379` edge `0.1186` maxDD `-1.1072`
- `risk_on_high->equity_24h` score `0.7369` n `107` status `ready` deltaP `15.8895` edge `0.3719` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `0.7369` n `107` status `ready` deltaP `15.8895` edge `0.3719` maxDD `-19.9806`
- `news_risk_high->fx_4h` score `0.1525` n `59` status `ready` deltaP `10.6397` edge `0.0011` maxDD `-0.7461`
- `risk_on_high->metal_1h` score `0.0967` n `107` status `ready` deltaP `12.095` edge `0.003` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0967` n `107` status `ready` deltaP `12.095` edge `0.003` maxDD `-1.699`
- `risk_on_high->index_1h` score `0.0465` n `107` status `ready` deltaP `7.1954` edge `0.0025` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0465` n `107` status `ready` deltaP `7.1954` edge `0.0025` maxDD `-0.5605`
- `risk_on_high->index_4h` score `-0.0094` n `107` status `ready` deltaP `18.9538` edge `0.0055` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `-0.0094` n `107` status `ready` deltaP `18.9538` edge `0.0055` maxDD `-3.6448`
- `risk_on_high->commodity_24h` score `-0.1814` n `107` status `ready` deltaP `6.5226` edge `0.0402` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `-0.1814` n `107` status `ready` deltaP `6.5226` edge `0.0402` maxDD `-0.5706`
- `risk_on_high->equity_1h` score `-0.1886` n `107` status `ready` deltaP `7.4179` edge `0.0093` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.1886` n `107` status `ready` deltaP `7.4179` edge `0.0093` maxDD `-2.3009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
