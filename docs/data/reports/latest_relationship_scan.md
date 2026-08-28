# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T00:37:30.781692+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `news_risk_high->unknown_24h` score `52.4334` n `50` status `ready` deltaP `11.6319` edge `4.2919` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `24.2898` n `50` status `ready` deltaP `37.8403` edge `1.816` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6712` n `50` status `ready` deltaP `24.6402` edge `0.9016` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `5.0046` n `50` status `ready` deltaP `46.4375` edge `0.1117` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `5.0021` n `50` status `ready` deltaP `27.9236` edge `0.3235` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.7594` n `50` status `ready` deltaP `43.9817` edge `0.0291` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.009` n `128` status `ready` deltaP `5.3819` edge `0.2881` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.9108` n `50` status `ready` deltaP `15.9281` edge `0.172` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.8481` n `50` status `ready` deltaP `31.9236` edge `0.0396` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2282` n `148` status `ready` deltaP `17.8024` edge `0.1077` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.5168` n `50` status `ready` deltaP `20.3533` edge `0.0077` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.2949` n `50` status `ready` deltaP `17.8623` edge `0.0167` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.1876` n `50` status `ready` deltaP `20.8171` edge `0.0365` maxDD `-2.105`
- `market_context_high->unknown_1h` score `0.7874` n `148` status `ready` deltaP `8.2254` edge `0.0558` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.516` n `50` status `ready` deltaP `14.2994` edge `0.0021` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.146` n `50` status `ready` deltaP `7.8084` edge `0.0006` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0976` n `50` status `ready` deltaP `5.4012` edge `-0.0009` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `0.0297` n `50` status `ready` deltaP `8.6829` edge `-0.0023` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.0747` n `50` status `ready` deltaP `5.1037` edge `-0.0006` maxDD `-0.1719`
- `market_context_high->metal_4h` score `-0.3619` n `148` status `ready` deltaP `7.5478` edge `-0.005` maxDD `-3.3377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
