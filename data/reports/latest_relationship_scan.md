# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T16:22:30.850001+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4022`

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

- `news_risk_high->equity_4h` score `2.335` n `105` status `ready` deltaP `15.9045` edge `0.2839` maxDD `-4.2454`
- `news_risk_high->equity_24h` score `1.051` n `105` status `ready` deltaP `31.1221` edge `1.0859` maxDD `-86.0244`
- `news_risk_high->index_4h` score `0.9511` n `105` status `ready` deltaP `14.9899` edge `0.0271` maxDD `-0.4888`
- `news_risk_high->index_1h` score `0.0175` n `105` status `ready` deltaP `7.783` edge `0.0036` maxDD `-0.6553`
- `news_risk_high->index_24h` score `-0.1913` n `105` status `ready` deltaP `2.4682` edge `0.1425` maxDD `-6.6786`
- `news_risk_high->equity_1h` score `-0.3139` n `105` status `ready` deltaP `2.381` edge `0.0578` maxDD `-5.4464`
- `news_risk_high->fx_1h` score `-0.3643` n `105` status `ready` deltaP `-1.008` edge `0.0` maxDD `-0.1984`
- `news_risk_high->crypto_major_4h` score `-0.6061` n `105` status `ready` deltaP `-0.2845` edge `0.0928` maxDD `-9.1553`
- `news_risk_high->crypto_alt_4h` score `-0.6104` n `105` status `ready` deltaP `2.1138` edge `0.1713` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6863` n `105` status `ready` deltaP `1.919` edge `0.022` maxDD `-5.8225`
- `news_risk_high->metal_1h` score `-0.7371` n `105` status `ready` deltaP `-1.075` edge `-0.0076` maxDD `-0.733`
- `news_risk_high->fx_4h` score `-0.7953` n `105` status `ready` deltaP `-2.6887` edge `-0.0031` maxDD `-0.4745`
- `news_risk_high->metal_4h` score `-1.0099` n `105` status `ready` deltaP `-1.3545` edge `-0.0299` maxDD `-1.5773`
- `news_risk_high->fx_24h` score `-1.2071` n `105` status `ready` deltaP `-14.2215` edge `0.0035` maxDD `-0.4086`
- `news_risk_high->crypto_major_1h` score `-1.4255` n `105` status `ready` deltaP `-3.3462` edge `-0.0026` maxDD `-4.1772`
- `news_risk_high->metal_24h` score `-2.9372` n `105` status `ready` deltaP `2.5705` edge `-0.2041` maxDD `-8.5019`
- `news_risk_high->commodity_1h` score `-3.0122` n `105` status `ready` deltaP `-15.7143` edge `-0.0096` maxDD `-3.2657`
- `news_risk_high->commodity_4h` score `-5.4204` n `105` status `ready` deltaP `-28.5511` edge `-0.0308` maxDD `-9.4446`
- `news_risk_high->crypto_major_24h` score `-6.0143` n `105` status `ready` deltaP `-16.2366` edge `0.1875` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-10.1337` n `105` status `ready` deltaP `-24.4752` edge `-0.012` maxDD `-36.2114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
