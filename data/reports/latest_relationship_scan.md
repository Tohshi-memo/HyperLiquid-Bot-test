# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T16:07:25.946056+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6591`

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

- `market_context_high->unknown_24h` score `7105.1275` n `55` status `ready` deltaP `1.3889` edge `592.0847` maxDD `0.0`
- `market_context_high->unknown_4h` score `379.9292` n `55` status `ready` deltaP `5.8038` edge `31.6264` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `74.7795` n `55` status `ready` deltaP `3.7616` edge `6.2176` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.076` n `55` status `ready` deltaP `42.7999` edge `1.4946` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.1122` n `94` status `ready` deltaP `30.6146` edge `1.0242` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.7023` n `55` status `ready` deltaP `54.5139` edge `0.1951` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.2954` n `55` status `ready` deltaP `44.4003` edge `0.2597` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.1278` n `55` status `ready` deltaP `24.2073` edge `0.3787` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.7059` n `55` status `ready` deltaP `31.5023` edge `0.2991` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.5141` n `55` status `ready` deltaP `6.3525` edge `0.3207` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.298` n `55` status `ready` deltaP `30.9146` edge `0.0938` maxDD `-0.3387`
- `news_risk_high->crypto_alt_4h` score `3.211` n `118` status `ready` deltaP `13.6988` edge `0.3149` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `2.4076` n `55` status `ready` deltaP `10.685` edge `0.3051` maxDD `-3.0799`
- `news_risk_high->unknown_1h` score `2.0199` n `126` status `ready` deltaP `-7.5515` edge `0.2473` maxDD `-0.9571`
- `market_context_high->crypto_alt_24h` score `1.8333` n `55` status `ready` deltaP `-4.6465` edge `0.4178` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.6616` n `55` status `ready` deltaP `19.4179` edge `0.0515` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.5572` n `55` status `ready` deltaP `3.3261` edge `0.1601` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.424` n `55` status `ready` deltaP `8.3315` edge `0.1241` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.3991` n `55` status `ready` deltaP `4.0746` edge `0.1565` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.9498` n `55` status `ready` deltaP `11.7746` edge `0.0255` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
