# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T23:07:44.287385+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5932`

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

- `market_context_high->unknown_24h` score `40.5201` n `43` status `ready` deltaP `27.0147` edge `3.2009` maxDD `-0.0128`
- `market_context_high->unknown_4h` score `12.7907` n `65` status `ready` deltaP `11.3462` edge `1.0375` maxDD `-1.4466`
- `market_context_high->crypto_alt_24h` score `10.5046` n `43` status `ready` deltaP `48.2316` edge `0.5712` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `9.4712` n `43` status `ready` deltaP `45.8011` edge `0.496` maxDD `-0.2995`
- `news_risk_high->fx_24h` score `1.0313` n `31` status `ready` deltaP `12.192` edge `0.0699` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.9054` n `31` status `ready` deltaP `19.3886` edge `0.008` maxDD `-0.6947`
- `market_context_high->commodity_4h` score `0.7197` n `65` status `ready` deltaP `10.2908` edge `0.076` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.5743` n `65` status `ready` deltaP `19.1182` edge `0.0064` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.4946` n `77` status `ready` deltaP `11.5892` edge `-0.0012` maxDD `-0.7878`
- `market_context_high->commodity_1h` score `0.2565` n `77` status `ready` deltaP `6.1922` edge `0.0217` maxDD `-1.3282`
- `news_risk_high->fx_4h` score `0.0995` n `31` status `ready` deltaP `4.1306` edge `0.0355` maxDD `-0.356`
- `news_risk_high->equity_4h` score `0.0229` n `31` status `ready` deltaP `-9.7167` edge `0.1351` maxDD `-2.8064`
- `news_risk_high->commodity_4h` score `-0.113` n `31` status `ready` deltaP `9.8938` edge `-0.0253` maxDD `-1.6728`
- `news_risk_high->index_1h` score `-0.1326` n `31` status `ready` deltaP `1.3956` edge `-0.0065` maxDD `-0.5845`
- `news_risk_high->index_4h` score `-0.1738` n `31` status `ready` deltaP `-2.8078` edge `0.0423` maxDD `-0.3783`
- `news_risk_high->crypto_alt_1h` score `-0.2095` n `31` status `ready` deltaP `9.7933` edge `-0.0281` maxDD `-3.1233`
- `market_context_high->index_1h` score `-0.3084` n `77` status `ready` deltaP `3.6998` edge `-0.0108` maxDD `-1.6054`
- `news_risk_high->fx_1h` score `-0.3502` n `31` status `ready` deltaP `-2.3614` edge `0.002` maxDD `-0.1588`
- `news_risk_high->unknown_4h` score `-0.5142` n `31` status `ready` deltaP `-1.2097` edge `-0.0092` maxDD `-1.5591`
- `market_context_high->metal_1h` score `-0.5854` n `77` status `ready` deltaP `-2.4458` edge `-0.0093` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
