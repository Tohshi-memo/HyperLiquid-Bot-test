# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T21:37:32.642376+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `risk_on_high->unknown_4h` score `7.803` n `107` status `ready` deltaP `23.4215` edge `0.5558` maxDD `-2.2689`
- `risk_on_and_context->unknown_4h` score `7.803` n `107` status `ready` deltaP `23.4215` edge `0.5558` maxDD `-2.2689`
- `market_context_high->unknown_4h` score `6.2558` n `159` status `ready` deltaP `20.1181` edge `0.4566` maxDD `-2.5526`
- `risk_on_high->unknown_1h` score `2.2028` n `107` status `ready` deltaP `5.6173` edge `0.2038` maxDD `-1.9477`
- `risk_on_and_context->unknown_1h` score `2.2028` n `107` status `ready` deltaP `5.6173` edge `0.2038` maxDD `-1.9477`
- `market_context_high->unknown_1h` score `1.979` n `159` status `ready` deltaP `4.959` edge `0.1949` maxDD `-2.0436`
- `risk_on_high->commodity_24h` score `1.8922` n `90` status `ready` deltaP `14.0973` edge `0.1625` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.8922` n `90` status `ready` deltaP `14.0973` edge `0.1625` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.2972` n `61` status `ready` deltaP `2.7216` edge `0.1246` maxDD `-1.1049`
- `risk_on_high->fx_24h` score `0.8943` n `90` status `ready` deltaP `41.8403` edge `0.0238` maxDD `-3.3794`
- `risk_on_and_context->fx_24h` score `0.8943` n `90` status `ready` deltaP `41.8403` edge `0.0238` maxDD `-3.3794`
- `risk_on_high->crypto_alt_24h` score `0.6025` n `90` status `ready` deltaP `13.0556` edge `0.6779` maxDD `-42.682`
- `risk_on_and_context->crypto_alt_24h` score `0.6025` n `90` status `ready` deltaP `13.0556` edge `0.6779` maxDD `-42.682`
- `news_risk_high->commodity_4h` score `0.1981` n `61` status `ready` deltaP `6.5774` edge `0.0232` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `0.1755` n `159` status `ready` deltaP `9.3304` edge `0.0174` maxDD `-1.5315`
- `news_risk_high->fx_4h` score `0.1086` n `61` status `ready` deltaP `10.196` edge `0.0004` maxDD `-0.7461`
- `risk_on_high->commodity_1h` score `-0.001` n `107` status `ready` deltaP `5.6215` edge `0.0146` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.001` n `107` status `ready` deltaP `5.6215` edge `0.0146` maxDD `-0.8428`
- `risk_on_high->index_1h` score `-0.0524` n `107` status `ready` deltaP `5.6984` edge `-0.0002` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0524` n `107` status `ready` deltaP `5.6984` edge `-0.0002` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
