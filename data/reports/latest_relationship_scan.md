# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T15:14:07.059293+00:00`
- Price records: `672`
- Market context records: `8634`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `5191.185` n `60` status `ready` deltaP `34.2345` edge `432.4126` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.267` n `51` status `ready` deltaP `54.202` edge `1.1173` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.3307` n `60` status `ready` deltaP `22.3882` edge `0.438` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.5814` n `60` status `ready` deltaP `22.5406` edge `0.0839` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7155` n `60` status `ready` deltaP `15.2296` edge `0.0891` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.2578` n `60` status `ready` deltaP `7.7439` edge `0.1872` maxDD `-3.5385`
- `market_context_high->commodity_24h` score `1.1099` n `51` status `ready` deltaP `24.8989` edge `0.1916` maxDD `-11.5569`
- `market_context_high->crypto_alt_4h` score `0.7125` n `56` status `ready` deltaP `10.1481` edge `0.1194` maxDD `-5.323`
- `news_risk_high->crypto_alt_4h` score `0.4767` n `60` status `ready` deltaP `11.2195` edge `0.1255` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4483` n `60` status `ready` deltaP `8.3333` edge `0.0546` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3404` n `60` status `ready` deltaP `6.2176` edge `0.0534` maxDD `-2.0972`
- `news_risk_high->fx_4h` score `0.329` n `60` status `ready` deltaP `14.7561` edge `0.0248` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1455` n `60` status `ready` deltaP `4.6748` edge `0.0351` maxDD `-0.8085`
- `market_context_high->commodity_1h` score `0.1366` n `56` status `ready` deltaP `7.1535` edge `0.0178` maxDD `-1.3282`
- `market_context_high->fx_24h` score `0.1269` n `51` status `ready` deltaP `10.0893` edge `0.043` maxDD `-2.1858`
- `news_risk_high->fx_1h` score `0.1258` n `60` status `ready` deltaP `5.8982` edge `0.0049` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `0.1182` n `60` status `ready` deltaP `6.2375` edge `0.0086` maxDD `-0.5599`
- `market_context_high->fx_4h` score `0.0978` n `56` status `ready` deltaP `11.5418` edge `0.0152` maxDD `-1.3685`
- `news_risk_high->index_1h` score `-0.0069` n `60` status `ready` deltaP `3.2236` edge `0.0093` maxDD `-0.5338`
- `market_context_high->fx_1h` score `-0.2395` n `56` status `ready` deltaP `4.4696` edge `0.0005` maxDD `-0.6874`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
