# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T12:52:33.311753+00:00`
- Price records: `672`
- Market context records: `7776`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `6.7656` n `132` status `ready` deltaP `26.7131` edge `0.5199` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.3119` n `133` status `ready` deltaP `12.7506` edge `0.2334` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `0.9398` n `133` status `ready` deltaP `12.7088` edge `0.0377` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.6685` n `132` status `ready` deltaP `23.0942` edge `0.0405` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `0.4779` n `133` status `ready` deltaP `12.3647` edge `0.1292` maxDD `-6.7444`
- `market_context_high->equity_1h` score `0.395` n `133` status `ready` deltaP `7.4454` edge `0.0692` maxDD `-4.2072`
- `market_context_high->equity_4h` score `0.3853` n `133` status `ready` deltaP `1.6636` edge `0.2296` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.2846` n `133` status `ready` deltaP `7.8937` edge `0.0141` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `0.264` n `133` status `ready` deltaP `6.8276` edge `0.0882` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.2111` n `133` status `ready` deltaP `6.622` edge `0.0328` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.104` n `133` status `ready` deltaP `4.1286` edge `0.0244` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.0571` n `133` status `ready` deltaP `4.7461` edge `0.0095` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.3068` n `133` status `ready` deltaP `9.794` edge `0.0412` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.387` n `133` status `ready` deltaP `0.9743` edge `0.0` maxDD `-0.4331`
- `market_context_high->commodity_24h` score `-0.8774` n `132` status `ready` deltaP `9.1701` edge `0.0241` maxDD `-7.0012`
- `market_context_high->metal_1h` score `-0.9681` n `133` status `ready` deltaP `0.3692` edge `0.0172` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.4111` n `133` status `ready` deltaP `-2.7856` edge `0.0005` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.7122` n `133` status `ready` deltaP `-0.8436` edge `0.0684` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.8882` n `132` status `ready` deltaP `-12.1819` edge `0.0494` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.2177` n `133` status `ready` deltaP `-0.9747` edge `-0.1193` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
