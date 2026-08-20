# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T15:37:29.870439+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10819`

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

- `market_context_high->equity_4h` score `0.6176` n `105` status `ready` deltaP `7.6365` edge `0.1635` maxDD `-8.3685`
- `market_context_high->equity_1h` score `0.4612` n `105` status `ready` deltaP `9.3185` edge `0.0578` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3143` n `105` status `ready` deltaP `10.2581` edge `0.0065` maxDD `-0.5622`
- `market_context_high->metal_4h` score `0.1442` n `105` status `ready` deltaP `11.5607` edge `-0.001` maxDD `-1.273`
- `market_context_high->fx_4h` score `0.0131` n `105` status `ready` deltaP `6.8757` edge `0.0061` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.1005` n `96` status `ready` deltaP `4.3403` edge `0.1415` maxDD `-4.666`
- `market_context_high->metal_1h` score `-0.1814` n `105` status `ready` deltaP `3.3875` edge `0.001` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.1936` n `105` status `ready` deltaP `1.075` edge `0.0039` maxDD `-0.2043`
- `market_context_high->index_4h` score `-0.2269` n `105` status `ready` deltaP `6.4954` edge `0.02` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.3726` n `105` status `ready` deltaP `7.3311` edge `-0.0572` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.441` n `105` status `ready` deltaP `1.8492` edge `0.0113` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.6079` n `105` status `ready` deltaP `1.986` edge `-0.0067` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7064` n `105` status `ready` deltaP `-2.1951` edge `0.0091` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7712` n `105` status `ready` deltaP `-6.3273` edge `-0.0001` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.202` n `105` status `ready` deltaP `5.0436` edge `-0.0068` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.4232` n `105` status `ready` deltaP `7.1399` edge `-0.0641` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-1.6281` n `96` status `ready` deltaP `17.7083` edge `-0.2031` maxDD `-1.0505`
- `market_context_high->index_24h` score `-3.583` n `96` status `ready` deltaP `1.2152` edge `-0.0507` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.785` n `96` status `ready` deltaP `-21.1805` edge `-0.0159` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9447` n `96` status `ready` deltaP `-21.0069` edge `-0.1631` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
