# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T07:22:39.724424+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5900`

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

- `news_risk_high->unknown_24h` score `5188.5933` n `60` status `ready` deltaP `31.8082` edge `432.2128` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.1513` n `48` status `ready` deltaP `60.4709` edge `1.1492` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `5.2449` n `48` status `ready` deltaP `35.1495` edge `0.3291` maxDD `-7.1082`
- `news_risk_high->equity_4h` score `4.5277` n `68` status `ready` deltaP `16.5261` edge `0.3435` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.589` n `68` status `ready` deltaP `15.6115` edge `0.0664` maxDD `-0.3783`
- `market_context_high->fx_4h` score `1.0199` n `48` status `ready` deltaP `21.2399` edge `0.023` maxDD `-1.3685`
- `news_risk_high->equity_1h` score `0.6635` n `68` status `ready` deltaP `10.0916` edge `0.0703` maxDD `-2.916`
- `market_context_high->commodity_4h` score `0.4074` n `48` status `ready` deltaP `8.3333` edge `0.0813` maxDD `-2.7703`
- `market_context_high->crypto_alt_4h` score `0.3106` n `48` status `ready` deltaP `5.2845` edge `0.1003` maxDD `-5.323`
- `news_risk_high->fx_4h` score `0.1272` n `68` status `ready` deltaP `12.2938` edge `0.0244` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.0993` n `68` status `ready` deltaP `5.165` edge `0.0259` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.0843` n `68` status `ready` deltaP `6.3315` edge `0.0368` maxDD `-3.1233`
- `market_context_high->fx_24h` score `-0.0347` n `48` status `ready` deltaP `7.5065` edge `0.0435` maxDD `-2.506`
- `news_risk_high->fx_1h` score `-0.035` n `68` status `ready` deltaP `3.4167` edge `0.005` maxDD `-0.2475`
- `market_context_high->fx_1h` score `-0.0625` n `48` status `ready` deltaP `6.1128` edge `0.0015` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.0863` n `68` status `ready` deltaP `2.1663` edge `0.0068` maxDD `-0.5845`
- `market_context_high->commodity_1h` score `-0.119` n `48` status `ready` deltaP `1.9461` edge `0.0217` maxDD `-1.3282`
- `news_risk_high->metal_1h` score `-0.1598` n `68` status `ready` deltaP `2.1663` edge `0.0054` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2662` n `68` status `ready` deltaP `1.6203` edge `0.0271` maxDD `-3.762`
- `news_risk_high->commodity_1h` score `-0.628` n `68` status `ready` deltaP `3.4167` edge `-0.0253` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
