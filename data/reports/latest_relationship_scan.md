# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T21:27:28.515269+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `55.2202` n `50` status `ready` deltaP `15.5979` edge `4.4977` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.0546` n `50` status `ready` deltaP `46.26` edge `2.5736` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `9.1463` n `68` status `ready` deltaP `18.5258` edge `0.6697` maxDD `-1.4812`
- `news_risk_high->crypto_major_24h` score `7.8078` n `50` status `ready` deltaP `25.4211` edge `0.5305` maxDD `-2.6128`
- `news_risk_high->equity_24h` score `6.2815` n `50` status `ready` deltaP `30.1005` edge `0.4156` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `4.5289` n `120` status `ready` deltaP `8.9312` edge `0.3911` maxDD `-3.1917`
- `news_risk_high->metal_24h` score `4.3974` n `50` status `ready` deltaP `43.4073` edge `0.0813` maxDD `-0.0053`
- `news_risk_high->unknown_1h` score `3.4945` n `71` status `ready` deltaP `9.4059` edge `0.2642` maxDD `-0.8558`
- `market_context_high->metal_24h` score `3.2146` n `120` status `ready` deltaP `28.7406` edge `0.1782` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.4022` n `50` status `ready` deltaP `26.9948` edge `0.0353` maxDD `-0.2064`
- `news_risk_high->fx_4h` score `2.3109` n `68` status `ready` deltaP `32.9717` edge `0.0231` maxDD `-0.3605`
- `market_context_high->unknown_4h` score `2.3051` n `120` status `ready` deltaP `17.3984` edge `0.1168` maxDD `-0.5894`
- `market_context_high->unknown_1h` score `0.9071` n `120` status `ready` deltaP `9.2416` edge `0.059` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.5962` n `71` status `ready` deltaP `12.3598` edge `0.006` maxDD `-0.0975`
- `news_risk_high->commodity_1h` score `0.3743` n `71` status `ready` deltaP `11.4616` edge `0.0036` maxDD `-0.5618`
- `market_context_high->metal_4h` score `0.076` n `120` status `ready` deltaP `13.1504` edge `0.0138` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.395` n `120` status `ready` deltaP `3.4631` edge `-0.0005` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.4841` n `71` status `ready` deltaP `-1.3304` edge `-0.0098` maxDD `-0.8054`
- `news_risk_high->index_4h` score `-0.646` n `68` status `ready` deltaP `0.0` edge `-0.02` maxDD `-1.6927`
- `news_risk_high->metal_1h` score `-0.6767` n `71` status `ready` deltaP `-0.4048` edge `-0.0265` maxDD `-2.605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
