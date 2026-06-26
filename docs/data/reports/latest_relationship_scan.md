# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T13:52:33.298542+00:00`
- Price records: `672`
- Market context records: `4833`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7588`

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

- `market_context_high->unknown_1h` score `13.7439` n `109` status `ready` deltaP `11.038` edge `1.1135` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.1632` n `104` status `ready` deltaP `20.6965` edge `0.7389` maxDD `-4.0622`
- `market_context_high->unknown_24h` score `3.6243` n `97` status `ready` deltaP `18.6175` edge `0.239` maxDD `-2.2204`
- `market_context_high->index_4h` score `0.7068` n `104` status `ready` deltaP `9.4747` edge `0.0424` maxDD `-0.7334`
- `market_context_high->equity_4h` score `0.4589` n `104` status `ready` deltaP `11.2922` edge `0.1217` maxDD `-6.3852`
- `market_context_high->commodity_4h` score `0.2191` n `104` status `ready` deltaP `13.696` edge `0.054` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.2178` n `109` status `ready` deltaP `5.2683` edge `0.0312` maxDD `-1.1869`
- `market_context_high->equity_1h` score `-0.0733` n `109` status `ready` deltaP `3.8098` edge `0.0268` maxDD `-2.928`
- `market_context_high->fx_4h` score `-0.2902` n `104` status `ready` deltaP `4.456` edge `0.0037` maxDD `-0.9826`
- `market_context_high->index_1h` score `-0.5523` n `109` status `ready` deltaP `-0.5892` edge `0.0086` maxDD `-0.7054`
- `market_context_high->crypto_alt_4h` score `-1.0653` n `104` status `ready` deltaP `11.7964` edge `0.1232` maxDD `-23.7399`
- `market_context_high->fx_1h` score `-1.1168` n `109` status `ready` deltaP `-3.5873` edge `-0.0042` maxDD `-0.8626`
- `market_context_high->crypto_major_1h` score `-2.1618` n `109` status `ready` deltaP `2.8155` edge `-0.0384` maxDD `-17.9354`
- `market_context_high->crypto_alt_1h` score `-2.172` n `109` status `ready` deltaP `4.09` edge `-0.0159` maxDD `-12.7225`
- `market_context_high->fx_24h` score `-2.2071` n `97` status `ready` deltaP `-9.869` edge `-0.0171` maxDD `-2.749`
- `market_context_high->metal_1h` score `-2.2332` n `109` status `ready` deltaP `-0.7046` edge `-0.0713` maxDD `-13.4916`
- `market_context_high->commodity_24h` score `-2.7392` n `97` status `ready` deltaP `15.7503` edge `0.0547` maxDD `-27.5371`
- `market_context_high->crypto_major_4h` score `-3.0358` n `104` status `ready` deltaP `8.3607` edge `0.0429` maxDD `-35.694`
- `market_context_high->index_24h` score `-4.1582` n `97` status `ready` deltaP `-4.3886` edge `-0.113` maxDD `-23.2678`
- `market_context_high->metal_4h` score `-4.6946` n `104` status `ready` deltaP `7.6688` edge `-0.1736` maxDD `-35.0184`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
