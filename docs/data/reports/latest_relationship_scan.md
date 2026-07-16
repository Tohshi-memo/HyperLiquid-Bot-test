# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T17:37:28.787240+00:00`
- Price records: `672`
- Market context records: `6941`
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
- `market_context_high->crypto_alt_1h` score `-0.5808` n `236` status `ready` deltaP `2.3648` edge `0.0186` maxDD `-4.2882`
- `market_context_high->index_1h` score `-0.7341` n `236` status `ready` deltaP `-0.3451` edge `-0.0007` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.742` n `236` status `ready` deltaP `-2.5119` edge `-0.0016` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.8358` n `225` status `ready` deltaP `13.4438` edge `0.0096` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.1406` n `236` status `ready` deltaP `2.8139` edge `0.0119` maxDD `-6.7235`
- `market_context_high->unknown_24h` score `-1.1903` n `218` status `ready` deltaP `-7.9055` edge `0.3283` maxDD `-16.5894`
- `market_context_high->commodity_1h` score `-1.2652` n `236` status `ready` deltaP `-2.7428` edge `-0.015` maxDD `-2.4388`
- `market_context_high->commodity_4h` score `-1.6045` n `225` status `ready` deltaP `-4.0976` edge `-0.0294` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.6162` n `225` status `ready` deltaP `9.1755` edge `-0.0104` maxDD `-11.3047`
- `market_context_high->unknown_1h` score `-1.6484` n `236` status `ready` deltaP `-2.5145` edge `-0.0305` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.9496` n `236` status `ready` deltaP `2.2962` edge `-0.0182` maxDD `-15.4311`
- `market_context_high->metal_4h` score `-1.9602` n `225` status `ready` deltaP `5.0271` edge `0.0135` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.7593` n `225` status `ready` deltaP `-0.0204` edge `-0.0209` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-2.7684` n `225` status `ready` deltaP `1.6694` edge `-0.0077` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-2.9979` n `225` status `ready` deltaP `-7.6599` edge `0.0378` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.4852` n `218` status `ready` deltaP `-4.7263` edge `-0.0721` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.2689` n `218` status `ready` deltaP `-6.1518` edge `-0.0111` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.4581` n `225` status `ready` deltaP `5.9891` edge `-0.0734` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.9491` n `218` status `ready` deltaP `-13.5111` edge `-0.1189` maxDD `-34.7346`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
