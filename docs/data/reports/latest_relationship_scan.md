# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T01:52:26.112063+00:00`
- Price records: `672`
- Market context records: `6451`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5875`

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

- `news_risk_high->crypto_alt_24h` score `11.6684` n `32` status `ready` deltaP `29.6875` edge `0.7892` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `8.1852` n `145` status `ready` deltaP `18.5895` edge `0.8882` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.307` n `32` status `ready` deltaP `52.2569` edge `0.1772` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1096` n `32` status `ready` deltaP `42.7591` edge `0.062` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.8368` n `32` status `ready` deltaP `33.5069` edge `0.1169` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.3395` n `32` status `ready` deltaP `11.8056` edge `0.4274` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4697` n `32` status `ready` deltaP `29.7904` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4976` n `32` status `ready` deltaP `13.5292` edge `0.1485` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.3339` n `178` status `ready` deltaP `-5.6903` edge `0.2392` maxDD `-3.2083`
- `news_risk_high->crypto_alt_1h` score `0.8599` n `32` status `ready` deltaP `9.5247` edge `0.0929` maxDD `-1.6923`
- `market_context_high->index_4h` score `0.0945` n `178` status `ready` deltaP `7.5465` edge `0.0252` maxDD `-0.4108`
- `market_context_high->metal_4h` score `-0.109` n `178` status `ready` deltaP `8.6754` edge `0.0419` maxDD `-2.7056`
- `market_context_high->commodity_24h` score `-0.1707` n `145` status `ready` deltaP `3.6147` edge `0.1485` maxDD `-5.2791`
- `market_context_high->unknown_4h` score `-0.1808` n `178` status `ready` deltaP `-15.3295` edge `0.3277` maxDD `-10.5788`
- `news_risk_high->unknown_1h` score `-0.2284` n `32` status `ready` deltaP `5.9319` edge `-0.0241` maxDD `-0.7581`
- `market_context_high->crypto_alt_4h` score `-0.3868` n `178` status `ready` deltaP `7.0636` edge `0.0961` maxDD `-8.367`
- `news_risk_high->metal_1h` score `-0.5059` n `32` status `ready` deltaP `1.3473` edge `-0.0241` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.5616` n `178` status `ready` deltaP `6.3295` edge `0.0171` maxDD `-5.8368`
- `market_context_high->metal_1h` score `-0.5848` n `178` status `ready` deltaP `0.2237` edge `0.0013` maxDD `-1.8877`
- `news_risk_high->index_24h` score `-0.5946` n `32` status `ready` deltaP `2.7778` edge `-0.0076` maxDD `-2.3058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
