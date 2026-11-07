# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T14:37:32.305648+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4117`

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

- `market_context_high->unknown_4h` score `189.487` n `34` status `ready` deltaP `-2.5108` edge `15.8354` maxDD `-0.5798`
- `market_context_high->fx_4h` score `3.4254` n `34` status `ready` deltaP `36.8005` edge `0.0491` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.0927` n `37` status `ready` deltaP `8.711` edge `0.2456` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.9041` n `34` status `ready` deltaP `24.8386` edge `0.0401` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `0.9947` n `56` status `ready` deltaP `3.2986` edge `0.083` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.9831` n `56` status `ready` deltaP `8.1664` edge `0.1455` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.668` n `37` status `ready` deltaP `9.0023` edge `0.0542` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.508` n `37` status `ready` deltaP `8.1203` edge `0.0153` maxDD `-0.1681`
- `news_risk_high->index_4h` score `0.485` n `56` status `ready` deltaP `13.2839` edge `0.0214` maxDD `-0.4888`
- `market_context_high->crypto_alt_1h` score `0.3789` n `37` status `ready` deltaP `10.4993` edge `0.0601` maxDD `-3.1881`
- `market_context_high->index_1h` score `0.2733` n `37` status `ready` deltaP `1.6508` edge `0.0388` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.263` n `56` status `ready` deltaP `8.2093` edge `0.1458` maxDD `-6.6786`
- `news_risk_high->index_1h` score `0.1551` n `56` status `ready` deltaP `9.228` edge `0.0037` maxDD `-0.2931`
- `market_context_high->commodity_1h` score `0.1522` n `37` status `ready` deltaP `9.6173` edge `0.01` maxDD `-1.7019`
- `news_risk_high->fx_4h` score `-0.0309` n `56` status `ready` deltaP `5.1829` edge `0.0057` maxDD `-0.2038`
- `market_context_high->commodity_4h` score `-0.0479` n `34` status `ready` deltaP `2.6363` edge `0.0217` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.091` n `37` status `ready` deltaP `0.7526` edge `0.0161` maxDD `-0.6226`
- `news_risk_high->equity_1h` score `-0.0955` n `56` status `ready` deltaP `-0.7485` edge `0.0477` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.1151` n `56` status `ready` deltaP `3.101` edge `0.0031` maxDD `-0.0826`
- `news_risk_high->metal_1h` score `-0.7375` n `56` status `ready` deltaP `-7.7417` edge `-0.0072` maxDD `-0.5256`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
