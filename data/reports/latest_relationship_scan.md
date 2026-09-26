# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T18:37:27.073766+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11744`

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

- `news_risk_high->unknown_24h` score `4433.9412` n `85` status `ready` deltaP `1.2153` edge `369.487` maxDD `0.0`
- `market_context_high->unknown_1h` score `69.7977` n `47` status `ready` deltaP `8.4693` edge `5.7671` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `46.3179` n `47` status `ready` deltaP `20.7003` edge `3.7611` maxDD `-2.4756`
- `market_context_high->equity_24h` score `25.4895` n `47` status `ready` deltaP `32.1587` edge `1.9453` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `25.2542` n `47` status `ready` deltaP `15.0598` edge `2.0421` maxDD `-2.7051`
- `market_context_high->index_24h` score `6.7615` n `47` status `ready` deltaP `25.9087` edge `0.4037` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.2473` n `47` status `ready` deltaP `27.2459` edge `0.1128` maxDD `-0.2401`
- `market_context_high->index_4h` score `2.7833` n `47` status `ready` deltaP `32.1971` edge `0.0327` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.7387` n `47` status `ready` deltaP `17.4494` edge `0.1537` maxDD `-1.3444`
- `news_risk_high->index_24h` score `2.0562` n `85` status `ready` deltaP `24.0564` edge `0.068` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.4146` n `85` status `ready` deltaP `30.4249` edge `0.1433` maxDD `-6.8481`
- `market_context_high->equity_1h` score `1.0745` n `47` status `ready` deltaP `12.3646` edge `0.0474` maxDD `-1.5564`
- `news_risk_high->crypto_alt_24h` score `1.0152` n `85` status `ready` deltaP `8.9522` edge `0.4201` maxDD `-29.2814`
- `market_context_high->index_1h` score `0.8325` n `47` status `ready` deltaP `13.1131` edge `0.0098` maxDD `-0.2275`
- `market_context_high->crypto_alt_4h` score `0.7696` n `47` status `ready` deltaP `8.9258` edge `0.0714` maxDD `-3.3417`
- `market_context_high->crypto_major_1h` score `0.4393` n `47` status `ready` deltaP `6.0995` edge `0.0777` maxDD `-4.5405`
- `market_context_high->fx_1h` score `0.4218` n `47` status `ready` deltaP `9.5107` edge `0.0074` maxDD `-0.1854`
- `market_context_high->crypto_major_4h` score `0.4144` n `47` status `ready` deltaP `4.8423` edge `0.0927` maxDD `-5.2359`
- `market_context_high->metal_1h` score `0.0445` n `47` status `ready` deltaP `4.026` edge `0.0105` maxDD `-0.1976`
- `news_risk_high->index_1h` score `-0.0459` n `139` status `ready` deltaP `3.2708` edge `0.0035` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
