# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T18:22:26.905206+00:00`
- Price records: `672`
- Market context records: `5376`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11528`

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

- `market_context_high->unknown_24h` score `8.4235` n `180` status `ready` deltaP `16.7362` edge `0.6034` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.3725` n `180` status `ready` deltaP `22.4305` edge `0.7522` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.122` n `205` status `ready` deltaP `14.1768` edge `0.3949` maxDD `-14.0065`
- `market_context_high->equity_24h` score `2.7201` n `180` status `ready` deltaP `13.2986` edge `0.7009` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `2.5137` n `205` status `ready` deltaP `10.8537` edge `0.3012` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.6675` n `205` status `ready` deltaP `9.6037` edge `0.2388` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.1161` n `180` status `ready` deltaP `16.7708` edge `0.0949` maxDD `-9.0959`
- `market_context_high->equity_1h` score `0.0579` n `205` status `ready` deltaP `6.1129` edge `0.0606` maxDD `-5.0555`
- `market_context_high->fx_24h` score `-0.0614` n `180` status `ready` deltaP `7.8472` edge `0.0321` maxDD `-0.8294`
- `market_context_high->index_1h` score `-0.1038` n `205` status `ready` deltaP `4.3786` edge `0.0115` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2038` n `205` status `ready` deltaP `1.4802` edge `0.0693` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.2125` n `205` status `ready` deltaP `3.4263` edge `0.084` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.4166` n `205` status `ready` deltaP `-0.5046` edge `-0.0011` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.6041` n `205` status `ready` deltaP `1.0311` edge `0.0103` maxDD `-2.0682`
- `market_context_high->unknown_4h` score `-0.7603` n `205` status `ready` deltaP `8.2927` edge `-0.0002` maxDD `-6.1421`
- `market_context_high->fx_4h` score `-1.1791` n `205` status `ready` deltaP `0.5488` edge `0.001` maxDD `-1.567`
- `market_context_high->index_4h` score `-1.2522` n `205` status `ready` deltaP `4.4207` edge `0.0271` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.5346` n `205` status `ready` deltaP `-3.9192` edge `-0.0073` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.5737` n `205` status `ready` deltaP `-6.6768` edge `-0.033` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.2879` n `180` status `ready` deltaP `13.3333` edge `0.3593` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
