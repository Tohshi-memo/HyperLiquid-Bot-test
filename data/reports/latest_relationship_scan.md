# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-21T10:21:57.672890+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9062`

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

- `risk_on_high->equity_1h` score `0.6997` n `37` status `ready` deltaP `16.5385` edge `0.0218` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6997` n `37` status `ready` deltaP `16.5385` edge `0.0218` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.6145` n `37` status `ready` deltaP `14.8991` edge `0.0065` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.6145` n `37` status `ready` deltaP `14.8991` edge `0.0065` maxDD `-0.1637`
- `market_context_high->index_1h` score `0.0889` n `78` status `ready` deltaP `6.7217` edge `0.0021` maxDD `-0.5082`
- `risk_on_high->fx_1h` score `0.0114` n `37` status `ready` deltaP `3.9796` edge `0.0008` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.0114` n `37` status `ready` deltaP `3.9796` edge `0.0008` maxDD `-0.0698`
- `risk_on_high->commodity_24h` score `-0.0822` n `37` status `ready` deltaP `12.3805` edge `-0.0133` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.0822` n `37` status `ready` deltaP `12.3805` edge `-0.0133` maxDD `-1.7154`
- `risk_on_high->index_4h` score `-0.1158` n `37` status `ready` deltaP `8.9043` edge `0.0103` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.1158` n `37` status `ready` deltaP `8.9043` edge `0.0103` maxDD `-0.7604`
- `risk_on_high->fx_4h` score `-0.2542` n `37` status `ready` deltaP `-0.7472` edge `-0.0012` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2542` n `37` status `ready` deltaP `-0.7472` edge `-0.0012` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.3363` n `78` status `ready` deltaP `2.1915` edge `0.0088` maxDD `-0.9891`
- `market_context_high->commodity_24h` score `-0.3764` n `78` status `ready` deltaP `9.3313` edge `-0.0029` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `-0.3991` n `78` status `ready` deltaP `6.0307` edge `0.0118` maxDD `-2.9203`
- `risk_on_high->equity_4h` score `-0.5789` n `37` status `ready` deltaP `5.4625` edge `0.0148` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.5789` n `37` status `ready` deltaP `5.4625` edge `0.0148` maxDD `-4.0351`
- `market_context_high->metal_1h` score `-0.6175` n `78` status `ready` deltaP `-5.7702` edge `-0.0032` maxDD `-0.6669`
- `risk_on_high->commodity_1h` score `-0.7661` n `37` status `ready` deltaP `-1.724` edge `-0.0202` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
