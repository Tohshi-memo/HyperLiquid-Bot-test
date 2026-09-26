# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T14:52:25.764173+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11838`

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

- `news_risk_high->unknown_24h` score `4384.9766` n `85` status `ready` deltaP `0.3472` edge `365.4124` maxDD `0.0`
- `market_context_high->unknown_1h` score `68.9506` n `47` status `ready` deltaP `8.1698` edge `5.6985` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `46.837` n `47` status `ready` deltaP `22.0892` edge `3.7951` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `26.4971` n `47` status `ready` deltaP `16.7959` edge `2.1341` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.554` n `47` status `ready` deltaP `32.6795` edge `1.9472` maxDD `-2.1786`
- `market_context_high->index_24h` score `6.8894` n `47` status `ready` deltaP `27.2976` edge `0.4051` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.281` n `47` status `ready` deltaP `27.5931` edge `0.1133` maxDD `-0.2401`
- `market_context_high->index_4h` score `2.7699` n `47` status `ready` deltaP `32.0446` edge `0.0326` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.7363` n `47` status `ready` deltaP `17.4494` edge `0.1535` maxDD `-1.3444`
- `news_risk_high->crypto_alt_24h` score `2.2581` n `85` status `ready` deltaP `10.6883` edge `0.5121` maxDD `-29.2814`
- `news_risk_high->index_24h` score `2.1841` n `85` status `ready` deltaP `25.4453` edge `0.0694` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.4366` n `85` status `ready` deltaP `30.7721` edge `0.1438` maxDD `-6.8481`
- `market_context_high->crypto_alt_4h` score `1.2324` n `47` status `ready` deltaP `10.4502` edge `0.0998` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0374` n `47` status `ready` deltaP `11.9155` edge `0.0473` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.8193` n `47` status `ready` deltaP `12.9634` edge `0.0097` maxDD `-0.2275`
- `market_context_high->crypto_major_4h` score `0.7911` n `47` status `ready` deltaP `6.6716` edge `0.1119` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.4578` n `47` status `ready` deltaP `9.9598` edge `0.0074` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.4441` n `47` status `ready` deltaP `5.9498` edge `0.0791` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.0445` n `47` status `ready` deltaP `4.026` edge `0.0105` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0591` n `139` status `ready` deltaP `3.1211` edge `0.0034` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
