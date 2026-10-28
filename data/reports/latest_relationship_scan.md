# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T17:37:40.991941+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8562`

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

- `market_context_high->unknown_24h` score `1252.4338` n `146` status `ready` deltaP `-2.3664` edge `104.478` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.9084` n `149` status `ready` deltaP `4.385` edge `1.8117` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.5183` n `146` status `ready` deltaP `24.7074` edge `0.0306` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1865` n `149` status `ready` deltaP `7.4187` edge `0.0019` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.0917` n `149` status `ready` deltaP `8.327` edge `0.0074` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.1126` n `149` status `ready` deltaP `6.9242` edge `0.0043` maxDD `-0.4545`
- `market_context_high->crypto_major_1h` score `-0.2977` n `149` status `ready` deltaP `7.2791` edge `0.0416` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.427` n `149` status `ready` deltaP `7.049` edge `0.0393` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.4362` n `146` status `ready` deltaP `13.6772` edge `0.0297` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.6476` n `149` status `ready` deltaP `-0.3406` edge `0.0067` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7352` n `149` status `ready` deltaP `-3.4743` edge `-0.0028` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7411` n `149` status `ready` deltaP `9.0563` edge `-0.0013` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.3992` n `149` status `ready` deltaP `1.0891` edge `0.0046` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.4988` n `149` status `ready` deltaP `3.4943` edge `0.0209` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.6708` n `146` status `ready` deltaP `7.0443` edge `0.0269` maxDD `-15.7143`
- `market_context_high->index_4h` score `-3.0614` n `149` status `ready` deltaP `-9.484` edge `-0.0297` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.2037` n `146` status `ready` deltaP `0.8681` edge `0.0692` maxDD `-29.1905`
- `market_context_high->metal_24h` score `-3.2572` n `146` status `ready` deltaP `0.6541` edge `0.0219` maxDD `-9.8155`
- `market_context_high->crypto_major_4h` score `-3.3593` n `149` status `ready` deltaP `4.119` edge `-0.0262` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.3401` n `149` status `ready` deltaP `-3.1725` edge `-0.1401` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
