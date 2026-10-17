# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T17:52:26.957085+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9582`

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

- `risk_on_high->commodity_24h` score `6.9461` n `54` status `ready` deltaP `38.676` edge `0.321` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.9461` n `54` status `ready` deltaP `38.676` edge `0.321` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `1.614` n `171` status `ready` deltaP `13.9923` edge `0.3495` maxDD `-13.9957`
- `risk_on_high->crypto_major_4h` score `0.5651` n `90` status `ready` deltaP `16.0976` edge `0.2021` maxDD `-10.6246`
- `risk_on_and_context->crypto_major_4h` score `0.5651` n `90` status `ready` deltaP `16.0976` edge `0.2021` maxDD `-10.6246`
- `market_context_high->crypto_major_1h` score `0.5029` n `174` status `ready` deltaP `5.3703` edge `0.095` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.0902` n `174` status `ready` deltaP `7.5917` edge `0.1069` maxDD `-7.3329`
- `risk_on_high->index_1h` score `0.0639` n `90` status `ready` deltaP `5.7057` edge `0.0057` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0639` n `90` status `ready` deltaP `5.7057` edge `0.0057` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1882` n `174` status `ready` deltaP `6.8551` edge `0.005` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2592` n `90` status `ready` deltaP `1.1711` edge `-0.003` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2592` n `90` status `ready` deltaP `1.1711` edge `-0.003` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3074` n `174` status `ready` deltaP `5.9157` edge `0.0081` maxDD `-0.9556`
- `market_context_high->equity_1h` score `-0.3689` n `174` status `ready` deltaP `10.1584` edge `0.0387` maxDD `-7.2977`
- `risk_on_high->equity_1h` score `-0.4134` n `90` status `ready` deltaP `10.1201` edge `0.0277` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4134` n `90` status `ready` deltaP `10.1201` edge `0.0277` maxDD `-5.3696`
- `market_context_high->metal_4h` score `-0.4396` n `171` status `ready` deltaP `5.9104` edge `0.041` maxDD `-1.6961`
- `risk_on_high->metal_1h` score `-0.4955` n `90` status `ready` deltaP `0.8583` edge `0.0039` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4955` n `90` status `ready` deltaP `0.8583` edge `0.0039` maxDD `-0.8513`
- `risk_on_high->crypto_major_1h` score `-0.6985` n `90` status `ready` deltaP `0.2362` edge `0.0008` maxDD `-4.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
