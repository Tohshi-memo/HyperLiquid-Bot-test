# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T01:52:27.429067+00:00`
- Price records: `672`
- Market context records: `6146`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `11.6886` n `30` status `ready` deltaP `41.25` edge `0.7138` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.7131` n `30` status `ready` deltaP `68.2292` edge `0.1879` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3189` n `32` status `ready` deltaP `45.0457` edge `0.0642` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4159` n `32` status `ready` deltaP `29.0419` edge `0.0216` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.4011` n `195` status `ready` deltaP `0.3555` edge `0.2152` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.2067` n `32` status `ready` deltaP `13.0801` edge `0.1142` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6252` n `32` status `ready` deltaP `8.3271` edge `0.0708` maxDD `-1.6923`
- `news_risk_high->crypto_major_24h` score `0.2279` n `30` status `ready` deltaP `11.7708` edge `0.0287` maxDD `-4.2368`
- `market_context_high->equity_4h` score `0.215` n `195` status `ready` deltaP `3.1402` edge `0.0887` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.2181` n `30` status `ready` deltaP `7.5` edge `0.0092` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2598` n `195` status `ready` deltaP `1.7342` edge `-0.0003` maxDD `-0.5659`
- `market_context_high->unknown_4h` score `-0.3653` n `195` status `ready` deltaP `-2.6118` edge `0.2402` maxDD `-11.925`
- `market_context_high->metal_24h` score `-0.5736` n `195` status `ready` deltaP `17.2516` edge `0.0683` maxDD `-11.8809`
- `market_context_high->metal_4h` score `-0.599` n `195` status `ready` deltaP `3.847` edge `0.0163` maxDD `-3.4996`
- `news_risk_high->commodity_24h` score `-0.6079` n `30` status `ready` deltaP `14.0973` edge `-0.1241` maxDD `-0.3101`
- `market_context_high->commodity_1h` score `-0.7368` n `195` status `ready` deltaP `-1.8394` edge `-0.0045` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7567` n `32` status `ready` deltaP `-2.8443` edge `-0.0283` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7984` n `195` status `ready` deltaP `2.5403` edge `-0.0036` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.8655` n `195` status `ready` deltaP `-1.4571` edge `0.0103` maxDD `-4.2573`
- `market_context_high->crypto_alt_1h` score `-0.9507` n `195` status `ready` deltaP `3.3111` edge `0.0313` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
