# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T07:52:34.898273+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9897`

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

- `market_context_high->unknown_1h` score `66.1206` n `47` status `ready` deltaP `10.5651` edge `5.4467` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `40.2417` n `46` status `ready` deltaP `27.5966` edge `3.1851` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `25.3172` n `46` status `ready` deltaP `22.5694` edge `1.9593` maxDD `0.0`
- `market_context_high->equity_24h` score `23.3035` n `46` status `ready` deltaP `24.9925` edge `1.7854` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.7315` n `46` status `ready` deltaP `34.0203` edge `0.4262` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `6.5005` n `103` status `ready` deltaP `-0.0944` edge `1.4466` maxDD `-63.6743`
- `news_risk_high->crypto_alt_4h` score `4.7626` n `103` status `ready` deltaP `14.2316` edge `0.4018` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.6844` n `103` status `ready` deltaP `18.195` edge `0.3268` maxDD `-2.619`
- `news_risk_high->crypto_alt_24h` score `3.0551` n `103` status `ready` deltaP `-2.6733` edge `0.9737` maxDD `-49.7699`
- `market_context_high->metal_24h` score `2.9383` n `46` status `ready` deltaP `27.9967` edge `0.0816` maxDD `-0.2042`
- `market_context_high->index_4h` score `2.7811` n `47` status `ready` deltaP `32.3495` edge `0.0315` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.3067` n `113` status `ready` deltaP `12.6994` edge `0.1566` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.0602` n `47` status `ready` deltaP `15.1628` edge `0.1124` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `1.9215` n `113` status `ready` deltaP `14.7952` edge `0.105` maxDD `-1.8141`
- `news_risk_high->commodity_24h` score `1.8562` n `103` status `ready` deltaP `20.2754` edge `0.1374` maxDD `-2.431`
- `news_risk_high->fx_4h` score `1.616` n `103` status `ready` deltaP `23.5289` edge `0.0414` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2602` n `103` status `ready` deltaP `30.0111` edge `0.1246` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.8625` n `47` status `ready` deltaP `13.5622` edge `0.0093` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.7689` n `47` status `ready` deltaP `10.1191` edge `0.0369` maxDD `-1.5564`
- `news_risk_high->metal_1h` score `0.6057` n `113` status `ready` deltaP `14.6415` edge `0.0122` maxDD `-0.7468`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
