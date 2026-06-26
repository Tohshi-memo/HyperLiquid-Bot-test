# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T05:37:30.772042+00:00`
- Price records: `672`
- Market context records: `4797`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7548`

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

- `market_context_high->unknown_4h` score `7.7823` n `122` status `ready` deltaP `19.3298` edge `0.6407` maxDD `-4.6834`
- `market_context_high->unknown_1h` score `2.6917` n `122` status `ready` deltaP `12.2804` edge `0.1842` maxDD `-1.674`
- `market_context_high->unknown_24h` score `2.3651` n `114` status `ready` deltaP `13.4137` edge `0.2` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `0.077` n `122` status `ready` deltaP `5.3818` edge `0.0293` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `0.0472` n `122` status `ready` deltaP `11.8153` edge `0.0445` maxDD `-4.377`
- `market_context_high->equity_4h` score `0.0225` n `122` status `ready` deltaP `8.9964` edge `0.1115` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.2962` n `122` status `ready` deltaP `7.7569` edge `0.0172` maxDD `-5.5505`
- `market_context_high->fx_4h` score `-0.4068` n `122` status `ready` deltaP `3.4311` edge `0.0026` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.6779` n `122` status `ready` deltaP `1.8676` edge `0.0078` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-0.8717` n `122` status `ready` deltaP `-0.7338` edge `-0.0028` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.3476` n `122` status `ready` deltaP `-1.0479` edge `-0.0049` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.0817` n `114` status `ready` deltaP `20.2485` edge `0.109` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.2151` n `122` status `ready` deltaP `-0.4982` edge `-0.0631` maxDD `-14.0715`
- `market_context_high->crypto_alt_1h` score `-3.0692` n `122` status `ready` deltaP `1.3473` edge `-0.0408` maxDD `-15.2495`
- `market_context_high->fx_24h` score `-3.161` n `114` status `ready` deltaP `-13.3132` edge `-0.0197` maxDD `-3.3968`
- `market_context_high->crypto_major_1h` score `-4.4096` n `122` status `ready` deltaP `1.1338` edge `-0.066` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-4.6755` n `122` status `ready` deltaP `5.5078` edge `0.0063` maxDD `-46.0617`
- `market_context_high->index_24h` score `-6.8863` n `114` status `ready` deltaP `-8.4887` edge `-0.1283` maxDD `-23.1172`
- `market_context_high->crypto_major_4h` score `-7.9704` n `122` status `ready` deltaP `4.2683` edge `-0.1272` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.2317` n `122` status `ready` deltaP `7.1447` edge `-0.2789` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
