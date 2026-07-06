# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T03:52:31.926571+00:00`
- Price records: `672`
- Market context records: `5842`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10128`

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

- `news_risk_high->fx_1h` score `1.9387` n `30` status `ready` deltaP `23.483` edge `0.0189` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.8231` n `30` status `ready` deltaP `11.2375` edge `0.0773` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.7383` n `262` status `ready` deltaP `7.8012` edge `0.1553` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.1749` n `30` status `ready` deltaP `4.5709` edge `0.0381` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3327` n `262` status `ready` deltaP `0.9131` edge `-0.0002` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.3608` n `262` status `ready` deltaP `4.579` edge `0.0401` maxDD `-5.0555`
- `news_risk_high->metal_1h` score `-0.4258` n `30` status `ready` deltaP `1.3872` edge `-0.0272` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5162` n `262` status `ready` deltaP `-0.6731` edge `-0.0016` maxDD `-2.1412`
- `market_context_high->metal_1h` score `-0.5242` n `262` status `ready` deltaP `3.0157` edge `0.0033` maxDD `-2.0339`
- `market_context_high->index_1h` score `-0.5397` n `262` status `ready` deltaP `1.4216` edge `0.0061` maxDD `-0.7819`
- `market_context_high->equity_24h` score `-0.6376` n `234` status `ready` deltaP `16.3595` edge `0.3457` maxDD `-31.6316`
- `market_context_high->crypto_major_1h` score `-0.8658` n `262` status `ready` deltaP `3.2477` edge `0.0383` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.0713` n `262` status `ready` deltaP `1.721` edge `0.0327` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1747` n `262` status `ready` deltaP `0.5434` edge `0.0145` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.2346` n `30` status `ready` deltaP `-12.3952` edge `-0.0242` maxDD `-1.1161`
- `market_context_high->fx_4h` score `-1.6985` n `262` status `ready` deltaP `-3.1267` edge `-0.002` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.7206` n `234` status `ready` deltaP `6.3301` edge `0.019` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-2.1132` n `262` status `ready` deltaP `-4.4172` edge `-0.0411` maxDD `-8.6964`
- `market_context_high->commodity_4h` score `-2.4096` n `262` status `ready` deltaP `-0.3224` edge `-0.0135` maxDD `-7.4789`
- `market_context_high->index_24h` score `-2.92` n `234` status `ready` deltaP `2.9114` edge `0.0207` maxDD `-18.1572`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
