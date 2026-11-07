# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T16:37:27.941400+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4182`

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

- `market_context_high->unknown_4h` score `143.9868` n `37` status `ready` deltaP `-8.5118` edge `12.1004` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.363` n `37` status `ready` deltaP `36.5153` edge `0.0458` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.1706` n `37` status `ready` deltaP `9.4595` edge `0.2471` maxDD `-2.3425`
- `market_context_high->index_4h` score `2.0001` n `37` status `ready` deltaP `26.2031` edge `0.039` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.5959` n `52` status `ready` deltaP `8.8942` edge `0.0958` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.7885` n `52` status `ready` deltaP `6.0741` edge `0.1345` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7639` n `37` status `ready` deltaP `9.6011` edge `0.0582` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.532` n `37` status `ready` deltaP `8.4197` edge `0.0153` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.495` n `37` status `ready` deltaP `11.5472` edge `0.068` maxDD `-3.1881`
- `news_risk_high->index_4h` score `0.3375` n `52` status `ready` deltaP `10.5066` edge `0.021` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2482` n `37` status `ready` deltaP `1.3514` edge `0.0387` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.1652` n `52` status `ready` deltaP `6.3302` edge `0.1458` maxDD `-6.6786`
- `market_context_high->commodity_1h` score `0.1257` n `37` status `ready` deltaP `9.1682` edge `0.0096` maxDD `-1.7019`
- `news_risk_high->fx_4h` score `0.0938` n `52` status `ready` deltaP `7.3053` edge `0.0072` maxDD `-0.1771`
- `market_context_high->commodity_4h` score `-0.0005` n `37` status `ready` deltaP `3.2919` edge `0.0234` maxDD `-1.633`
- `news_risk_high->index_1h` score `-0.0302` n `52` status `ready` deltaP `5.7692` edge `0.003` maxDD `-0.2931`
- `market_context_high->metal_1h` score `-0.0349` n `37` status `ready` deltaP `1.8005` edge `0.0163` maxDD `-0.6226`
- `news_risk_high->fx_1h` score `-0.2718` n `52` status `ready` deltaP `0.1037` edge `0.003` maxDD `-0.0826`
- `news_risk_high->equity_1h` score `-0.2979` n `52` status `ready` deltaP `-3.8462` edge `0.0424` maxDD `-1.396`
- `market_context_high->equity_4h` score `-0.8347` n `37` status `ready` deltaP `20.5752` edge `0.0838` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
