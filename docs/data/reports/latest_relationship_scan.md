# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T23:07:11.053179+00:00`
- Price records: `672`
- Market context records: `805`
- Flow alert records: `2262`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1170`

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

- `market_context_high->crypto_major_24h` score `12.5693` n `149` status `ready` deltaP `29.9905` edge `0.8809` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.5009` n `149` status `ready` deltaP `7.1414` edge `0.4156` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.5702` n `33` status `ready` deltaP `10.1903` edge `0.2661` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.5702` n `33` status `ready` deltaP `10.1903` edge `0.2661` maxDD `-0.9217`
- `risk_on_high->index_4h` score `2.8605` n `33` status `ready` deltaP `17.6229` edge `0.1297` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.8605` n `33` status `ready` deltaP `17.6229` edge `0.1297` maxDD `-0.038`
- `risk_on_high->crypto_major_4h` score `2.7138` n `33` status `ready` deltaP `19.5076` edge `0.1333` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.7138` n `33` status `ready` deltaP `19.5076` edge `0.1333` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `2.6795` n `33` status `ready` deltaP `20.6347` edge `0.1062` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.6795` n `33` status `ready` deltaP `20.6347` edge `0.1062` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.1183` n `33` status `ready` deltaP `13.1102` edge `0.0288` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.1183` n `33` status `ready` deltaP `13.1102` edge `0.0288` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.8264` n `33` status `ready` deltaP `5.5155` edge `0.1523` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.8264` n `33` status `ready` deltaP `5.5155` edge `0.1523` maxDD `-1.3162`
- `risk_on_high->commodity_1h` score `0.3506` n `33` status `ready` deltaP `8.8868` edge `0.0233` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.3506` n `33` status `ready` deltaP `8.8868` edge `0.0233` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.2696` n `33` status `ready` deltaP `8.3969` edge `0.0021` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2696` n `33` status `ready` deltaP `8.3969` edge `0.0021` maxDD `-0.2147`
- `risk_on_high->crypto_major_1h` score `-0.1588` n `33` status `ready` deltaP `4.1327` edge `-0.0175` maxDD `-1.0995`
- `risk_on_and_context->crypto_major_1h` score `-0.1588` n `33` status `ready` deltaP `4.1327` edge `-0.0175` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
