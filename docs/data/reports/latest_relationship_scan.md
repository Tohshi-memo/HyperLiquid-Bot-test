# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T04:37:38.724039+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11685`

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

- `market_context_high->unknown_24h` score `12.3424` n `90` status `ready` deltaP `4.4445` edge `1.0032` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.1344` n `109` status `ready` deltaP `-0.8881` edge `0.45` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2806` n `109` status `ready` deltaP `14.3615` edge `0.0956` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.7721` n `90` status `ready` deltaP `2.0139` edge `0.2024` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.7078` n `90` status `ready` deltaP `23.507` edge `0.0546` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4886` n `109` status `ready` deltaP `8.5082` edge `0.0256` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0057` n `109` status `ready` deltaP `5.6831` edge `-0.0024` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1414` n `109` status `ready` deltaP `9.0093` edge `0.0078` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5666` n `109` status `ready` deltaP `-2.159` edge `-0.0088` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7439` n `109` status `ready` deltaP `-3.3566` edge `-0.0196` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.9618` n `109` status `ready` deltaP `0.9552` edge `-0.0062` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.3364` n `90` status `ready` deltaP `-0.1389` edge `-0.0261` maxDD `-4.5445`
- `market_context_high->index_24h` score `-1.4966` n `90` status `ready` deltaP `-3.9584` edge `0.054` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.5301` n `109` status `ready` deltaP `-5.4373` edge `-0.0202` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.8728` n `109` status `ready` deltaP `0.82` edge `-0.092` maxDD `-10.619`
- `market_context_high->crypto_alt_4h` score `-2.1285` n `109` status `ready` deltaP `1.2321` edge `-0.0466` maxDD `-5.7857`
- `market_context_high->index_4h` score `-2.1643` n `109` status `ready` deltaP `-13.43` edge `-0.0625` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.2717` n `109` status `ready` deltaP `2.0326` edge `-0.2415` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3582` n `109` status `ready` deltaP `-11.8978` edge `-0.0632` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.1807` n `90` status `ready` deltaP `9.0973` edge `-0.0316` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
