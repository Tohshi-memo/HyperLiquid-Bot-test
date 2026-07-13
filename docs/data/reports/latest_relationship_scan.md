# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T12:37:30.405060+00:00`
- Price records: `672`
- Market context records: `6603`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9808`

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

- `market_context_high->unknown_24h` score `3.3376` n `168` status `ready` deltaP `3.0318` edge `0.5779` maxDD `-14.5984`
- `market_context_high->unknown_1h` score `2.0591` n `209` status `ready` deltaP `-5.2058` edge `0.2964` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.5018` n `168` status `ready` deltaP `9.186` edge `0.1674` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.306` n `209` status `ready` deltaP `1.6804` edge `0.0003` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4535` n `209` status `ready` deltaP `6.5768` edge `0.0246` maxDD `-6.7936`
- `market_context_high->index_1h` score `-0.5401` n `209` status `ready` deltaP `-0.1483` edge `0.0037` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.5549` n `209` status `ready` deltaP `0.1454` edge `-0.0038` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.6568` n `209` status `ready` deltaP `4.3635` edge `0.018` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.9231` n `209` status `ready` deltaP `9.1099` edge `0.0089` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.1784` n `209` status `ready` deltaP `1.8831` edge `-0.0004` maxDD `-4.1619`
- `market_context_high->commodity_4h` score `-1.2067` n `209` status `ready` deltaP `-0.0956` edge `-0.0046` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.3386` n `209` status `ready` deltaP `-4.2726` edge `-0.0029` maxDD `-2.0797`
- `market_context_high->fx_4h` score `-1.6233` n `209` status `ready` deltaP `2.1152` edge `-0.001` maxDD `-3.3635`
- `market_context_high->unknown_4h` score `-1.6836` n `209` status `ready` deltaP `-17.3751` edge `0.2161` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.8871` n `209` status `ready` deltaP `6.6329` edge `0.0453` maxDD `-16.8495`
- `market_context_high->metal_4h` score `-2.201` n `209` status `ready` deltaP `-1.9241` edge `0.0167` maxDD `-5.2172`
- `market_context_high->crypto_alt_4h` score `-2.2089` n `209` status `ready` deltaP `3.6731` edge `0.0325` maxDD `-19.2145`
- `market_context_high->fx_24h` score `-3.8181` n `168` status `ready` deltaP `-6.078` edge `-0.0005` maxDD `-9.2113`
- `market_context_high->metal_24h` score `-4.8441` n `168` status `ready` deltaP `-0.0227` edge `0.0568` maxDD `-10.8256`
- `market_context_high->equity_4h` score `-4.9329` n `209` status `ready` deltaP `6.3959` edge `-0.0268` maxDD `-27.1529`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
