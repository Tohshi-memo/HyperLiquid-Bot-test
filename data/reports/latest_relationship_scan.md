# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T05:37:25.630435+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6373`

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

- `market_context_high->unknown_24h` score `6290.7555` n `60` status `ready` deltaP `1.875` edge `524.2246` maxDD `-0.2646`
- `market_context_high->unknown_4h` score `324.7384` n `60` status `ready` deltaP `5.4979` edge `27.0292` maxDD `-0.0124`
- `news_risk_high->unknown_1h` score `81.67` n `108` status `ready` deltaP `-5.1951` edge `6.8691` maxDD `-0.9571`
- `market_context_high->unknown_1h` score `28.164` n `60` status `ready` deltaP `3.3234` edge `2.3359` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.5222` n `60` status `ready` deltaP `39.3056` edge `1.4105` maxDD `-1.988`
- `news_risk_high->crypto_alt_24h` score `13.4059` n `98` status `ready` deltaP `31.7212` edge `1.0413` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.5578` n `60` status `ready` deltaP `55.4167` edge `0.1907` maxDD `-0.0926`
- `news_risk_high->crypto_alt_4h` score `5.1159` n `108` status `ready` deltaP `19.3598` edge `0.4359` maxDD `-7.4246`
- `market_context_high->crypto_major_4h` score `3.6427` n `60` status `ready` deltaP `24.3801` edge `0.2114` maxDD `-3.6301`
- `market_context_high->crypto_alt_4h` score `3.6384` n `60` status `ready` deltaP `17.6931` edge `0.2676` maxDD `-4.5886`
- `market_context_high->commodity_24h` score `3.3678` n `60` status `ready` deltaP `39.6875` edge `0.2246` maxDD `-2.9262`
- `market_context_high->commodity_4h` score `2.8465` n `60` status `ready` deltaP `27.2866` edge `0.0887` maxDD `-0.3387`
- `market_context_high->equity_4h` score `2.6267` n `60` status `ready` deltaP `2.1138` edge `0.275` maxDD `-2.283`
- `market_context_high->crypto_major_24h` score `2.0199` n `60` status `ready` deltaP `7.6389` edge `0.2757` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.5145` n `60` status `ready` deltaP `-7.3264` edge `0.3948` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.5077` n `60` status `ready` deltaP `18.0488` edge `0.0478` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.8457` n `60` status `ready` deltaP `10.7285` edge `0.0238` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.7497` n `108` status `ready` deltaP `8.2779` edge `0.1027` maxDD `-3.9659`
- `market_context_high->fx_1h` score `0.6529` n `60` status `ready` deltaP `15.3194` edge `0.0` maxDD `-0.1407`
- `market_context_high->equity_1h` score `0.5091` n `60` status `ready` deltaP `-1.6667` edge `0.1398` maxDD `-1.7407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
