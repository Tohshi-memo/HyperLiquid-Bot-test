# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T21:22:26.825570+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10827`

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

- `market_context_high->equity_4h` score `2.2771` n `96` status `ready` deltaP `11.6107` edge `0.2012` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.7984` n `96` status `ready` deltaP `14.8516` edge `0.081` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9857` n `96` status `ready` deltaP `16.5107` edge `0.0108` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.5052` n `96` status `ready` deltaP `13.2113` edge `0.0116` maxDD `-1.273`
- `market_context_high->index_4h` score `0.2942` n `96` status `ready` deltaP `9.7815` edge `0.0248` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.2348` n `96` status `ready` deltaP `6.4236` edge `0.1706` maxDD `-4.666`
- `market_context_high->unknown_24h` score `0.0471` n `96` status `ready` deltaP `17.7083` edge `-0.0635` maxDD `-1.0505`
- `market_context_high->fx_4h` score `0.0367` n `96` status `ready` deltaP `7.4949` edge `0.005` maxDD `-0.3539`
- `market_context_high->unknown_1h` score `-0.1428` n `96` status `ready` deltaP `6.2126` edge `-0.0306` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.1652` n `96` status `ready` deltaP `3.125` edge `0.0041` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3276` n `96` status `ready` deltaP `-1.3224` edge `0.0027` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.6614` n `96` status `ready` deltaP `-0.94` edge `0.0065` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8438` n `96` status `ready` deltaP `-0.6175` edge `-0.0239` maxDD `-2.413`
- `market_context_high->commodity_1h` score `-0.8884` n `96` status `ready` deltaP `-7.7408` edge `-0.0057` maxDD `-1.1941`
- `market_context_high->crypto_major_1h` score `-0.9132` n `96` status `ready` deltaP `1.1851` edge `-0.0405` maxDD `-2.7581`
- `market_context_high->crypto_major_4h` score `-1.5543` n `96` status `ready` deltaP `5.6656` edge `-0.0652` maxDD `-3.1677`
- `market_context_high->crypto_major_24h` score `-1.6177` n `96` status `ready` deltaP `2.9514` edge `-0.0337` maxDD `-4.9964`
- `market_context_high->crypto_alt_4h` score `-1.7198` n `96` status `ready` deltaP `3.5061` edge `-0.0397` maxDD `-5.4926`
- `market_context_high->metal_24h` score `-3.1227` n `96` status `ready` deltaP `-9.5486` edge `-0.0059` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.3968` n `96` status `ready` deltaP `-17.7083` edge `-0.0067` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
