# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T03:22:30.100982+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7652`

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

- `market_context_high->unknown_4h` score `52.6593` n `95` status `ready` deltaP `0.8408` edge `4.4162` maxDD `-1.016`
- `market_context_high->unknown_1h` score `17.3303` n `107` status `ready` deltaP `2.1574` edge `1.4787` maxDD `-1.5781`
- `market_context_high->commodity_24h` score `1.348` n `45` status `ready` deltaP `18.0208` edge `0.0831` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `-0.1781` n `95` status `ready` deltaP `2.9878` edge `0.0423` maxDD `-1.165`
- `market_context_high->commodity_1h` score `-0.2894` n `107` status `ready` deltaP `2.3323` edge `0.0104` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.4154` n `107` status `ready` deltaP `-2.9674` edge `0.002` maxDD `-0.1712`
- `market_context_high->index_1h` score `-0.5759` n `107` status `ready` deltaP `-0.4267` edge `-0.0058` maxDD `-1.2155`
- `market_context_high->fx_4h` score `-0.6164` n `95` status `ready` deltaP `-3.5976` edge `0.0048` maxDD `-0.4541`
- `market_context_high->crypto_major_24h` score `-0.6442` n `45` status `ready` deltaP `8.9236` edge `0.0551` maxDD `-11.1077`
- `market_context_high->fx_24h` score `-0.8333` n `45` status `ready` deltaP `0.9028` edge `0.0011` maxDD `-1.1249`
- `market_context_high->metal_1h` score `-0.8552` n `107` status `ready` deltaP `1.9685` edge `-0.0052` maxDD `-1.6682`
- `market_context_high->crypto_major_1h` score `-0.9949` n `107` status `ready` deltaP `6.1839` edge `-0.0107` maxDD `-9.3126`
- `market_context_high->crypto_alt_24h` score `-1.1279` n `45` status `ready` deltaP `13.9583` edge `0.1503` maxDD `-27.037`
- `market_context_high->equity_1h` score `-2.444` n `107` status `ready` deltaP `0.4351` edge `-0.0889` maxDD `-12.1865`
- `market_context_high->metal_4h` score `-2.5315` n `95` status `ready` deltaP `-1.1007` edge `-0.0282` maxDD `-5.7003`
- `market_context_high->crypto_alt_1h` score `-2.642` n `107` status `ready` deltaP `0.5079` edge `-0.0445` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-2.7296` n `45` status `ready` deltaP `-7.743` edge `-0.0096` maxDD `-6.6329`
- `market_context_high->index_4h` score `-4.0342` n `95` status `ready` deltaP `-14.4721` edge `-0.0472` maxDD `-4.7338`
- `market_context_high->index_24h` score `-7.0536` n `45` status `ready` deltaP `-35.6597` edge `-0.1881` maxDD `-5.9574`
- `market_context_high->crypto_major_4h` score `-10.4881` n `95` status `ready` deltaP `-14.6245` edge `-0.2261` maxDD `-37.3663`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
