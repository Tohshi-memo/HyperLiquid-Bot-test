# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T21:13:07.997178+00:00`
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

- `market_context_high->equity_4h` score `2.2855` n `96` status `ready` deltaP `11.6107` edge `0.2019` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.8032` n `96` status `ready` deltaP `14.8516` edge `0.0814` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9869` n `96` status `ready` deltaP `16.5107` edge `0.0109` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.5076` n `96` status `ready` deltaP `13.2113` edge `0.0118` maxDD `-1.273`
- `market_context_high->index_4h` score `0.2954` n `96` status `ready` deltaP `9.7815` edge `0.0249` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.2402` n `96` status `ready` deltaP `6.4236` edge `0.1713` maxDD `-4.666`
- `market_context_high->unknown_24h` score `0.0723` n `96` status `ready` deltaP `17.7083` edge `-0.0614` maxDD `-1.0505`
- `market_context_high->fx_4h` score `0.0367` n `96` status `ready` deltaP `7.4949` edge `0.005` maxDD `-0.3539`
- `market_context_high->unknown_1h` score `-0.1213` n `96` status `ready` deltaP `6.3623` edge `-0.0298` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.1508` n `96` status `ready` deltaP `3.2747` edge `0.0043` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3276` n `96` status `ready` deltaP `-1.3224` edge `0.0027` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.6638` n `96` status `ready` deltaP `-0.94` edge `0.0062` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8056` n `96` status `ready` deltaP `-0.4678` edge `-0.02` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.8625` n `96` status `ready` deltaP `1.3348` edge `-0.035` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8884` n `96` status `ready` deltaP `-7.7408` edge `-0.0057` maxDD `-1.1941`
- `market_context_high->crypto_major_24h` score `-1.4005` n `96` status `ready` deltaP `2.9514` edge `-0.0156` maxDD `-4.9964`
- `market_context_high->crypto_major_4h` score `-1.4317` n `96` status `ready` deltaP `5.8181` edge `-0.056` maxDD `-3.1677`
- `market_context_high->crypto_alt_4h` score `-1.6512` n `96` status `ready` deltaP `3.6585` edge `-0.035` maxDD `-5.4926`
- `market_context_high->metal_24h` score `-3.0903` n `96` status `ready` deltaP `-9.375` edge `-0.0029` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.4167` n `96` status `ready` deltaP `-17.8819` edge `-0.0072` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
