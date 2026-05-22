# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T19:07:21.049269+00:00`
- Price records: `672`
- Market context records: `1555`
- Flow alert records: `6388`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8813`

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

- `market_context_high->metal_24h` score `12.4648` n `182` status `ready` deltaP `23.8171` edge `0.98` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.851` n `182` status `ready` deltaP `26.9974` edge `0.9259` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.3189` n `182` status `ready` deltaP `26.7399` edge `0.7115` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.068` n `182` status `ready` deltaP `20.7799` edge `0.3091` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7818` n `182` status `ready` deltaP `14.4155` edge `0.3684` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.5614` n `182` status `ready` deltaP `15.314` edge `0.0496` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.3521` n `199` status `ready` deltaP `5.5483` edge `0.1018` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.1091` n `199` status `ready` deltaP `13.2545` edge `0.2296` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.2148` n `199` status `ready` deltaP `9.1272` edge `0.1825` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.3722` n `199` status `ready` deltaP `0.9674` edge `0.0482` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.6335` n `199` status `ready` deltaP `-2.1439` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.7048` n `199` status `ready` deltaP `-0.1978` edge `0.0031` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7423` n `199` status `ready` deltaP `5.1478` edge `0.0041` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.7908` n `199` status `ready` deltaP `-0.4235` edge `0.0001` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.796` n `199` status `ready` deltaP `-1.0328` edge `0.0214` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.9285` n `199` status `ready` deltaP `-0.7432` edge `0.0216` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.3736` n `199` status `ready` deltaP `-10.3973` edge `-0.0139` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.4079` n `199` status `ready` deltaP `10.0587` edge `0.0848` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.4668` n `199` status `ready` deltaP `-4.7448` edge `0.0183` maxDD `-3.7119`
- `market_context_high->commodity_4h` score `-5.0772` n `199` status `ready` deltaP `-13.9379` edge `-0.0953` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
