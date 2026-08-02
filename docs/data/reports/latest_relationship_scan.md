# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T09:07:22.823801+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5900`

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

- `news_risk_high->unknown_24h` score `5185.1997` n `60` status `ready` deltaP `30.8333` edge `431.9365` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.823` n `44` status `ready` deltaP `59.8327` edge `1.1261` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `7.765` n `44` status `ready` deltaP `42.4558` edge `0.4334` maxDD `-3.8815`
- `news_risk_high->equity_4h` score `4.5409` n `68` status `ready` deltaP `16.5261` edge `0.3446` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.589` n `68` status `ready` deltaP `15.6115` edge `0.0664` maxDD `-0.3783`
- `market_context_high->fx_4h` score `0.9732` n `44` status `ready` deltaP `20.3714` edge `0.0249` maxDD `-1.3685`
- `market_context_high->commodity_4h` score `0.8622` n `44` status `ready` deltaP `12.6109` edge `0.1111` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.6156` n `68` status `ready` deltaP `9.6425` edge `0.0693` maxDD `-2.916`
- `market_context_high->crypto_alt_4h` score `0.2913` n `44` status `ready` deltaP `4.8642` edge `0.0993` maxDD `-5.2176`
- `market_context_high->commodity_1h` score `0.2515` n `44` status `ready` deltaP `6.3419` edge `0.0274` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1936` n `44` status `ready` deltaP `10.8873` edge `0.0025` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.1686` n `68` status `ready` deltaP `12.7511` edge `0.0248` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1237` n `68` status `ready` deltaP `5.4698` edge `0.027` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.0757` n `68` status `ready` deltaP `6.1818` edge `0.0367` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.0427` n `68` status `ready` deltaP `3.267` edge `0.005` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0949` n `68` status `ready` deltaP `2.0166` edge `0.0067` maxDD `-0.5845`
- `news_risk_high->metal_1h` score `-0.1263` n `68` status `ready` deltaP `2.7651` edge `0.0057` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2233` n `68` status `ready` deltaP `2.2191` edge `0.0286` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.4378` n `44` status `ready` deltaP `0.2994` edge `0.0046` maxDD `-3.0178`
- `market_context_high->fx_24h` score `-0.5795` n `44` status `ready` deltaP `2.4306` edge `0.0335` maxDD `-2.506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
