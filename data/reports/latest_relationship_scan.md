# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T14:52:25.741238+00:00`
- Price records: `672`
- Market context records: `7575`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14512`

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

- `market_context_high->commodity_4h` score `0.2401` n `166` status `ready` deltaP `9.797` edge `0.0307` maxDD `-2.4139`
- `market_context_high->index_1h` score `-0.0667` n `166` status `ready` deltaP `5.4126` edge `0.0082` maxDD `-1.2267`
- `market_context_high->commodity_24h` score `-0.1462` n `155` status `ready` deltaP `12.7144` edge `0.0614` maxDD `-7.0012`
- `market_context_high->commodity_1h` score `-0.28` n `166` status `ready` deltaP `4.6781` edge `0.0027` maxDD `-1.5775`
- `market_context_high->index_4h` score `-0.4613` n `166` status `ready` deltaP `11.4735` edge `0.037` maxDD `-3.4775`
- `market_context_high->fx_1h` score `-0.4648` n `166` status `ready` deltaP `1.6499` edge `0.0002` maxDD `-0.6615`
- `market_context_high->crypto_alt_1h` score `-0.7479` n `166` status `ready` deltaP `-0.606` edge `0.0023` maxDD `-5.1979`
- `market_context_high->metal_1h` score `-0.8152` n `166` status `ready` deltaP `-0.6205` edge `0.0094` maxDD `-1.4491`
- `market_context_high->crypto_major_1h` score `-0.8186` n `166` status `ready` deltaP `4.6696` edge `0.0036` maxDD `-7.5081`
- `market_context_high->fx_24h` score `-0.9314` n `155` status `ready` deltaP `7.7565` edge `0.0147` maxDD `-3.8554`
- `market_context_high->unknown_24h` score `-1.0969` n `156` status `ready` deltaP `6.4503` edge `0.0804` maxDD `-9.7887`
- `market_context_high->equity_1h` score `-1.2183` n `166` status `ready` deltaP `3.9057` edge `0.027` maxDD `-12.0721`
- `market_context_high->unknown_1h` score `-1.4276` n `166` status `ready` deltaP `0.7485` edge `-0.0616` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.4788` n `166` status `ready` deltaP `0.9293` edge `0.0524` maxDD `-4.8549`
- `market_context_high->equity_4h` score `-1.5933` n `166` status `ready` deltaP `3.2018` edge `0.2111` maxDD `-21.9375`
- `market_context_high->crypto_alt_4h` score `-1.5935` n `166` status `ready` deltaP `0.3122` edge `0.0365` maxDD `-12.7632`
- `market_context_high->unknown_4h` score `-1.7123` n `166` status `ready` deltaP `9.7267` edge `-0.0485` maxDD `-6.2031`
- `market_context_high->fx_4h` score `-2.0715` n `166` status `ready` deltaP `-0.7884` edge `0.0011` maxDD `-2.1439`
- `market_context_high->crypto_major_4h` score `-2.2985` n `166` status `ready` deltaP `4.834` edge `0.0384` maxDD `-21.5574`
- `market_context_high->index_24h` score `-3.8268` n `155` status `ready` deltaP `-18.7355` edge `0.0021` maxDD `-14.7581`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
