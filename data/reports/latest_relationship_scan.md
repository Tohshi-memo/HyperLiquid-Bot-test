# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T07:37:29.589626+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4790`

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

- `market_context_high->unknown_4h` score `125.1458` n `37` status `ready` deltaP `-4.5484` edge `10.5039` maxDD `-0.9139`
- `market_context_high->equity_1h` score `3.2808` n `37` status `ready` deltaP `10.6571` edge `0.2483` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.2351` n `37` status `ready` deltaP `34.9909` edge `0.0453` maxDD `-0.0521`
- `market_context_high->index_4h` score `2.0438` n `37` status `ready` deltaP `26.6604` edge `0.0396` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.7417` n `50` status `ready` deltaP `9.8611` edge `0.1015` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.8147` n `50` status `ready` deltaP `6.5915` edge `0.1344` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7987` n `37` status `ready` deltaP `9.9005` edge `0.0591` maxDD `-3.0172`
- `market_context_high->crypto_alt_1h` score `0.5184` n `37` status `ready` deltaP `11.6969` edge `0.07` maxDD `-3.1881`
- `market_context_high->fx_1h` score `0.4086` n `37` status `ready` deltaP `6.9227` edge `0.015` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.3225` n `37` status `ready` deltaP `2.2496` edge `0.0389` maxDD `-0.1621`
- `news_risk_high->index_4h` score `0.2916` n `50` status `ready` deltaP `9.5793` edge `0.0213` maxDD `-0.4888`
- `news_risk_high->fx_4h` score `0.2479` n `50` status `ready` deltaP `8.3963` edge `0.0081` maxDD `-0.1403`
- `news_risk_high->index_24h` score `0.1349` n `50` status `ready` deltaP `5.3125` edge `0.1487` maxDD `-6.6786`
- `market_context_high->commodity_1h` score `0.1273` n `37` status `ready` deltaP `9.1682` edge `0.0098` maxDD `-1.7019`
- `news_risk_high->index_1h` score `0.0607` n `53` status `ready` deltaP `7.502` edge `0.0031` maxDD `-0.2931`
- `market_context_high->commodity_4h` score `0.0382` n `37` status `ready` deltaP `3.9017` edge `0.0243` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.017` n `37` status `ready` deltaP `2.0999` edge `0.0166` maxDD `-0.6226`
- `news_risk_high->equity_1h` score `-0.0519` n `53` status `ready` deltaP `0.2542` edge `0.0466` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.1026` n `53` status `ready` deltaP `3.2511` edge `0.0037` maxDD `-0.0826`
- `market_context_high->equity_4h` score `-0.6378` n `37` status `ready` deltaP `22.8618` edge `0.0938` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
