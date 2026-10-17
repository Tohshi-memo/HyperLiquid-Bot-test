# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T14:52:33.869446+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9424`

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

- `risk_on_high->commodity_24h` score `6.9621` n `54` status `ready` deltaP `38.5017` edge `0.3235` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.9621` n `54` status `ready` deltaP `38.5017` edge `0.3235` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `4.0223` n `159` status `ready` deltaP `17.5996` edge `0.3977` maxDD `-7.7207`
- `risk_on_high->crypto_major_4h` score `2.1411` n `85` status `ready` deltaP `18.8648` edge `0.2325` maxDD `-7.7207`
- `risk_on_and_context->crypto_major_4h` score `2.1411` n `85` status `ready` deltaP `18.8648` edge `0.2325` maxDD `-7.7207`
- `market_context_high->crypto_alt_4h` score `1.7193` n `159` status `ready` deltaP `10.1482` edge `0.4503` maxDD `-19.6408`
- `market_context_high->crypto_major_1h` score `0.5559` n `171` status `ready` deltaP `5.883` edge `0.096` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0502` n `159` status `ready` deltaP `9.5577` edge `0.045` maxDD `-1.6961`
- `risk_on_high->index_1h` score `0.0483` n `90` status `ready` deltaP `5.5556` edge `0.0054` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0483` n `90` status `ready` deltaP `5.5556` edge `0.0054` maxDD `-0.7394`
- `market_context_high->crypto_alt_1h` score `0.0338` n `171` status `ready` deltaP `7.0666` edge `0.1057` maxDD `-7.3329`
- `market_context_high->index_1h` score `-0.1813` n `171` status `ready` deltaP `7.0176` edge `0.0048` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2599` n `90` status `ready` deltaP `1.1711` edge `-0.0031` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2599` n `90` status `ready` deltaP `1.1711` edge `-0.0031` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.268` n `171` status `ready` deltaP `6.6735` edge `0.0081` maxDD `-0.9556`
- `market_context_high->equity_1h` score `-0.334` n `171` status `ready` deltaP `10.4552` edge `0.0389` maxDD `-7.1141`
- `market_context_high->equity_4h` score `-0.4786` n `159` status `ready` deltaP `12.2757` edge `0.2009` maxDD `-17.5281`
- `risk_on_high->equity_1h` score `-0.4807` n `90` status `ready` deltaP `9.5195` edge `0.0261` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4807` n `90` status `ready` deltaP `9.5195` edge `0.0261` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.5048` n `90` status `ready` deltaP `0.7086` edge `0.0037` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
