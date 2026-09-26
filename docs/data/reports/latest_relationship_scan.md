# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T14:37:28.272474+00:00`
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

- `news_risk_high->unknown_24h` score `4384.9838` n `85` status `ready` deltaP `0.3472` edge `365.413` maxDD `0.0`
- `market_context_high->unknown_1h` score `69.1882` n `47` status `ready` deltaP `8.1698` edge `5.7183` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `46.9061` n `47` status `ready` deltaP `22.2628` edge `3.7997` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `26.6274` n `47` status `ready` deltaP `16.9695` edge `2.1438` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.5823` n `47` status `ready` deltaP `32.8531` edge `1.9484` maxDD `-2.1786`
- `market_context_high->index_24h` score `6.9069` n `47` status `ready` deltaP `27.4712` edge `0.4054` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.2997` n `47` status `ready` deltaP `27.7667` edge `0.1137` maxDD `-0.2401`
- `market_context_high->index_4h` score `2.7699` n `47` status `ready` deltaP `32.0446` edge `0.0326` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.7375` n `47` status `ready` deltaP `17.4494` edge `0.1536` maxDD `-1.3444`
- `news_risk_high->crypto_alt_24h` score `2.3883` n `85` status `ready` deltaP `10.8619` edge `0.5218` maxDD `-29.2814`
- `news_risk_high->index_24h` score `2.2016` n `85` status `ready` deltaP `25.6189` edge `0.0697` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.4487` n `85` status `ready` deltaP `30.9457` edge `0.1442` maxDD `-6.8481`
- `market_context_high->crypto_alt_4h` score `1.2554` n `47` status `ready` deltaP `10.6026` edge `0.1007` maxDD `-3.3417`
- `market_context_high->equity_1h` score `1.0506` n `47` status `ready` deltaP `12.0652` edge `0.0474` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.8193` n `47` status `ready` deltaP `12.9634` edge `0.0097` maxDD `-0.2275`
- `market_context_high->crypto_major_4h` score `0.8093` n `47` status `ready` deltaP `6.8241` edge `0.1124` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.4698` n `47` status `ready` deltaP `10.1095` edge `0.0074` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.4489` n `47` status `ready` deltaP `5.9498` edge `0.0795` maxDD `-4.5405`
- `market_context_high->metal_1h` score `0.0531` n `47` status `ready` deltaP `4.1757` edge `0.0106` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0591` n `139` status `ready` deltaP `3.1211` edge `0.0034` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
