# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T15:07:28.720952+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `7312`

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

- `market_context_high->unknown_24h` score `1279.8561` n `41` status `ready` deltaP `-18.8346` edge `106.8166` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `53.8983` n `73` status `ready` deltaP `-8.0438` edge `4.6032` maxDD `-2.3109`
- `market_context_high->unknown_1h` score `12.9723` n `82` status `ready` deltaP `-5.2285` edge `1.1495` maxDD `-1.0231`
- `market_context_high->equity_24h` score `8.8732` n `41` status `ready` deltaP `28.7432` edge `0.5907` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.113` n `41` status `ready` deltaP `50.5124` edge `0.1778` maxDD `-0.0774`
- `market_context_high->fx_24h` score `3.2699` n `41` status `ready` deltaP `36.9453` edge `0.0393` maxDD `-0.0489`
- `market_context_high->crypto_major_24h` score `2.117` n `41` status `ready` deltaP `-18.8643` edge `0.617` maxDD `-17.8526`
- `market_context_high->fx_4h` score `1.043` n `73` status `ready` deltaP `15.8975` edge `0.0093` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.7305` n `73` status `ready` deltaP `14.371` edge `0.0184` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `-0.1209` n `82` status `ready` deltaP `1.5846` edge `0.0023` maxDD `-0.6025`
- `market_context_high->crypto_alt_1h` score `-0.169` n `82` status `ready` deltaP `3.4249` edge `0.0665` maxDD `-4.9401`
- `market_context_high->fx_1h` score `-0.1837` n `82` status `ready` deltaP `1.1575` edge `0.0012` maxDD `-0.271`
- `market_context_high->metal_1h` score `-0.3553` n `82` status `ready` deltaP `4.0018` edge `0.0026` maxDD `-0.7107`
- `market_context_high->metal_4h` score `-0.4133` n `73` status `ready` deltaP `-0.0773` edge `0.0198` maxDD `-1.1153`
- `market_context_high->crypto_major_1h` score `-0.8241` n `82` status `ready` deltaP `-0.8982` edge `0.0262` maxDD `-3.7778`
- `market_context_high->index_4h` score `-1.0709` n `73` status `ready` deltaP `-10.1236` edge `0.0005` maxDD `-0.9573`
- `market_context_high->equity_1h` score `-1.2719` n `82` status `ready` deltaP `-10.0956` edge `-0.0088` maxDD `-2.2898`
- `market_context_high->index_1h` score `-1.4315` n `82` status `ready` deltaP `-6.9958` edge `-0.0034` maxDD `-0.5405`
- `market_context_high->crypto_major_4h` score `-1.4383` n `73` status `ready` deltaP `-6.9203` edge `0.0723` maxDD `-11.1784`
- `market_context_high->crypto_alt_4h` score `-2.1537` n `73` status `ready` deltaP `-9.5201` edge `0.0432` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
