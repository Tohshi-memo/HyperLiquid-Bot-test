# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T16:37:33.550436+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6601`

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

- `market_context_high->unknown_24h` score `7137.9883` n `55` status `ready` deltaP `1.3889` edge `594.8231` maxDD `0.0`
- `market_context_high->unknown_4h` score `380.0184` n `55` status `ready` deltaP `6.1086` edge `31.6318` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `74.9354` n `55` status `ready` deltaP `4.061` edge `6.2286` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.0892` n `55` status `ready` deltaP `42.7999` edge `1.4957` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.1784` n `94` status `ready` deltaP `30.9619` edge `1.0274` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.6685` n `55` status `ready` deltaP `54.1667` edge `0.1946` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.299` n `55` status `ready` deltaP `44.4003` edge `0.26` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.1508` n `55` status `ready` deltaP `24.3598` edge `0.3796` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.7071` n `55` status `ready` deltaP `31.5023` edge `0.2992` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.5189` n `55` status `ready` deltaP `6.3525` edge `0.3211` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.326` n `55` status `ready` deltaP `31.2195` edge `0.0941` maxDD `-0.3387`
- `news_risk_high->crypto_alt_4h` score `3.1624` n `120` status `ready` deltaP `13.5265` edge `0.312` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `2.4092` n `55` status `ready` deltaP `10.685` edge `0.3053` maxDD `-3.0799`
- `news_risk_high->unknown_1h` score `2.1759` n `126` status `ready` deltaP `-7.2521` edge `0.2583` maxDD `-0.9571`
- `market_context_high->crypto_alt_24h` score `1.8763` n `55` status `ready` deltaP `-4.2992` edge `0.421` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.6628` n `55` status `ready` deltaP `19.4179` edge `0.0516` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.562` n `55` status `ready` deltaP `3.3261` edge `0.1605` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.4671` n `55` status `ready` deltaP `8.6309` edge `0.1257` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.4578` n `55` status `ready` deltaP `4.374` edge `0.1594` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.975` n `55` status `ready` deltaP `12.074` edge `0.0256` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
