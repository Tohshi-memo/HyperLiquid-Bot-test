# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T20:37:36.761019+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8016`

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

- `market_context_high->unknown_4h` score `93.0075` n `153` status `ready` deltaP `1.0172` edge `7.7774` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `24.6529` n `153` status `ready` deltaP `1.4745` edge `2.0935` maxDD `-1.5807`
- `market_context_high->metal_24h` score `0.3038` n `112` status `ready` deltaP `24.282` edge `0.1397` maxDD `-7.0108`
- `market_context_high->fx_1h` score `0.265` n `153` status `ready` deltaP `8.2648` edge `0.0028` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0982` n `153` status `ready` deltaP `9.0198` edge `0.0079` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.0129` n `112` status `ready` deltaP `16.3051` edge `0.0135` maxDD `-4.5747`
- `market_context_high->metal_1h` score `-0.1135` n `153` status `ready` deltaP `8.6298` edge `0.0071` maxDD `-1.6682`
- `market_context_high->fx_24h` score `-0.2229` n `112` status `ready` deltaP `15.4122` edge `0.0259` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.2594` n `153` status `ready` deltaP `2.3023` edge `0.0131` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.5416` n `153` status `ready` deltaP `0.7612` edge `-0.0008` maxDD `-1.8971`
- `market_context_high->commodity_4h` score `-0.6732` n `153` status `ready` deltaP `4.2294` edge `0.0386` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.8654` n `153` status `ready` deltaP `4.3834` edge `0.0179` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9376` n `153` status `ready` deltaP `7.6648` edge `-0.0003` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.7653` n `153` status `ready` deltaP `1.904` edge `-0.0114` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.9648` n `153` status `ready` deltaP `-0.2759` edge `-0.0016` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.3387` n `153` status `ready` deltaP `-5.6223` edge `-0.0231` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.4087` n `112` status `ready` deltaP `-2.4449` edge `-0.0632` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.5417` n `153` status `ready` deltaP `0.1514` edge `-0.0793` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.177` n `112` status `ready` deltaP `-15.3441` edge `-0.1307` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.3574` n `112` status `ready` deltaP `-5.1235` edge `-0.2376` maxDD `-35.4638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
