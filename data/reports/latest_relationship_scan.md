# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T08:52:29.398003+00:00`
- Price records: `672`
- Market context records: `5232`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5602`

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

- `market_context_high->unknown_24h` score `22.3459` n `123` status `ready` deltaP `32.1647` edge `1.6667` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `13.366` n `123` status `ready` deltaP `32.7744` edge `1.2615` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `7.4787` n `123` status `ready` deltaP `23.5391` edge `0.805` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.0337` n `155` status `ready` deltaP `13.3891` edge `0.4068` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.9478` n `155` status `ready` deltaP `14.3745` edge `0.4624` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `2.1648` n `155` status `ready` deltaP `16.9827` edge `0.1694` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `1.8094` n `155` status `ready` deltaP `8.0896` edge `0.161` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.5656` n `123` status `ready` deltaP `13.3003` edge `0.048` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4688` n `155` status `ready` deltaP `4.803` edge `0.1032` maxDD `-5.0257`
- `market_context_high->equity_24h` score `0.452` n `123` status `ready` deltaP `17.2553` edge `0.5058` maxDD `-40.0306`
- `market_context_high->crypto_major_1h` score `0.4372` n `155` status `ready` deltaP `6.8524` edge `0.1153` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.0759` n `155` status `ready` deltaP `6.1782` edge `0.129` maxDD `-7.4425`
- `market_context_high->equity_1h` score `-0.1755` n `155` status `ready` deltaP `5.3699` edge `0.0461` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.1885` n `155` status `ready` deltaP `3.6623` edge `0.0106` maxDD `-2.0682`
- `market_context_high->index_24h` score `-0.2109` n `123` status `ready` deltaP `16.3279` edge `0.0276` maxDD `-7.413`
- `market_context_high->index_1h` score `-0.2182` n `155` status `ready` deltaP `3.5378` edge `0.0086` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.3188` n `155` status `ready` deltaP `0.7611` edge `-0.0007` maxDD `-0.6194`
- `market_context_high->commodity_1h` score `-0.6577` n `155` status `ready` deltaP `-0.1729` edge `-0.0023` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.7109` n `155` status `ready` deltaP `1.3572` edge `0.0032` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.8971` n `155` status `ready` deltaP `3.1619` edge `0.0159` maxDD `-2.9391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
