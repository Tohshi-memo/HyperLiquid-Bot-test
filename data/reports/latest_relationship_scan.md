# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T01:22:30.301925+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8299`

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

- `market_context_high->commodity_24h` score `1.9412` n `69` status `ready` deltaP `20.3125` edge `0.1115` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `1.045` n `39` status `ready` deltaP `18.4247` edge `0.0535` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `1.045` n `39` status `ready` deltaP `18.4247` edge `0.0535` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.657` n `39` status `ready` deltaP `15.281` edge `0.0094` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.657` n `39` status `ready` deltaP `15.281` edge `0.0094` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.1002` n `39` status `ready` deltaP `15.1843` edge `-0.0131` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1002` n `39` status `ready` deltaP `15.1843` edge `-0.0131` maxDD `-1.7154`
- `market_context_high->index_1h` score `-0.0299` n `87` status `ready` deltaP `4.3172` edge `0.0029` maxDD `-0.5082`
- `risk_on_high->index_4h` score `-0.0951` n `39` status `ready` deltaP `8.2669` edge `0.0172` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.0951` n `39` status `ready` deltaP `8.2669` edge `0.0172` maxDD `-0.7604`
- `risk_on_high->equity_4h` score `-0.1246` n `39` status `ready` deltaP `5.4252` edge `0.0733` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.1246` n `39` status `ready` deltaP `5.4252` edge `0.0733` maxDD `-4.0351`
- `market_context_high->metal_1h` score `-0.1982` n `87` status `ready` deltaP `0.8689` edge `0.0063` maxDD `-0.6669`
- `risk_on_high->fx_1h` score `-0.252` n `39` status `ready` deltaP `0.3839` edge `-0.0003` maxDD `-0.0985`
- `risk_on_and_context->fx_1h` score `-0.252` n `39` status `ready` deltaP `0.3839` edge `-0.0003` maxDD `-0.0985`
- `risk_on_high->metal_1h` score `-0.2763` n `39` status `ready` deltaP `-2.6678` edge `0.0084` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.2763` n `39` status `ready` deltaP `-2.6678` edge `0.0084` maxDD `-0.0831`
- `risk_on_high->fx_4h` score `-0.3835` n `39` status `ready` deltaP `-3.084` edge `-0.0022` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.3835` n `39` status `ready` deltaP `-3.084` edge `-0.0022` maxDD `-0.1126`
- `market_context_high->crypto_major_1h` score `-0.512` n `87` status `ready` deltaP `0.8311` edge `0.0305` maxDD `-4.8007`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
