# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T20:37:27.930346+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11754`

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

- `news_risk_high->unknown_24h` score `4436.5068` n `85` status `ready` deltaP `1.2153` edge `369.7008` maxDD `0.0`
- `market_context_high->unknown_1h` score `68.419` n `46` status `ready` deltaP `10.2512` edge `5.6379` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `47.9047` n `46` status `ready` deltaP `22.7355` edge `3.8756` maxDD `-2.4756`
- `market_context_high->equity_24h` score `26.2528` n `46` status `ready` deltaP `33.4994` edge `1.9958` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `25.923` n `46` status `ready` deltaP `14.84` edge `2.0993` maxDD `-2.7051`
- `market_context_high->index_24h` score `7.1027` n `46` status `ready` deltaP `27.9439` edge `0.4144` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.3984` n `46` status `ready` deltaP `28.8648` edge `0.1146` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.0885` n `46` status `ready` deltaP `35.2067` edge `0.0339` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.8532` n `46` status `ready` deltaP `18.1602` edge `0.1585` maxDD `-1.3444`
- `news_risk_high->index_24h` score `2.055` n `85` status `ready` deltaP `24.0564` edge `0.0679` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.4154` n `85` status `ready` deltaP `30.4249` edge `0.1434` maxDD `-6.8481`
- `market_context_high->equity_1h` score `1.2372` n `46` status `ready` deltaP `14.0979` edge `0.0494` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `0.8981` n `46` status `ready` deltaP `8.4769` edge `0.0851` maxDD `-3.3417`
- `news_risk_high->crypto_alt_24h` score `0.8597` n `85` status `ready` deltaP `8.7786` edge `0.4083` maxDD `-29.2814`
- `market_context_high->crypto_major_1h` score `0.8064` n `46` status `ready` deltaP `7.3484` edge `0.0958` maxDD `-4.5405`
- `market_context_high->index_1h` score `0.7709` n `46` status `ready` deltaP `12.3731` edge `0.0096` maxDD `-0.2275`
- `market_context_high->crypto_major_4h` score `0.6861` n `46` status `ready` deltaP `6.1837` edge `0.1064` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.3142` n `46` status `ready` deltaP `8.24` edge `0.0069` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.132` n `46` status `ready` deltaP `4.7904` edge `0.0107` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0447` n `139` status `ready` deltaP `3.2708` edge `0.0036` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
