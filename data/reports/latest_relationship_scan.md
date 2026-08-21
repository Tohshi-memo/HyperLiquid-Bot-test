# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T12:52:23.910490+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13758`

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

- `market_context_high->index_1h` score `0.4696` n `120` status `ready` deltaP `12.1357` edge `0.007` maxDD `-0.5685`
- `market_context_high->equity_1h` score `0.3902` n `120` status `ready` deltaP `9.0769` edge `0.0535` maxDD `-3.1861`
- `market_context_high->fx_4h` score `0.2198` n `108` status `ready` deltaP `10.3264` edge `0.0096` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.025` n `120` status `ready` deltaP `4.1667` edge `0.0049` maxDD `-0.2043`
- `market_context_high->equity_4h` score `-0.0942` n `108` status `ready` deltaP `4.274` edge `0.1266` maxDD `-8.3685`
- `market_context_high->index_4h` score `-0.2925` n `108` status `ready` deltaP `5.7306` edge `0.0167` maxDD `-1.7252`
- `market_context_high->metal_4h` score `-0.3408` n `108` status `ready` deltaP `5.1886` edge `-0.0207` maxDD `-1.273`
- `market_context_high->metal_1h` score `-0.4552` n `120` status `ready` deltaP `1.003` edge `-0.005` maxDD `-0.503`
- `market_context_high->commodity_24h` score `-0.4607` n `105` status `ready` deltaP `4.4147` edge `0.1155` maxDD `-4.666`
- `market_context_high->unknown_1h` score `-0.5714` n `120` status `ready` deltaP `9.7356` edge `-0.0898` maxDD `-0.4843`
- `market_context_high->commodity_1h` score `-0.6568` n `120` status `ready` deltaP `-4.2764` edge `0.0009` maxDD `-1.1941`
- `market_context_high->commodity_4h` score `-0.704` n `108` status `ready` deltaP `-1.9987` edge `0.0081` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-1.0102` n `120` status `ready` deltaP `-0.9481` edge `0.0023` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.5312` n `120` status `ready` deltaP `-3.8722` edge `-0.068` maxDD `-4.1996`
- `market_context_high->fx_24h` score `-3.0687` n `105` status `ready` deltaP `-12.9961` edge `-0.0081` maxDD `-2.2121`
- `market_context_high->crypto_alt_4h` score `-3.3968` n `108` status `ready` deltaP `-1.0162` edge `-0.1493` maxDD `-5.4926`
- `market_context_high->index_24h` score `-4.1477` n `105` status `ready` deltaP `-5.0744` edge `-0.0477` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-4.4116` n `108` status `ready` deltaP `-1.6711` edge `-0.2544` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-4.4497` n `105` status `ready` deltaP `-16.7212` edge `-0.1282` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-4.8116` n `105` status `ready` deltaP `8.8145` edge `-0.4091` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
