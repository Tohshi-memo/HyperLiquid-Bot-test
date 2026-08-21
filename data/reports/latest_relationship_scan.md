# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T09:22:30.302056+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13758`

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

- `market_context_high->index_1h` score `0.3778` n `106` status `ready` deltaP `11.0666` edge `0.0064` maxDD `-0.5622`
- `market_context_high->equity_1h` score `0.3578` n `106` status `ready` deltaP `8.7617` edge `0.0529` maxDD `-3.1861`
- `market_context_high->equity_4h` score `0.0895` n `105` status `ready` deltaP `4.7402` edge `0.1388` maxDD `-8.3685`
- `market_context_high->fx_4h` score `0.0803` n `105` status `ready` deltaP `7.9428` edge `0.0076` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1888` n `106` status `ready` deltaP `1.0931` edge `0.0044` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2562` n `105` status `ready` deltaP `6.5302` edge `-0.0188` maxDD `-1.273`
- `market_context_high->metal_1h` score `-0.2835` n `106` status `ready` deltaP `2.6212` edge `-0.0024` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.2925` n `105` status `ready` deltaP `5.5807` edge `0.0177` maxDD `-1.7252`
- `market_context_high->commodity_24h` score `-0.3491` n `103` status `ready` deltaP `5.0752` edge `0.1204` maxDD `-4.666`
- `market_context_high->unknown_1h` score `-0.5146` n `106` status `ready` deltaP `7.2054` edge `-0.0682` maxDD `-0.4843`
- `market_context_high->commodity_4h` score `-0.7411` n `105` status `ready` deltaP `-2.6524` edge `0.0077` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7903` n `106` status `ready` deltaP `-6.4682` edge `-0.0016` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-1.0219` n `106` status `ready` deltaP `-2.8725` edge `-0.0317` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.1033` n `106` status `ready` deltaP `-1.9602` edge `-0.0439` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-3.2004` n `105` status `ready` deltaP `-0.9016` edge `-0.1337` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-3.2563` n `103` status `ready` deltaP `-14.9643` edge `-0.0125` maxDD `-2.0613`
- `market_context_high->crypto_major_4h` score `-3.4972` n `105` status `ready` deltaP `1.1948` edge `-0.1973` maxDD `-3.1677`
- `market_context_high->index_24h` score `-4.0257` n `103` status `ready` deltaP `-3.1924` edge `-0.0446` maxDD `-18.6848`
- `market_context_high->unknown_24h` score `-4.4281` n `103` status `ready` deltaP `10.8937` edge `-0.391` maxDD `-1.0505`
- `market_context_high->metal_24h` score `-4.4708` n `103` status `ready` deltaP `-17.6088` edge `-0.125` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
