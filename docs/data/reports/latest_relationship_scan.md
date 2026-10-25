# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T04:37:37.786009+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7734`

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

- `market_context_high->unknown_4h` score `52.0221` n `95` status `ready` deltaP `-0.0593` edge `4.3691` maxDD `-1.016`
- `market_context_high->unknown_1h` score `18.2386` n `107` status `ready` deltaP `4.512` edge `1.5387` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `3.1939` n `40` status `ready` deltaP `21.7361` edge `0.3801` maxDD `-18.3748`
- `market_context_high->commodity_24h` score `0.6721` n `40` status `ready` deltaP `14.3056` edge `0.0817` maxDD `-3.6055`
- `market_context_high->fx_1h` score `-0.243` n `107` status `ready` deltaP `0.1721` edge `0.0026` maxDD `-0.1258`
- `market_context_high->crypto_major_24h` score `-0.3818` n `40` status `ready` deltaP `11.5278` edge `0.0833` maxDD `-11.0243`
- `market_context_high->commodity_1h` score `-0.4438` n `107` status `ready` deltaP `0.7625` edge `0.008` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.4601` n `40` status `ready` deltaP `4.7917` edge `0.0039` maxDD `-0.9352`
- `market_context_high->fx_4h` score `-0.4628` n `95` status `ready` deltaP `-0.897` edge `0.0065` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.4711` n `107` status `ready` deltaP `3.5382` edge `-0.0048` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.4889` n `107` status `ready` deltaP `1.143` edge `-0.0051` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.8386` n `95` status `ready` deltaP `-1.5132` edge `0.0381` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.0593` n `107` status `ready` deltaP `4.6141` edge `-0.0085` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.1837` n `95` status `ready` deltaP `2.5` edge `-0.0259` maxDD `-5.4859`
- `market_context_high->equity_1h` score `-2.3436` n `107` status `ready` deltaP `2.0049` edge `-0.0865` maxDD `-12.1865`
- `market_context_high->crypto_alt_1h` score `-2.3928` n `107` status `ready` deltaP `2.0776` edge `-0.0342` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-2.4456` n `40` status `ready` deltaP `-5.5208` edge `-0.0236` maxDD `-6.4717`
- `market_context_high->index_4h` score `-3.5895` n `95` status `ready` deltaP `-9.9712` edge `-0.0435` maxDD `-4.4653`
- `market_context_high->crypto_major_4h` score `-6.0466` n `95` status `ready` deltaP `-10.1236` edge `-0.1899` maxDD `-34.7582`
- `market_context_high->index_24h` score `-6.7816` n `40` status `ready` deltaP `-34.4097` edge `-0.198` maxDD `-5.6853`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
