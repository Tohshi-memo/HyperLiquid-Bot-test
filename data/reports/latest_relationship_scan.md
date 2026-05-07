# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T02:37:12.797684+00:00`
- Price records: `510`
- Market context records: `605`
- Flow alert records: `1709`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `4.7731` n `146` status `ready` deltaP `7.0446` edge `0.3556` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.9908` n `146` status `ready` deltaP `11.8291` edge `0.2871` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0064` n `146` status `ready` deltaP `10.4641` edge `0.0182` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3137` n `146` status `ready` deltaP `2.0684` edge `0.0038` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5957` n `146` status `ready` deltaP `1.5309` edge `0.0376` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6564` n `146` status `ready` deltaP `0.6003` edge `-0.0028` maxDD `-2.8282`
- `market_context_high->crypto_alt_1h` score `-1.0562` n `146` status `ready` deltaP `6.0832` edge `0.0029` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.0976` n `146` status `ready` deltaP `-3.6493` edge `-0.0068` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.2248` n `146` status `ready` deltaP `-1.7901` edge `-0.0091` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.6827` n `146` status `ready` deltaP `5.6364` edge `-0.0055` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.7636` n `146` status `ready` deltaP `4.3065` edge `0.0813` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2228` n `146` status `ready` deltaP `0.1705` edge `-0.0341` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.5057` n `146` status `ready` deltaP `13.6182` edge `0.071` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.5427` n `146` status `ready` deltaP `-7.1066` edge `0.035` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.1997` n `146` status `ready` deltaP `-3.0948` edge `-0.0308` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3376` n `146` status `ready` deltaP `-4.7702` edge `-0.0504` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7857` n `146` status `ready` deltaP `-7.182` edge `0.0825` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.2969` n `146` status `ready` deltaP `-2.9402` edge `-0.0141` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.5945` n `146` status `ready` deltaP `-10.7551` edge `-0.0507` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.9238` n `146` status `ready` deltaP `1.3504` edge `-0.2315` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
