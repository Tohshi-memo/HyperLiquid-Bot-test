# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T13:07:32.019799+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11798`

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

- `market_context_high->unknown_24h` score `203.6013` n `88` status `ready` deltaP `-21.512` edge `26.5145` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `7.5949` n `88` status `ready` deltaP `41.3037` edge `0.3633` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.5324` n `122` status `ready` deltaP `14.8516` edge `0.0758` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.1035` n `125` status `ready` deltaP `1.9066` edge `0.0198` maxDD `-0.624`
- `market_context_high->fx_1h` score `-0.1721` n `125` status `ready` deltaP `0.7042` edge `0.0014` maxDD `-0.2527`
- `market_context_high->fx_4h` score `-0.2772` n `122` status `ready` deltaP `4.6156` edge `0.0066` maxDD `-0.504`
- `market_context_high->metal_1h` score `-0.5354` n `125` status `ready` deltaP `1.3545` edge `-0.0061` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.8169` n `125` status `ready` deltaP `-7.4359` edge `-0.003` maxDD `-0.5064`
- `market_context_high->metal_4h` score `-0.9506` n `122` status `ready` deltaP `7.3971` edge `-0.0138` maxDD `-4.5909`
- `market_context_high->fx_24h` score `-1.5663` n `88` status `ready` deltaP `-9.5802` edge `0.0238` maxDD `-1.8596`
- `market_context_high->equity_1h` score `-1.6635` n `125` status `ready` deltaP `-9.5832` edge `-0.0454` maxDD `-4.9849`
- `market_context_high->metal_24h` score `-1.7018` n `88` status `ready` deltaP `-6.3131` edge `0.0751` maxDD `-7.0954`
- `market_context_high->index_24h` score `-1.9843` n `88` status `ready` deltaP `-4.8454` edge `-0.0681` maxDD `-2.3194`
- `market_context_high->crypto_alt_1h` score `-1.9915` n `125` status `ready` deltaP `-1.5461` edge `-0.0217` maxDD `-7.0497`
- `market_context_high->crypto_major_1h` score `-2.0049` n `125` status `ready` deltaP `-4.5497` edge `-0.0314` maxDD `-5.4277`
- `market_context_high->index_4h` score `-2.1157` n `122` status `ready` deltaP `-12.8049` edge `-0.0097` maxDD `-0.8328`
- `market_context_high->crypto_major_4h` score `-3.5648` n `122` status `ready` deltaP `0.5523` edge `-0.065` maxDD `-13.1929`
- `market_context_high->crypto_major_24h` score `-4.6377` n `88` status `ready` deltaP `-3.267` edge `0.0129` maxDD `-35.189`
- `market_context_high->unknown_1h` score `-7.1928` n `125` status `ready` deltaP `-0.297` edge `-0.5517` maxDD `-1.3246`
- `market_context_high->crypto_alt_4h` score `-8.3331` n `122` status `ready` deltaP `-13.2672` edge `-0.1181` maxDD `-26.3633`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
