# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T00:37:25.699310+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7488`

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

- `market_context_high->unknown_24h` score `7636.3411` n `55` status `ready` deltaP `1.3889` edge `636.3525` maxDD `0.0`
- `market_context_high->unknown_4h` score `331.1918` n `55` status `ready` deltaP `7.1757` edge `27.5558` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `32.0125` n `56` status `ready` deltaP `4.7049` edge `2.6474` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.3364` n `55` status `ready` deltaP `42.7999` edge `1.5163` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.4254` n `94` status `ready` deltaP `31.8299` edge `1.0422` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.1674` n `55` status `ready` deltaP `49.1319` edge `0.1864` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.0267` n `55` status `ready` deltaP `23.9024` edge `0.3723` maxDD `-1.6876`
- `market_context_high->commodity_24h` score `5.8698` n `55` status `ready` deltaP `40.5808` edge `0.2497` maxDD `-0.8203`
- `market_context_high->crypto_major_4h` score `5.4429` n `55` status `ready` deltaP `30.4352` edge `0.2843` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.1698` n `55` status `ready` deltaP `5.4379` edge `0.2981` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.011` n `55` status `ready` deltaP `28.9329` edge `0.0831` maxDD `-0.3387`
- `market_context_high->crypto_major_24h` score `2.4372` n `55` status `ready` deltaP `10.685` edge `0.3089` maxDD `-3.0799`
- `news_risk_high->crypto_alt_4h` score `2.3487` n `126` status `ready` deltaP `9.7754` edge `0.2692` maxDD `-7.4246`
- `market_context_high->crypto_alt_24h` score `2.0369` n `55` status `ready` deltaP `-3.4312` edge `0.4358` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.7531` n `55` status `ready` deltaP `20.6374` edge `0.051` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.5636` n `56` status `ready` deltaP `3.7211` edge `0.158` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.2449` n `56` status `ready` deltaP `6.9932` edge `0.1181` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.1834` n `56` status `ready` deltaP `2.6839` edge `0.1478` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.8643` n `56` status `ready` deltaP `10.8854` edge `0.0243` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5914` n `56` status `ready` deltaP `13.9863` edge `0.001` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
