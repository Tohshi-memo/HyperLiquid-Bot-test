# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T03:22:15.555164+00:00`
- Price records: `672`
- Market context records: `1804`
- Flow alert records: `7090`
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

- `market_context_high->metal_24h` score `6.9157` n `183` status `ready` deltaP `28.051` edge `0.6319` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.5615` n `188` status `ready` deltaP `22.1848` edge `0.532` maxDD `-6.6486`
- `news_risk_high->commodity_4h` score `6.5005` n `30` status `ready` deltaP `29.563` edge `0.4101` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `5.6777` n `188` status `ready` deltaP `25.5157` edge `0.4774` maxDD `-7.2827`
- `market_context_high->unknown_4h` score `4.2303` n `188` status `ready` deltaP `16.5543` edge `0.4578` maxDD `-10.2508`
- `news_risk_high->commodity_1h` score `3.2554` n `30` status `ready` deltaP `24.7206` edge `0.1382` maxDD `-1.2043`
- `market_context_high->index_24h` score `3.2009` n `183` status `ready` deltaP `15.5965` edge `0.2856` maxDD `-4.1604`
- `market_context_high->equity_4h` score `2.9732` n `188` status `ready` deltaP `16.3077` edge `0.2485` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.3686` n `183` status `ready` deltaP `17.6144` edge `0.5698` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.634` n `183` status `ready` deltaP `12.1812` edge `0.587` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.9042` n `30` status `ready` deltaP `21.6362` edge `-0.0011` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8572` n `188` status `ready` deltaP `12.2146` edge `0.0989` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.419` n `189` status `ready` deltaP `6.335` edge `0.0913` maxDD `-3.2225`
- `news_risk_high->unknown_4h` score `0.3594` n `30` status `ready` deltaP `9.6748` edge `0.0539` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `0.3029` n `189` status `ready` deltaP `6.7944` edge `0.0911` maxDD `-4.8924`
- `market_context_high->equity_1h` score `-0.1477` n `189` status `ready` deltaP `3.9707` edge `0.0406` maxDD `-2.6836`
- `market_context_high->index_1h` score `-0.401` n `189` status `ready` deltaP `2.2131` edge `0.015` maxDD `-1.7205`
- `market_context_high->fx_24h` score `-0.4511` n `183` status `ready` deltaP `8.8826` edge `0.0081` maxDD `-1.3925`
- `news_risk_high->fx_1h` score `-0.4632` n `30` status `ready` deltaP `-4.98` edge `0.0` maxDD `-0.0948`
- `news_risk_high->unknown_1h` score `-0.4699` n `30` status `ready` deltaP `16.5569` edge `-0.1234` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
