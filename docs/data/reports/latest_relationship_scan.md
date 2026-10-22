# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T08:22:28.200595+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8262`

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

- `risk_on_high->commodity_24h` score `0.659` n `37` status `ready` deltaP `17.2303` edge `0.0494` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.659` n `37` status `ready` deltaP `17.2303` edge `0.0494` maxDD `-1.7154`
- `risk_on_high->equity_1h` score `0.6124` n `37` status `ready` deltaP `16.3457` edge `0.0119` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6124` n `37` status `ready` deltaP `16.3457` edge `0.0119` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5792` n `37` status `ready` deltaP `14.3996` edge `0.0053` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5792` n `37` status `ready` deltaP `14.3996` edge `0.0053` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.3648` n `78` status `ready` deltaP `14.1811` edge `0.0598` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.062` n `37` status `ready` deltaP `4.9523` edge `0.0008` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.062` n `37` status `ready` deltaP `4.9523` edge `0.0008` maxDD `-0.0698`
- `market_context_high->index_1h` score `0.0535` n `78` status `ready` deltaP `6.2222` edge `0.0009` maxDD `-0.5082`
- `risk_on_high->index_4h` score `-0.2895` n `37` status `ready` deltaP `6.8392` edge `0.0018` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.2895` n `37` status `ready` deltaP `6.8392` edge `0.0018` maxDD `-0.7604`
- `risk_on_high->fx_4h` score `-0.3139` n `37` status `ready` deltaP `-1.6563` edge `-0.0028` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.3139` n `37` status `ready` deltaP `-1.6563` edge `-0.0028` maxDD `-0.1126`
- `market_context_high->commodity_4h` score `-0.4121` n `78` status `ready` deltaP `5.4057` edge `0.0143` maxDD `-2.9203`
- `market_context_high->commodity_1h` score `-0.4369` n `78` status `ready` deltaP `0.4683` edge `0.0074` maxDD `-0.9891`
- `market_context_high->metal_1h` score `-0.6456` n `78` status `ready` deltaP `-5.9804` edge `-0.0054` maxDD `-0.6669`
- `risk_on_high->metal_1h` score `-0.8321` n `37` status `ready` deltaP `-6.4655` edge `-0.0002` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.8321` n `37` status `ready` deltaP `-6.4655` edge `-0.0002` maxDD `-0.0831`
- `risk_on_high->commodity_1h` score `-0.8667` n `37` status `ready` deltaP `-3.4472` edge `-0.0216` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
