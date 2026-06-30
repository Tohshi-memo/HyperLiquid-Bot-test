# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T08:07:52.361463+00:00`
- Price records: `672`
- Market context records: `5229`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5600`

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

- `market_context_high->unknown_24h` score `21.6687` n `120` status `ready` deltaP `32.4306` edge `1.6085` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `13.4907` n `120` status `ready` deltaP `32.0834` edge `1.2765` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `7.8383` n `120` status `ready` deltaP `24.5834` edge `0.828` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `3.9359` n `155` status `ready` deltaP `12.9318` edge `0.4017` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.8788` n `155` status `ready` deltaP `13.9172` edge `0.4597` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `2.1372` n `155` status `ready` deltaP `16.9827` edge `0.1671` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `1.8442` n `155` status `ready` deltaP `8.2393` edge `0.1629` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.5587` n `120` status `ready` deltaP `13.3333` edge `0.0472` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `0.3953` n `155` status `ready` deltaP `6.553` edge `0.1138` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.3933` n `155` status `ready` deltaP `4.3539` edge `0.0999` maxDD `-5.0257`
- `market_context_high->equity_24h` score `0.1954` n `120` status `ready` deltaP `16.9097` edge `0.4752` maxDD `-40.0306`
- `market_context_high->equity_4h` score `-0.0039` n `155` status `ready` deltaP `5.7208` edge `0.1254` maxDD `-7.4425`
- `market_context_high->metal_1h` score `-0.222` n `155` status `ready` deltaP `3.2132` edge `0.0093` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.2463` n `155` status `ready` deltaP `4.9208` edge `0.0432` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.2589` n `155` status `ready` deltaP `3.0887` edge `0.0082` maxDD `-1.0296`
- `market_context_high->index_24h` score `-0.2636` n `120` status `ready` deltaP `15.5555` edge `0.026` maxDD `-7.413`
- `market_context_high->fx_1h` score `-0.311` n `155` status `ready` deltaP `0.9108` edge `-0.0007` maxDD `-0.6194`
- `market_context_high->commodity_1h` score `-0.6265` n `155` status `ready` deltaP `0.2762` edge `-0.0013` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.6832` n `155` status `ready` deltaP `1.8145` edge `0.0037` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.9141` n `155` status `ready` deltaP `3.0094` edge `0.0155` maxDD `-2.9391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
