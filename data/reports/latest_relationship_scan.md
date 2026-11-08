# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T04:37:29.673086+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4443`

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

- `market_context_high->unknown_4h` score `121.1995` n `37` status `ready` deltaP `-6.0728` edge `10.1852` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.3374` n `37` status `ready` deltaP `36.2105` edge `0.0457` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.2628` n `37` status `ready` deltaP `10.5074` edge `0.2478` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.9281` n `37` status `ready` deltaP `25.2884` edge `0.0391` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.778` n `52` status `ready` deltaP `10.6303` edge `0.0994` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.9406` n `52` status `ready` deltaP `7.9033` edge `0.1418` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7364` n `37` status `ready` deltaP `9.3017` edge `0.0579` maxDD `-3.0172`
- `market_context_high->crypto_alt_1h` score `0.4717` n `37` status `ready` deltaP `11.0981` edge `0.068` maxDD `-3.1881`
- `market_context_high->fx_1h` score `0.4469` n `37` status `ready` deltaP `7.3718` edge `0.0152` maxDD `-0.1681`
- `news_risk_high->index_4h` score `0.2907` n `52` status `ready` deltaP `9.5919` edge `0.0211` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2721` n `37` status `ready` deltaP `1.6508` edge `0.0387` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.2469` n `52` status `ready` deltaP `6.851` edge `0.1528` maxDD `-6.6786`
- `market_context_high->commodity_1h` score `0.1452` n `37` status `ready` deltaP `9.4676` edge `0.0101` maxDD `-1.7019`
- `news_risk_high->fx_4h` score `0.0771` n `52` status `ready` deltaP `7.0005` edge `0.0071` maxDD `-0.1771`
- `market_context_high->commodity_4h` score `0.0715` n `37` status `ready` deltaP `4.5114` edge `0.0245` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.0022` n `37` status `ready` deltaP `2.3993` edge `0.0165` maxDD `-0.6226`
- `news_risk_high->index_1h` score `-0.0146` n `52` status `ready` deltaP `6.0686` edge `0.003` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.2379` n `52` status `ready` deltaP `-2.7983` edge `0.0431` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.327` n `52` status `ready` deltaP `-0.9442` edge `0.0029` maxDD `-0.0826`
- `market_context_high->equity_4h` score `-0.6827` n `37` status `ready` deltaP `22.4044` edge `0.0911` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
