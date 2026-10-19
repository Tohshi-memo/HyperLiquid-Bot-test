# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T00:37:28.959879+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8550`

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

- `market_context_high->commodity_24h` score `1.8898` n `93` status `ready` deltaP `15.9645` edge `0.1362` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `1.5808` n `93` status `ready` deltaP `14.2981` edge `0.4478` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `1.3183` n `60` status `ready` deltaP `15.6957` edge `0.085` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.3183` n `60` status `ready` deltaP `15.6957` edge `0.085` maxDD `-1.7154`
- `risk_on_high->crypto_major_4h` score `0.7312` n `60` status `ready` deltaP `11.7174` edge `0.2637` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.7312` n `60` status `ready` deltaP `11.7174` edge `0.2637` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.3791` n `93` status `ready` deltaP `3.6137` edge `0.1134` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.241` n `60` status `ready` deltaP `8.1232` edge `0.0023` maxDD `-0.5766`
- `risk_on_and_context->index_1h` score `0.241` n `60` status `ready` deltaP `8.1232` edge `0.0023` maxDD `-0.5766`
- `risk_on_high->fx_1h` score `-0.1376` n `60` status `ready` deltaP `2.7327` edge `-0.0007` maxDD `-0.1456`
- `risk_on_and_context->fx_1h` score `-0.1376` n `60` status `ready` deltaP `2.7327` edge `-0.0007` maxDD `-0.1456`
- `market_context_high->index_1h` score `-0.4449` n `93` status `ready` deltaP `2.6931` edge `-0.0022` maxDD `-1.1567`
- `market_context_high->fx_1h` score `-0.5279` n `93` status `ready` deltaP `-2.2135` edge `-0.0008` maxDD `-0.503`
- `market_context_high->crypto_alt_1h` score `-0.5352` n `93` status `ready` deltaP `-0.198` edge `0.0827` maxDD `-7.3329`
- `risk_on_high->fx_4h` score `-0.6242` n `60` status `ready` deltaP `-3.9144` edge `0.0016` maxDD `-0.2019`
- `risk_on_and_context->fx_4h` score `-0.6242` n `60` status `ready` deltaP `-3.9144` edge `0.0016` maxDD `-0.2019`
- `market_context_high->fx_4h` score `-0.636` n `93` status `ready` deltaP `-3.1617` edge `0.0026` maxDD `-0.7115`
- `market_context_high->metal_1h` score `-0.8041` n `93` status `ready` deltaP `-2.9473` edge `0.0035` maxDD `-0.9556`
- `risk_on_high->equity_1h` score `-0.8349` n `60` status `ready` deltaP `7.3274` edge `-0.0062` maxDD `-4.9779`
- `risk_on_and_context->equity_1h` score `-0.8349` n `60` status `ready` deltaP `7.3274` edge `-0.0062` maxDD `-4.9779`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
