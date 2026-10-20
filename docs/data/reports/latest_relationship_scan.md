# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T00:37:24.885378+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8202`

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

- `market_context_high->commodity_24h` score `2.3751` n `71` status `ready` deltaP `21.2514` edge `0.1414` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `1.0372` n `39` status `ready` deltaP `18.4247` edge `0.0525` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `1.0372` n `39` status `ready` deltaP `18.4247` edge `0.0525` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.6562` n `39` status `ready` deltaP `15.281` edge `0.0093` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.6562` n `39` status `ready` deltaP `15.281` edge `0.0093` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.051` n `39` status `ready` deltaP `15.1843` edge `-0.0172` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.051` n `39` status `ready` deltaP `15.1843` edge `-0.0172` maxDD `-1.7154`
- `risk_on_high->index_4h` score `-0.0974` n `39` status `ready` deltaP `8.2669` edge `0.0169` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.0974` n `39` status `ready` deltaP `8.2669` edge `0.0169` maxDD `-0.7604`
- `market_context_high->crypto_major_1h` score `-0.1565` n `90` status `ready` deltaP `1.8763` edge `0.0691` maxDD `-4.8007`
- `risk_on_high->equity_4h` score `-0.1747` n `39` status `ready` deltaP `5.1203` edge `0.0689` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.1747` n `39` status `ready` deltaP `5.1203` edge `0.0689` maxDD `-4.0351`
- `market_context_high->metal_1h` score `-0.24` n `90` status `ready` deltaP `0.2595` edge `0.005` maxDD `-0.6669`
- `risk_on_high->fx_1h` score `-0.2613` n `39` status `ready` deltaP `0.2342` edge `-0.0005` maxDD `-0.0985`
- `risk_on_and_context->fx_1h` score `-0.2613` n `39` status `ready` deltaP `0.2342` edge `-0.0005` maxDD `-0.0985`
- `market_context_high->index_1h` score `-0.2719` n `90` status `ready` deltaP `2.6314` edge `-0.0003` maxDD `-0.5251`
- `risk_on_high->metal_1h` score `-0.2864` n `39` status `ready` deltaP `-2.8175` edge `0.0081` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.2864` n `39` status `ready` deltaP `-2.8175` edge `0.0081` maxDD `-0.0831`
- `risk_on_high->fx_4h` score `-0.412` n `39` status `ready` deltaP `-3.5413` edge `-0.0028` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.412` n `39` status `ready` deltaP `-3.5413` edge `-0.0028` maxDD `-0.1126`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
