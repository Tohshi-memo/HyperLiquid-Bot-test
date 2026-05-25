# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T02:22:13.746008+00:00`
- Price records: `672`
- Market context records: `1800`
- Flow alert records: `7078`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8872`

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

- `market_context_high->metal_24h` score `6.9761` n `187` status `ready` deltaP `28.4016` edge `0.6346` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.4666` n `30` status `ready` deltaP `29.2582` edge `0.4093` maxDD `-3.5713`
- `market_context_high->crypto_alt_4h` score `5.732` n `191` status `ready` deltaP `21.1179` edge `0.5135` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.7637` n `191` status `ready` deltaP `24.0271` edge `0.4586` maxDD `-9.7443`
- `market_context_high->unknown_4h` score `4.1016` n `191` status `ready` deltaP `16.2798` edge `0.4489` maxDD `-10.2508`
- `news_risk_high->commodity_1h` score `3.2326` n `30` status `ready` deltaP `24.5709` edge `0.1373` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.8695` n `191` status `ready` deltaP `15.9415` edge `0.2423` maxDD `-5.0894`
- `market_context_high->index_24h` score `2.8093` n `187` status `ready` deltaP `13.8666` edge `0.2645` maxDD `-4.1604`
- `market_context_high->equity_24h` score `1.8099` n `187` status `ready` deltaP `16.4503` edge `0.531` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.0904` n `187` status `ready` deltaP `11.7907` edge `0.5443` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.898` n `30` status `ready` deltaP `21.6362` edge `-0.0019` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8252` n `191` status `ready` deltaP `11.9652` edge `0.0979` maxDD `-3.7119`
- `news_risk_high->unknown_4h` score `0.3753` n `30` status `ready` deltaP `9.9796` edge `0.0539` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `0.294` n `192` status `ready` deltaP `5.4173` edge `0.087` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.2683` n `192` status `ready` deltaP `6.6024` edge `0.0895` maxDD `-4.8924`
- `market_context_high->equity_1h` score `-0.2263` n `192` status `ready` deltaP `3.6739` edge `0.0375` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.4225` n `192` status `ready` deltaP `1.9742` edge `0.0148` maxDD `-1.7205`
- `news_risk_high->unknown_1h` score `-0.4442` n `30` status `ready` deltaP `16.8563` edge `-0.1221` maxDD `-2.1115`
- `news_risk_high->fx_1h` score `-0.464` n `30` status `ready` deltaP `-4.98` edge `-0.0001` maxDD `-0.0948`
- `market_context_high->fx_24h` score `-0.4643` n `187` status `ready` deltaP `8.4921` edge `0.0096` maxDD `-1.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
