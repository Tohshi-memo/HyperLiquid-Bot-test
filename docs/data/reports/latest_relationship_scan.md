# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T16:07:33.644224+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10204`

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

- `market_context_high->unknown_4h` score `29.8333` n `58` status `ready` deltaP `1.23` edge `2.4929` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `18.2198` n `101` status `ready` deltaP `5.8873` edge `2.1649` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `12.227` n `101` status `ready` deltaP `6.2723` edge `1.4652` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.5745` n `101` status `ready` deltaP `16.9373` edge `0.3059` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.2107` n `101` status `ready` deltaP `19.9861` edge `0.2601` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.4944` n `101` status `ready` deltaP `15.3332` edge `0.1522` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.8086` n `101` status `ready` deltaP `16.8302` edge `0.0908` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.5674` n `101` status `ready` deltaP `25.2802` edge `0.163` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7396` n `58` status `ready` deltaP `5.2602` edge `0.0519` maxDD `-0.36`
- `market_context_high->index_1h` score `0.5783` n `58` status `ready` deltaP `9.0801` edge `0.0132` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.5454` n `101` status `ready` deltaP `13.8495` edge `0.0133` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.3714` n `58` status `ready` deltaP `9.075` edge `0.0061` maxDD `-0.1854`
- `news_risk_high->metal_4h` score `0.3149` n `101` status `ready` deltaP `14.8122` edge `0.0329` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.2675` n `58` status `ready` deltaP `5.3996` edge `0.0171` maxDD `-0.1314`
- `news_risk_high->fx_4h` score `0.2647` n `101` status `ready` deltaP `9.098` edge `0.025` maxDD `-0.421`
- `market_context_high->index_4h` score `0.2355` n `58` status `ready` deltaP `13.2569` edge `0.0055` maxDD `-1.0949`
- `news_risk_high->fx_1h` score `-0.1777` n `101` status `ready` deltaP `3.4416` edge `0.0066` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.3352` n `101` status `ready` deltaP `0.873` edge `0.0068` maxDD `-0.9112`
- `market_context_high->fx_4h` score `-0.4639` n `58` status `ready` deltaP `0.9041` edge `-0.0031` maxDD `-0.6588`
- `market_context_high->crypto_major_1h` score `-0.4763` n `58` status `ready` deltaP `-2.9888` edge `0.0521` maxDD `-2.7494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
