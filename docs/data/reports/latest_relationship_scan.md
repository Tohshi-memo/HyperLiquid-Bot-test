# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T17:22:28.701237+00:00`
- Price records: `672`
- Market context records: `6940`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11728`

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

- `market_context_high->fx_1h` score `-0.2462` n `236` status `ready` deltaP `2.2709` edge `0.0018` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.6012` n `236` status `ready` deltaP `2.2151` edge `0.0179` maxDD `-4.2882`
- `market_context_high->index_1h` score `-0.7427` n `236` status `ready` deltaP `-0.4948` edge `-0.0008` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7436` n `236` status `ready` deltaP `-2.5119` edge `-0.0018` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.8358` n `225` status `ready` deltaP `13.4438` edge `0.0096` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.167` n `236` status `ready` deltaP `2.6642` edge `0.0107` maxDD `-6.7235`
- `market_context_high->unknown_24h` score `-1.1903` n `218` status `ready` deltaP `-7.9055` edge `0.3283` maxDD `-16.5894`
- `market_context_high->commodity_1h` score `-1.264` n `236` status `ready` deltaP `-2.7428` edge `-0.0149` maxDD `-2.4388`
- `market_context_high->commodity_4h` score `-1.6091` n `225` status `ready` deltaP `-4.0976` edge `-0.03` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.6265` n `225` status `ready` deltaP `9.023` edge `-0.0107` maxDD `-11.3047`
- `market_context_high->unknown_1h` score `-1.6328` n `236` status `ready` deltaP `-2.3648` edge `-0.0302` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-1.9586` n `225` status `ready` deltaP `5.0271` edge `0.0137` maxDD `-5.5324`
- `market_context_high->equity_1h` score `-1.9636` n `236` status `ready` deltaP `2.1465` edge `-0.019` maxDD `-15.4311`
- `market_context_high->crypto_major_4h` score `-2.7844` n `225` status `ready` deltaP `-0.1728` edge `-0.0231` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-2.7864` n `225` status `ready` deltaP `1.5169` edge `-0.009` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.0161` n `225` status `ready` deltaP `-7.8123` edge `0.0373` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.4804` n `218` status `ready` deltaP `-4.7263` edge `-0.0717` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.2689` n `218` status `ready` deltaP `-6.1518` edge `-0.0111` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.476` n `225` status `ready` deltaP `5.9891` edge `-0.0757` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.9546` n `218` status `ready` deltaP `-13.5111` edge `-0.1196` maxDD `-34.7346`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
