# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T11:37:25.665630+00:00`
- Price records: `672`
- Market context records: `7024`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11529`

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

- `market_context_high->fx_1h` score `-0.2855` n `220` status `ready` deltaP `1.6358` edge `0.001` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.6567` n `220` status `ready` deltaP `0.7812` edge `0.0265` maxDD `-4.5815`
- `market_context_high->metal_1h` score `-0.6733` n `220` status `ready` deltaP `-1.595` edge `0.0011` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.7417` n `220` status `ready` deltaP `-0.5199` edge `-0.0005` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.7505` n `220` status `ready` deltaP `2.4333` edge `0.0228` maxDD `-7.1523`
- `market_context_high->unknown_24h` score `-0.7722` n `207` status `ready` deltaP `-6.7029` edge `0.4007` maxDD `-18.7342`
- `market_context_high->fx_4h` score `-0.7836` n `220` status `ready` deltaP `10.6513` edge `0.0066` maxDD `-1.9118`
- `market_context_high->unknown_1h` score `-1.2702` n `220` status `ready` deltaP `-2.9314` edge `-0.0007` maxDD `-3.1819`
- `market_context_high->commodity_1h` score `-1.3886` n `220` status `ready` deltaP `-3.7752` edge `-0.0184` maxDD `-2.4388`
- `market_context_high->commodity_4h` score `-1.5682` n `220` status `ready` deltaP `-4.4291` edge `-0.0389` maxDD `-4.2764`
- `market_context_high->index_4h` score `-1.8504` n `220` status `ready` deltaP `6.8514` edge `-0.013` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-1.9475` n `220` status `ready` deltaP `5.8565` edge `0.0096` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.2789` n `220` status `ready` deltaP `-5.9784` edge `0.0767` maxDD `-9.4737`
- `market_context_high->commodity_24h` score `-2.7634` n `207` status `ready` deltaP `-3.5553` edge `-0.0757` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.7656` n `220` status `ready` deltaP `0.7761` edge `0.0188` maxDD `-22.2831`
- `market_context_high->equity_1h` score `-3.1016` n `220` status `ready` deltaP `2.3625` edge `-0.0188` maxDD `-15.7664`
- `market_context_high->crypto_major_4h` score `-3.1407` n `220` status `ready` deltaP `1.8293` edge `0.0136` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.9626` n `207` status `ready` deltaP `-4.1667` edge `-0.0143` maxDD `-4.3844`
- `market_context_high->equity_4h` score `-11.3974` n `220` status `ready` deltaP `3.9884` edge `-0.0761` maxDD `-65.0215`
- `market_context_high->metal_24h` score `-13.5085` n `207` status `ready` deltaP `-11.0507` edge `-0.0551` maxDD `-39.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
