# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T00:22:25.844834+00:00`
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

- `risk_on_high->unknown_4h` score `7.0503` n `107` status `ready` deltaP `19.4581` edge `0.5196` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.0503` n `107` status `ready` deltaP `19.4581` edge `0.5196` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.5969` n `151` status `ready` deltaP `15.7507` edge `0.4309` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `1.8672` n `107` status `ready` deltaP `3.2221` edge `0.1918` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `1.8672` n `107` status `ready` deltaP `3.2221` edge `0.1918` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.7365` n `151` status `ready` deltaP `2.5846` edge `0.1905` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.1569` n `59` status `ready` deltaP `0.6876` edge `0.1265` maxDD `-1.1072`
- `risk_on_high->equity_24h` score `0.5555` n `107` status `ready` deltaP `15.5423` edge `0.3591` maxDD `-19.9806`
- `risk_on_and_context->equity_24h` score `0.5555` n `107` status `ready` deltaP `15.5423` edge `0.3591` maxDD `-19.9806`
- `news_risk_high->fx_4h` score `0.1257` n `59` status `ready` deltaP `10.3349` edge `0.0009` maxDD `-0.7461`
- `risk_on_high->metal_1h` score `0.0967` n `107` status `ready` deltaP `12.095` edge `0.003` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0967` n `107` status `ready` deltaP `12.095` edge `0.003` maxDD `-1.699`
- `risk_on_high->index_1h` score `0.0644` n `107` status `ready` deltaP `7.4948` edge `0.0028` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0644` n `107` status `ready` deltaP `7.4948` edge `0.0028` maxDD `-0.5605`
- `risk_on_high->index_4h` score `-0.0109` n `107` status `ready` deltaP `18.9538` edge `0.0053` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `-0.0109` n `107` status `ready` deltaP `18.9538` edge `0.0053` maxDD `-3.6448`
- `risk_on_high->commodity_24h` score `-0.1526` n `107` status `ready` deltaP `6.5226` edge `0.0426` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `-0.1526` n `107` status `ready` deltaP `6.5226` edge `0.0426` maxDD `-0.5706`
- `risk_on_high->equity_1h` score `-0.1613` n `107` status `ready` deltaP `7.7173` edge `0.0108` maxDD `-2.3009`
- `risk_on_and_context->equity_1h` score `-0.1613` n `107` status `ready` deltaP `7.7173` edge `0.0108` maxDD `-2.3009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
