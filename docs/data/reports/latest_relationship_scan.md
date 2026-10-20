# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T19:22:32.790379+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8773`

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

- `risk_on_high->equity_1h` score `0.7567` n `37` status `ready` deltaP `16.4954` edge `0.0294` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.7567` n `37` status `ready` deltaP `16.4954` edge `0.0294` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.608` n `37` status `ready` deltaP `14.699` edge `0.007` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.608` n `37` status `ready` deltaP `14.699` edge `0.007` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.2851` n `37` status `ready` deltaP `15.7095` edge `0.0116` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2851` n `37` status `ready` deltaP `15.7095` edge `0.0116` maxDD `-1.7154`
- `market_context_high->index_1h` score `0.0824` n `78` status `ready` deltaP `6.5216` edge `0.0026` maxDD `-0.5082`
- `risk_on_high->fx_1h` score `0.023` n `37` status `ready` deltaP `4.2038` edge `0.0008` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.023` n `37` status `ready` deltaP `4.2038` edge `0.0008` maxDD `-0.0698`
- `market_context_high->commodity_24h` score `-0.0091` n `78` status `ready` deltaP `12.6603` edge `0.022` maxDD `-3.6055`
- `risk_on_high->index_4h` score `-0.0096` n `37` status `ready` deltaP `10.3453` edge `0.0143` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.0096` n `37` status `ready` deltaP `10.3453` edge `0.0143` maxDD `-0.7604`
- `risk_on_high->equity_4h` score `-0.1315` n `37` status `ready` deltaP `7.2264` edge `0.0604` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.1315` n `37` status `ready` deltaP `7.2264` edge `0.0604` maxDD `-4.0351`
- `risk_on_high->fx_4h` score `-0.1889` n `37` status `ready` deltaP `0.4779` edge `-0.001` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1889` n `37` status `ready` deltaP `0.4779` edge `-0.001` maxDD `-0.1126`
- `market_context_high->commodity_4h` score `-0.2003` n `78` status `ready` deltaP `8.7594` edge `0.0191` maxDD `-2.9203`
- `market_context_high->commodity_1h` score `-0.2212` n `78` status `ready` deltaP `4.2108` edge `0.0101` maxDD `-0.9891`
- `market_context_high->metal_1h` score `-0.6285` n `78` status `ready` deltaP `-5.8307` edge `-0.0042` maxDD `-0.6669`
- `risk_on_high->commodity_1h` score `-0.651` n `37` status `ready` deltaP `0.2953` edge `-0.0189` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
