# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T14:37:31.621709+00:00`
- Price records: `672`
- Market context records: `2253`
- Flow alert records: `8379`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9257`

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

- `news_risk_high->crypto_alt_24h` score `23.7491` n `43` status `ready` deltaP `54.203` edge `1.6766` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.1233` n `43` status `ready` deltaP `43.855` edge `1.0952` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.6291` n `43` status `ready` deltaP `34.8272` edge `1.1017` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `13.2718` n `43` status `ready` deltaP `24.8021` edge `0.9987` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `10.0622` n `115` status `ready` deltaP `31.0612` edge `0.6726` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `9.6257` n `43` status `ready` deltaP `35.1057` edge `0.5907` maxDD `-1.4744`
- `market_context_high->crypto_alt_4h` score `8.7356` n `136` status `ready` deltaP `28.2819` edge `0.7887` maxDD `-14.6089`
- `market_context_high->crypto_major_4h` score `8.2144` n `136` status `ready` deltaP `33.5993` edge `0.6314` maxDD `-9.6692`
- `market_context_high->crypto_major_24h` score `6.905` n `115` status `ready` deltaP `18.513` edge `1.1511` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.4334` n `136` status `ready` deltaP `20.7675` edge `0.3753` maxDD `-1.8773`
- `market_context_high->index_4h` score `3.924` n `136` status `ready` deltaP `30.1291` edge `0.1637` maxDD `-0.3385`
- `news_risk_high->index_24h` score `3.8505` n `43` status `ready` deltaP `12.924` edge `0.2766` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.7781` n `43` status `ready` deltaP `32.3099` edge `0.3361` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.6639` n `43` status `ready` deltaP `37.2295` edge `0.0756` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.4608` n `115` status `ready` deltaP `14.7238` edge `0.242` maxDD `-1.4737`
- `market_context_high->equity_24h` score `3.268` n `115` status `ready` deltaP `22.3702` edge `0.2759` maxDD `-6.8828`
- `news_risk_high->commodity_24h` score `2.9128` n `43` status `ready` deltaP `1.6836` edge `0.3132` maxDD `-3.202`
- `market_context_high->equity_4h` score `2.457` n `136` status `ready` deltaP `19.6019` edge `0.2089` maxDD `-5.4528`
- `news_risk_high->fx_4h` score `2.0697` n `43` status `ready` deltaP `26.3648` edge `0.0151` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `1.8748` n `148` status `ready` deltaP `13.2101` edge `0.1869` maxDD `-6.1656`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
