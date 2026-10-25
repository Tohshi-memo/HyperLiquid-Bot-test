# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T02:52:28.757727+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7628`

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

- `market_context_high->unknown_4h` score `53.6133` n `95` status `ready` deltaP `0.8408` edge `4.4957` maxDD `-1.016`
- `market_context_high->unknown_1h` score `17.3267` n `107` status `ready` deltaP `2.1574` edge `1.4784` maxDD `-1.5781`
- `market_context_high->commodity_24h` score `1.4672` n `47` status `ready` deltaP `19.3447` edge `0.0842` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.0863` n `95` status `ready` deltaP `4.7882` edge `0.044` maxDD `-1.165`
- `market_context_high->commodity_1h` score `-0.357` n `107` status `ready` deltaP `1.5474` edge `0.01` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.3746` n `107` status `ready` deltaP `-2.1826` edge `0.002` maxDD `-0.1712`
- `market_context_high->index_1h` score `-0.6207` n `107` status `ready` deltaP `-1.2116` edge `-0.0063` maxDD `-1.2155`
- `market_context_high->fx_4h` score `-0.6663` n `95` status `ready` deltaP `-4.4977` edge `0.0044` maxDD `-0.4541`
- `market_context_high->crypto_major_24h` score `-0.8395` n `47` status `ready` deltaP `8.2299` edge `0.039` maxDD `-11.4533`
- `market_context_high->metal_1h` score `-0.8577` n `107` status `ready` deltaP `1.9685` edge `-0.0054` maxDD `-1.6693`
- `market_context_high->fx_24h` score `-0.9627` n `47` status `ready` deltaP `-0.4211` edge `0.0003` maxDD `-1.2171`
- `market_context_high->crypto_major_1h` score `-1.0864` n `107` status `ready` deltaP `5.399` edge `-0.0172` maxDD `-9.3126`
- `market_context_high->crypto_alt_24h` score `-2.4879` n `47` status `ready` deltaP `11.3106` edge `0.0557` maxDD `-31.3384`
- `market_context_high->equity_1h` score `-2.4981` n `107` status `ready` deltaP `-0.3498` edge `-0.0906` maxDD `-12.1865`
- `market_context_high->metal_4h` score `-2.7001` n `95` status `ready` deltaP `-2.9012` edge `-0.0292` maxDD `-5.784`
- `market_context_high->metal_24h` score `-2.8594` n `47` status `ready` deltaP `-8.4995` edge `-0.0057` maxDD `-6.74`
- `market_context_high->crypto_alt_1h` score `-3.0299` n `107` status `ready` deltaP `-0.277` edge `-0.0555` maxDD `-12.6114`
- `market_context_high->index_4h` score `-4.2173` n `95` status `ready` deltaP `-16.2725` edge `-0.0487` maxDD `-4.8739`
- `market_context_high->index_24h` score `-7.1816` n `47` status `ready` deltaP `-36.1481` edge `-0.1854` maxDD `-6.0996`
- `market_context_high->crypto_major_4h` score `-11.1558` n `95` status `ready` deltaP `-16.4249` edge `-0.2523` maxDD `-38.7612`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
