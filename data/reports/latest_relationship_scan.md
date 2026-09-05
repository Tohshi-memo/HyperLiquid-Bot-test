# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T23:22:29.164394+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10807`

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

- `risk_on_high->unknown_4h` score `21.3228` n `133` status `ready` deltaP `-2.7061` edge `1.9955` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `21.3228` n `133` status `ready` deltaP `-2.7061` edge `1.9955` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.4842` n `228` status `ready` deltaP `1.8052` edge `0.9418` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `6.1943` n `37` status `ready` deltaP `25.1783` edge `0.3753` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.8971` n `37` status `ready` deltaP `20.1389` edge `0.1905` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.2973` n `37` status `ready` deltaP `16.4181` edge `0.2066` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3503` n `37` status `ready` deltaP `23.8464` edge `0.059` maxDD `-0.7692`
- `market_context_high->equity_24h` score `2.1804` n `155` status `ready` deltaP `14.4478` edge `0.471` maxDD `-18.8498`
- `news_risk_high->equity_1h` score `1.6027` n `37` status `ready` deltaP `13.2344` edge `0.0844` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.549` n `37` status `ready` deltaP `7.4654` edge `0.0994` maxDD `-0.2737`
- `news_risk_high->metal_1h` score `1.3077` n `37` status `ready` deltaP `15.6134` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `1.1774` n `37` status `ready` deltaP `6.3158` edge `0.0743` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.1622` n `37` status `ready` deltaP `14.5736` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->fx_24h` score `0.983` n `37` status `ready` deltaP `20.6503` edge `0.0458` maxDD `-3.1244`
- `news_risk_high->crypto_alt_1h` score `0.8794` n `37` status `ready` deltaP `8.7272` edge `0.0416` maxDD `-0.7867`
- `risk_on_high->crypto_major_24h` score `0.4326` n `80` status `ready` deltaP `10.7292` edge `0.7817` maxDD `-52.4879`
- `risk_on_and_context->crypto_major_24h` score `0.4326` n `80` status `ready` deltaP `10.7292` edge `0.7817` maxDD `-52.4879`
- `news_risk_high->crypto_alt_4h` score `0.151` n `37` status `ready` deltaP `3.502` edge `0.0221` maxDD `-1.296`
- `news_risk_high->crypto_major_24h` score `0.065` n `37` status `ready` deltaP `15.1887` edge `0.1847` maxDD `-18.2098`
- `news_risk_high->commodity_1h` score `-0.0597` n `37` status `ready` deltaP `5.1263` edge `0.0028` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
