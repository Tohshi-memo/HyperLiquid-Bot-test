# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T14:52:16.560976+00:00`
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

- `market_context_high->equity_4h` score `0.5683` n `105` status `ready` deltaP `7.4841` edge `0.1604` maxDD `-8.3685`
- `market_context_high->equity_1h` score `0.4887` n `105` status `ready` deltaP `9.4682` edge `0.0591` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3287` n `105` status `ready` deltaP `10.4078` edge `0.0067` maxDD `-0.5622`
- `market_context_high->metal_4h` score `0.1813` n `105` status `ready` deltaP `12.018` edge `0.0007` maxDD `-1.273`
- `market_context_high->fx_4h` score `0.0044` n `105` status `ready` deltaP `6.7232` edge `0.006` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.1262` n `105` status `ready` deltaP `3.8366` edge `0.0026` maxDD `-0.4291`
- `market_context_high->commodity_24h` score `-0.137` n `96` status `ready` deltaP `3.8194` edge `0.1403` maxDD `-4.666`
- `market_context_high->fx_1h` score `-0.2014` n `105` status `ready` deltaP `0.9253` edge `0.0039` maxDD `-0.2043`
- `market_context_high->index_4h` score `-0.2451` n `105` status `ready` deltaP `6.1905` edge `0.0197` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.339` n `105` status `ready` deltaP `7.4808` edge `-0.0554` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.3747` n `105` status `ready` deltaP `2.2983` edge `0.0168` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.5448` n `105` status `ready` deltaP `2.4351` edge `-0.0016` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7182` n `105` status `ready` deltaP `-2.3476` edge `0.0086` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7962` n `105` status `ready` deltaP `-6.6267` edge `-0.0013` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.0694` n `105` status `ready` deltaP `5.5009` edge `0.0012` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.2942` n `105` status `ready` deltaP `7.5973` edge `-0.0564` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-1.5057` n `96` status `ready` deltaP `17.7083` edge `-0.1929` maxDD `-1.0505`
- `market_context_high->index_24h` score `-3.5838` n `96` status `ready` deltaP `1.2152` edge `-0.0508` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.7766` n `96` status `ready` deltaP `-21.1805` edge `-0.0152` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9315` n `96` status `ready` deltaP `-21.0069` edge `-0.1614` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
