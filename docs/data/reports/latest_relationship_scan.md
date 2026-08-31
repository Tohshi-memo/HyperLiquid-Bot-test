# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T16:07:38.199045+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11688`

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

- `risk_on_high->unknown_4h` score `8.0294` n `107` status `ready` deltaP `24.641` edge `0.5665` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.0294` n `107` status `ready` deltaP `24.641` edge `0.5665` maxDD `-2.266`
- `risk_on_high->crypto_alt_24h` score `6.954` n `70` status `ready` deltaP `29.881` edge `1.0491` maxDD `-22.8746`
- `risk_on_and_context->crypto_alt_24h` score `6.954` n `70` status `ready` deltaP `29.881` edge `1.0491` maxDD `-22.8746`
- `market_context_high->unknown_4h` score `6.4834` n `159` status `ready` deltaP `21.3376` edge `0.4674` maxDD `-2.5493`
- `market_context_high->crypto_alt_24h` score `3.4895` n `113` status `ready` deltaP `14.3437` edge `0.6183` maxDD `-27.517`
- `risk_on_high->fx_24h` score `2.5619` n `70` status `ready` deltaP `55.4811` edge `0.0391` maxDD `-1.4419`
- `risk_on_and_context->fx_24h` score `2.5619` n `70` status `ready` deltaP `55.4811` edge `0.0391` maxDD `-1.4419`
- `risk_on_high->unknown_1h` score `2.437` n `107` status `ready` deltaP `6.8149` edge `0.2153` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.437` n `107` status `ready` deltaP `6.8149` edge `0.2153` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.2144` n `159` status `ready` deltaP `6.1566` edge `0.2065` maxDD `-2.041`
- `news_risk_high->unknown_1h` score `1.5335` n `61` status `ready` deltaP `3.9192` edge `0.1363` maxDD `-1.1043`
- `market_context_high->fx_24h` score `1.1783` n `113` status `ready` deltaP `33.5469` edge `0.0259` maxDD `-2.1083`
- `market_context_high->metal_24h` score `0.9753` n `113` status `ready` deltaP `25.086` edge `0.1633` maxDD `-7.7739`
- `risk_on_high->commodity_24h` score `0.9733` n `70` status `ready` deltaP `10.9325` edge `0.1507` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.9733` n `70` status `ready` deltaP `10.9325` edge `0.1507` maxDD `-0.5706`
- `news_risk_high->commodity_24h` score `0.3552` n `44` status `ready` deltaP `5.9975` edge `0.0371` maxDD `-1.1904`
- `news_risk_high->commodity_4h` score `0.3315` n `61` status `ready` deltaP `8.5591` edge `0.0271` maxDD `-1.3325`
- `news_risk_high->fx_4h` score `0.2597` n `61` status `ready` deltaP `12.0252` edge `0.0008` maxDD `-0.7461`
- `market_context_high->commodity_1h` score `0.2354` n `159` status `ready` deltaP `9.9292` edge `0.0184` maxDD `-1.5315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
