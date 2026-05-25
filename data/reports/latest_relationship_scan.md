# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T16:52:15.748400+00:00`
- Price records: `672`
- Market context records: `1860`
- Flow alert records: `7256`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4500`

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

- `market_context_high->crypto_alt_4h` score `6.5119` n `199` status `ready` deltaP `21.2893` edge `0.5152` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.0356` n `199` status `ready` deltaP `24.9709` edge `0.4611` maxDD `-4.9684`
- `market_context_high->metal_24h` score `5.0628` n `178` status `ready` deltaP `22.035` edge `0.5176` maxDD `-12.7414`
- `market_context_high->unknown_4h` score `4.145` n `199` status `ready` deltaP `16.8909` edge `0.4352` maxDD `-9.8581`
- `market_context_high->index_24h` score `2.5069` n `178` status `ready` deltaP `13.7017` edge `0.2404` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `2.2213` n `178` status `ready` deltaP `12.9975` edge `0.6305` maxDD `-35.8966`
- `market_context_high->equity_4h` score `2.13` n `199` status `ready` deltaP `13.9723` edge `0.1938` maxDD `-5.0894`
- `market_context_high->index_4h` score `0.3993` n `199` status `ready` deltaP `9.9407` edge `0.0759` maxDD `-3.7119`
- `market_context_high->equity_24h` score `0.3787` n `178` status `ready` deltaP `10.68` edge `0.4502` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `0.2796` n `199` status `ready` deltaP `5.1478` edge `0.0876` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.1939` n `178` status `ready` deltaP `19.2065` edge `0.7467` maxDD `-62.3533`
- `market_context_high->fx_24h` score `0.1648` n `178` status `ready` deltaP `13.8655` edge `0.0262` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `0.0231` n `199` status `ready` deltaP `4.5595` edge `0.0829` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.2211` n `199` status `ready` deltaP `4.2383` edge `0.0327` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.5169` n `199` status `ready` deltaP `3.2874` edge `0.0302` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.578` n `199` status `ready` deltaP `5.8323` edge `0.0206` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6581` n `199` status `ready` deltaP `-3.2024` edge `0.0002` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-0.6624` n `199` status `ready` deltaP `12.238` edge `0.1324` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.7392` n `199` status `ready` deltaP `-1.0539` edge `0.0086` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-0.9891` n `199` status `ready` deltaP `-5.0389` edge `-0.0044` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
