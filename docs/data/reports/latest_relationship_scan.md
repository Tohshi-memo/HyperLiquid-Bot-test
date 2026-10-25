# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T03:37:23.980455+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7692`

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

- `market_context_high->unknown_4h` score `52.4901` n `95` status `ready` deltaP `0.8408` edge `4.4021` maxDD `-1.016`
- `market_context_high->unknown_1h` score `17.4711` n `107` status `ready` deltaP `2.9423` edge `1.4852` maxDD `-1.5781`
- `market_context_high->commodity_24h` score `1.2843` n `44` status `ready` deltaP `17.3137` edge `0.0825` maxDD `-3.6055`
- `market_context_high->commodity_1h` score `-0.2894` n `107` status `ready` deltaP `2.3323` edge `0.0104` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.3085` n `95` status `ready` deltaP `2.0876` edge `0.0416` maxDD `-1.165`
- `market_context_high->fx_1h` score `-0.3716` n `107` status `ready` deltaP `-2.1826` edge `0.0022` maxDD `-0.1569`
- `market_context_high->crypto_alt_24h` score `-0.4818` n `44` status `ready` deltaP `15.3725` edge `0.1958` maxDD `-25.138`
- `market_context_high->crypto_major_24h` score `-0.5282` n `44` status `ready` deltaP `10.3378` edge `0.0604` maxDD `-11.0959`
- `market_context_high->index_1h` score `-0.5336` n `107` status `ready` deltaP `0.3582` edge `-0.0056` maxDD `-1.2155`
- `market_context_high->fx_4h` score `-0.6133` n `95` status `ready` deltaP `-3.5976` edge `0.0052` maxDD `-0.4541`
- `market_context_high->fx_24h` score `-0.7599` n `44` status `ready` deltaP `1.6099` edge `0.0018` maxDD `-1.0685`
- `market_context_high->metal_1h` score `-0.8539` n `107` status `ready` deltaP `1.9685` edge `-0.0051` maxDD `-1.6682`
- `market_context_high->crypto_major_1h` score `-0.9801` n `107` status `ready` deltaP `6.1839` edge `-0.0088` maxDD `-9.3126`
- `market_context_high->equity_1h` score `-2.3938` n `107` status `ready` deltaP `1.22` edge `-0.0877` maxDD `-12.1865`
- `market_context_high->metal_4h` score `-2.4503` n `95` status `ready` deltaP `-0.2006` edge `-0.0279` maxDD `-5.6627`
- `market_context_high->crypto_alt_1h` score `-2.5012` n `107` status `ready` deltaP `1.2927` edge `-0.038` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-2.6721` n `44` status `ready` deltaP `-7.339` edge `-0.0121` maxDD `-6.5985`
- `market_context_high->index_4h` score `-3.9474` n `95` status `ready` deltaP `-13.5719` edge `-0.0466` maxDD `-4.6831`
- `market_context_high->crypto_major_4h` score `-6.664` n `95` status `ready` deltaP `-13.7243` edge `-0.2193` maxDD `-36.8186`
- `market_context_high->index_24h` score `-6.9945` n `44` status `ready` deltaP `-35.3062` edge `-0.1902` maxDD `-5.9176`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
