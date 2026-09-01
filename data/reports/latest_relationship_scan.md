# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T09:22:28.130597+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11486`

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

- `risk_on_high->unknown_4h` score `7.2497` n `107` status `ready` deltaP `20.5252` edge `0.5291` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.2497` n `107` status `ready` deltaP `20.5252` edge `0.5291` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.7963` n `151` status `ready` deltaP `16.8178` edge `0.4404` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.161` n `107` status `ready` deltaP `4.5694` edge `0.2073` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.161` n `107` status `ready` deltaP `4.5694` edge `0.2073` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `2.0303` n `151` status `ready` deltaP `3.9319` edge `0.206` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.4331` n `60` status `ready` deltaP `2.6847` edge `0.1362` maxDD `-1.1072`
- `risk_on_high->commodity_24h` score `0.7053` n `107` status `ready` deltaP `9.8212` edge `0.0921` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.7053` n `107` status `ready` deltaP `9.8212` edge `0.0921` maxDD `-0.5706`
- `news_risk_high->fx_4h` score `0.2049` n `60` status `ready` deltaP `11.25` edge `0.0014` maxDD `-0.7461`
- `news_risk_high->commodity_24h` score `0.1371` n `58` status `ready` deltaP `4.5198` edge `0.0033` maxDD `-0.4274`
- `market_context_high->commodity_24h` score `0.1093` n `151` status `ready` deltaP `9.1898` edge `0.0674` maxDD `-1.2314`
- `risk_on_high->index_1h` score `0.0597` n `107` status `ready` deltaP `7.4948` edge `0.0022` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0597` n `107` status `ready` deltaP `7.4948` edge `0.0022` maxDD `-0.5605`
- `news_risk_high->commodity_4h` score `0.009` n `60` status `ready` deltaP `3.4451` edge `0.0141` maxDD `-0.8733`
- `market_context_high->commodity_1h` score `-0.0313` n `151` status `ready` deltaP `7.5247` edge `0.0122` maxDD `-1.5315`
- `risk_on_high->metal_1h` score `-0.0482` n `107` status `ready` deltaP `9.8495` edge `-0.0006` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.0482` n `107` status `ready` deltaP `9.8495` edge `-0.0006` maxDD `-1.699`
- `risk_on_high->commodity_1h` score `-0.0937` n `107` status `ready` deltaP `4.4239` edge `0.0107` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.0937` n `107` status `ready` deltaP `4.4239` edge `0.0107` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
