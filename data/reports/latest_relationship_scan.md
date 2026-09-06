# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T04:07:27.528166+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10839`

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

- `risk_on_high->unknown_4h` score `21.9139` n `145` status `ready` deltaP `-3.3126` edge `2.0488` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `21.9139` n `145` status `ready` deltaP `-3.3126` edge `2.0488` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.4467` n `245` status `ready` deltaP `1.2476` edge `0.9424` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `4.3848` n `37` status `ready` deltaP `21.8797` edge `0.2465` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.9643` n `37` status `ready` deltaP `20.1389` edge `0.1961` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.1717` n `37` status `ready` deltaP `15.8084` edge `0.2002` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.5015` n `37` status `ready` deltaP `25.6757` edge `0.0594` maxDD `-0.7692`
- `market_context_high->equity_24h` score `1.8487` n `165` status `ready` deltaP `13.7689` edge `0.4161` maxDD `-16.9737`
- `news_risk_high->equity_1h` score `1.5596` n `37` status `ready` deltaP `12.7853` edge `0.0838` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.5454` n `37` status `ready` deltaP `7.4654` edge `0.0991` maxDD `-0.2737`
- `news_risk_high->metal_1h` score `1.3436` n `37` status `ready` deltaP `16.0625` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1622` n `37` status `ready` deltaP `14.5736` edge `0.0131` maxDD `-0.0724`
- `risk_on_high->crypto_major_24h` score `1.1404` n `82` status `ready` deltaP `10.9672` edge `0.8057` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `1.1404` n `82` status `ready` deltaP `10.9672` edge `0.8057` maxDD `-47.9416`
- `news_risk_high->fx_24h` score `1.103` n `37` status `ready` deltaP `21.8656` edge `0.0477` maxDD `-3.1244`
- `news_risk_high->crypto_major_1h` score `1.036` n `37` status `ready` deltaP `5.4176` edge `0.0685` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.7595` n `37` status `ready` deltaP `8.1284` edge `0.0356` maxDD `-0.7867`
- `news_risk_high->commodity_1h` score `-0.0286` n `37` status `ready` deltaP `5.7251` edge `0.0028` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1162` n `145` status `ready` deltaP `4.937` edge `-0.0031` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1162` n `145` status `ready` deltaP `4.937` edge `-0.0031` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
