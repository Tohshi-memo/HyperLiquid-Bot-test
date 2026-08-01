# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T15:52:29.144059+00:00`
- Price records: `672`
- Market context records: `8637`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5915`

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

- `news_risk_high->unknown_24h` score `5190.9462` n `60` status `ready` deltaP `34.2345` edge `432.3927` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.1634` n `53` status `ready` deltaP `54.4979` edge `1.1067` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.3888` n `60` status `ready` deltaP `22.8455` edge `0.4398` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.596` n `60` status `ready` deltaP `22.6931` edge `0.0841` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.5946` n `61` status `ready` deltaP `14.2044` edge `0.0867` maxDD `-2.5479`
- `market_context_high->commodity_24h` score `1.5589` n `53` status `ready` deltaP `27.5236` edge `0.2217` maxDD `-11.0937`
- `news_risk_high->crypto_major_4h` score `1.2844` n `60` status `ready` deltaP `7.7439` edge `0.1906` maxDD `-3.5385`
- `market_context_high->crypto_alt_4h` score `0.6559` n `55` status `ready` deltaP `9.5538` edge `0.1161` maxDD `-5.323`
- `news_risk_high->crypto_alt_4h` score `0.5033` n `60` status `ready` deltaP `11.372` edge `0.1279` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4003` n `61` status `ready` deltaP `7.8261` edge `0.0534` maxDD `-2.0068`
- `news_risk_high->crypto_major_1h` score `0.3007` n `61` status `ready` deltaP `5.7377` edge `0.0525` maxDD `-2.1755`
- `news_risk_high->fx_4h` score `0.29` n `60` status `ready` deltaP `14.2988` edge `0.0246` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1448` n `60` status `ready` deltaP `4.6748` edge `0.035` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `0.1369` n `61` status `ready` deltaP `6.4715` edge `0.0086` maxDD `-0.5599`
- `market_context_high->fx_4h` score `0.123` n `55` status `ready` deltaP `12.0261` edge `0.0152` maxDD `-1.3685`
- `news_risk_high->fx_1h` score `0.061` n `61` status `ready` deltaP `4.6972` edge `0.0046` maxDD `-0.2475`
- `market_context_high->commodity_1h` score `0.0442` n `55` status `ready` deltaP `6.0425` edge `0.0175` maxDD `-1.3282`
- `news_risk_high->index_1h` score `0.0378` n `61` status `ready` deltaP `4.0836` edge `0.0093` maxDD `-0.5338`
- `market_context_high->fx_24h` score `-0.07` n `53` status `ready` deltaP `7.0207` edge `0.0404` maxDD `-2.3606`
- `market_context_high->fx_1h` score `-0.1856` n `55` status `ready` deltaP `5.1443` edge `0.0005` maxDD `-0.6874`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
