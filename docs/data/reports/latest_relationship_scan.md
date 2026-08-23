# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T03:07:25.685250+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `news_risk_high->unknown_4h` score `12.9152` n `34` status `ready` deltaP `29.7256` edge `0.8781` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.7037` n `34` status `ready` deltaP `47.2561` edge `0.2436` maxDD `0.0`
- `news_risk_high->unknown_1h` score `5.4422` n `46` status `ready` deltaP `28.5797` edge `0.2748` maxDD `-0.2787`
- `news_risk_high->fx_4h` score `3.1759` n `34` status `ready` deltaP `37.2131` edge `0.03` maxDD `-0.0746`
- `news_risk_high->metal_4h` score `2.0917` n `34` status `ready` deltaP `26.91` edge `0.0033` maxDD `-0.0045`
- `market_context_high->unknown_1h` score `1.5273` n `135` status `ready` deltaP `6.1643` edge `0.1089` maxDD `-0.4843`
- `news_risk_high->fx_1h` score `1.4698` n `46` status `ready` deltaP `19.8711` edge `0.007` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.279` n `46` status `ready` deltaP `24.8178` edge `0.0267` maxDD `-0.9204`
- `market_context_high->unknown_4h` score `0.9976` n `135` status `ready` deltaP `20.096` edge `-0.0295` maxDD `-0.3736`
- `news_risk_high->index_4h` score `0.4615` n `34` status `ready` deltaP `11.1101` edge `0.0237` maxDD `-0.0884`
- `news_risk_high->commodity_1h` score `0.3311` n `46` status `ready` deltaP `12.3731` edge `-0.0092` maxDD `-0.4666`
- `market_context_high->fx_4h` score `0.1039` n `135` status `ready` deltaP `8.2588` edge `0.0085` maxDD `-0.3527`
- `news_risk_high->index_1h` score `0.0707` n `46` status `ready` deltaP `6.2223` edge `0.0029` maxDD `-0.1583`
- `news_risk_high->metal_1h` score `0.0576` n `46` status `ready` deltaP `5.4738` edge `-0.0068` maxDD `-0.1184`
- `market_context_high->index_1h` score `-0.0703` n `135` status `ready` deltaP `5.9969` edge `0.0041` maxDD `-0.9144`
- `news_risk_high->crypto_major_4h` score `-0.1543` n `34` status `ready` deltaP `-2.4121` edge `0.1399` maxDD `-6.9344`
- `market_context_high->fx_1h` score `-0.1669` n `135` status `ready` deltaP `1.5137` edge `0.0044` maxDD `-0.2043`
- `news_risk_high->commodity_4h` score `-0.2403` n `34` status `ready` deltaP `5.6044` edge `-0.022` maxDD `-1.0273`
- `market_context_high->equity_1h` score `-0.3509` n `135` status `ready` deltaP `4.3347` edge `0.0331` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.4559` n `135` status `ready` deltaP `6.0603` edge `-0.0168` maxDD `-1.5942`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
