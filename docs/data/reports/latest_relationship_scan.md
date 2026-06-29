# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T12:52:29.481443+00:00`
- Price records: `672`
- Market context records: `5145`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5596`

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

- `market_context_high->unknown_24h` score `25.7586` n `68` status `ready` deltaP `31.5462` edge `1.9705` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `6.3704` n `128` status `ready` deltaP `18.1784` edge `0.5119` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `5.6419` n `140` status `ready` deltaP `10.231` edge `0.4661` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `4.9241` n `128` status `ready` deltaP `15.3391` edge `0.468` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.6674` n `128` status `ready` deltaP `13.3003` edge `0.4462` maxDD `-14.0065`
- `market_context_high->crypto_major_1h` score `0.965` n `140` status `ready` deltaP `8.8451` edge `0.146` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.9621` n `128` status `ready` deltaP `10.4611` edge `0.1743` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.9554` n `140` status `ready` deltaP `6.4157` edge `0.133` maxDD `-5.0257`
- `market_context_high->commodity_24h` score `0.7675` n `68` status `ready` deltaP `15.6862` edge `0.1171` maxDD `-5.1955`
- `market_context_high->equity_1h` score `0.7087` n `140` status `ready` deltaP `7.6604` edge `0.0673` maxDD `-2.745`
- `market_context_high->crypto_alt_24h` score `0.2697` n `68` status `ready` deltaP `16.8505` edge `0.5553` maxDD `-46.2794`
- `market_context_high->metal_1h` score `-0.0016` n `140` status `ready` deltaP `5.7699` edge `0.0179` maxDD `-1.8592`
- `market_context_high->index_1h` score `-0.0417` n `140` status `ready` deltaP `4.9187` edge `0.0141` maxDD `-1.0296`
- `market_context_high->crypto_major_24h` score `-0.3266` n `68` status `ready` deltaP `15.3902` edge `0.5541` maxDD `-48.0465`
- `market_context_high->metal_24h` score `-0.3911` n `68` status `ready` deltaP `-1.8587` edge `0.1681` maxDD `-10.0641`
- `market_context_high->index_4h` score `-0.4317` n `128` status `ready` deltaP `5.9641` edge `0.036` maxDD `-2.9391`
- `market_context_high->fx_24h` score `-0.4908` n `68` status `ready` deltaP `4.0543` edge `-0.0001` maxDD `-0.8549`
- `market_context_high->fx_1h` score `-0.5431` n `140` status `ready` deltaP `-0.6801` edge `-0.001` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.6459` n `140` status `ready` deltaP `-0.3807` edge `-0.0021` maxDD `-2.2534`
- `market_context_high->fx_4h` score `-0.8487` n `128` status `ready` deltaP `-0.5716` edge `0.0018` maxDD `-1.8772`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
