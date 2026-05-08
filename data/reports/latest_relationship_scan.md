# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T12:52:20.149961+00:00`
- Price records: `647`
- Market context records: `756`
- Flow alert records: `2134`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1117`

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

- `market_context_high->crypto_major_24h` score `13.3079` n `146` status `ready` deltaP `31.7082` edge `0.931` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.7233` n `146` status `ready` deltaP `7.4821` edge `0.5152` maxDD `-0.0508`
- `risk_on_high->metal_1h` score `1.4962` n `30` status `ready` deltaP `16.7237` edge `0.0362` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.4962` n `30` status `ready` deltaP `16.7237` edge `0.0362` maxDD `-0.5074`
- `risk_on_high->fx_1h` score `1.0104` n `30` status `ready` deltaP `14.6009` edge `0.0051` maxDD `-0.126`
- `risk_on_and_context->fx_1h` score `1.0104` n `30` status `ready` deltaP `14.6009` edge `0.0051` maxDD `-0.126`
- `risk_on_high->crypto_major_1h` score `0.8309` n `30` status `ready` deltaP `10.7672` edge `0.0213` maxDD `-0.5736`
- `risk_on_and_context->crypto_major_1h` score `0.8309` n `30` status `ready` deltaP `10.7672` edge `0.0213` maxDD `-0.5736`
- `market_context_high->index_24h` score `0.5374` n `146` status `ready` deltaP `3.1792` edge `0.2231` maxDD `-5.9609`
- `risk_on_high->crypto_alt_1h` score `0.3732` n `30` status `ready` deltaP `7.7242` edge `-0.002` maxDD `-0.4713`
- `risk_on_and_context->crypto_alt_1h` score `0.3732` n `30` status `ready` deltaP `7.7242` edge `-0.002` maxDD `-0.4713`
- `risk_on_high->commodity_1h` score `-0.0166` n `30` status `ready` deltaP `3.8341` edge `0.0099` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `-0.0166` n `30` status `ready` deltaP `3.8341` edge `0.0099` maxDD `-0.6739`
- `market_context_high->equity_24h` score `-0.0247` n `146` status `ready` deltaP `1.6679` edge `0.2473` maxDD `-10.5047`
- `market_context_high->fx_1h` score `-0.2763` n `173` status `ready` deltaP `2.9824` edge `0.0025` maxDD `-0.291`
- `market_context_high->fx_4h` score `-0.4396` n `161` status `ready` deltaP `6.1814` edge `0.0093` maxDD `-1.6381`
- `risk_on_high->index_1h` score `-0.5974` n `30` status `ready` deltaP `-4.0532` edge `0.0056` maxDD `-0.2687`
- `risk_on_and_context->index_1h` score `-0.5974` n `30` status `ready` deltaP `-4.0532` edge `0.0056` maxDD `-0.2687`
- `market_context_high->commodity_1h` score `-0.628` n `173` status `ready` deltaP `1.2329` edge `0.0369` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.6913` n `173` status `ready` deltaP `-1.1696` edge `0.0002` maxDD `-4.4826`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
