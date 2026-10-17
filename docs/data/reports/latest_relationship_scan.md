# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T11:37:27.471740+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9348`

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

- `risk_on_high->commodity_24h` score `7.0317` n `54` status `ready` deltaP `38.5017` edge `0.3293` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0317` n `54` status `ready` deltaP `38.5017` edge `0.3293` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.5504` n `146` status `ready` deltaP `21.3143` edge `0.4526` maxDD `-5.906`
- `market_context_high->crypto_alt_4h` score `5.3306` n `146` status `ready` deltaP `13.3186` edge `0.5256` maxDD `-7.6136`
- `risk_on_high->crypto_major_4h` score `5.2329` n `72` status `ready` deltaP `28.5061` edge `0.3313` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.2329` n `72` status `ready` deltaP `28.5061` edge `0.3313` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `1.2656` n `72` status `ready` deltaP `5.8605` edge `0.2357` maxDD `-7.5444`
- `risk_on_and_context->crypto_alt_4h` score `1.2656` n `72` status `ready` deltaP `5.8605` edge `0.2357` maxDD `-7.5444`
- `market_context_high->crypto_major_1h` score `0.8077` n `158` status `ready` deltaP `6.4447` edge `0.1049` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.5131` n `158` status `ready` deltaP `7.8602` edge `0.1218` maxDD `-5.8485`
- `market_context_high->metal_4h` score `0.409` n `146` status `ready` deltaP `13.5483` edge `0.0483` maxDD `-1.6961`
- `risk_on_high->index_1h` score `0.24` n `84` status `ready` deltaP `7.7864` edge `0.0065` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.24` n `84` status `ready` deltaP `7.7864` edge `0.0065` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1311` n `158` status `ready` deltaP `7.937` edge `0.0051` maxDD `-1.3195`
- `risk_on_high->equity_1h` score `-0.2427` n `84` status `ready` deltaP `11.9691` edge `0.0296` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.2427` n `84` status `ready` deltaP `11.9691` edge `0.0296` maxDD `-5.3696`
- `market_context_high->metal_1h` score `-0.2824` n `158` status `ready` deltaP `8.207` edge `0.0087` maxDD `-0.9556`
- `market_context_high->equity_1h` score `-0.3372` n `158` status `ready` deltaP `10.3718` edge `0.0386` maxDD `-7.0778`
- `market_context_high->equity_4h` score `-0.3686` n `146` status `ready` deltaP `14.348` edge `0.1997` maxDD `-17.4086`
- `risk_on_high->fx_1h` score `-0.4028` n `84` status `ready` deltaP `-1.5015` edge `-0.0036` maxDD `-0.376`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
