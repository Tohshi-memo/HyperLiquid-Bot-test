# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T02:22:20.261591+00:00`
- Price records: `672`
- Market context records: `3239`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9724`

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

- `market_context_high->crypto_alt_24h` score `14.3211` n `103` status `ready` deltaP `18.8241` edge `2.6947` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `13.7063` n `103` status `ready` deltaP `49.3831` edge `0.8558` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.6642` n `103` status `ready` deltaP `32.0102` edge `0.8474` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.6303` n `103` status `ready` deltaP `19.5692` edge `1.5612` maxDD `-53.663`
- `risk_on_high->crypto_major_1h` score `2.632` n `31` status `ready` deltaP `10.8267` edge `0.3722` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.632` n `31` status `ready` deltaP `10.8267` edge `0.3722` maxDD `-5.8885`
- `market_context_high->crypto_major_24h` score `2.6154` n `103` status `ready` deltaP `22.8948` edge `2.2526` maxDD `-152.2601`
- `market_context_high->commodity_4h` score `1.8129` n `137` status `ready` deltaP `16.6637` edge `0.1358` maxDD `-3.9989`
- `risk_on_high->crypto_alt_1h` score `0.7402` n `31` status `ready` deltaP `4.0081` edge `0.2119` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.7402` n `31` status `ready` deltaP `4.0081` edge `0.2119` maxDD `-8.1649`
- `risk_on_high->metal_1h` score `0.4764` n `31` status `ready` deltaP `8.0645` edge `0.0758` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.4764` n `31` status `ready` deltaP `8.0645` edge `0.0758` maxDD `-1.4793`
- `risk_on_high->equity_1h` score `0.3508` n `31` status `ready` deltaP `2.6608` edge `0.1176` maxDD `-3.5625`
- `risk_on_and_context->equity_1h` score `0.3508` n `31` status `ready` deltaP `2.6608` edge `0.1176` maxDD `-3.5625`
- `risk_on_high->index_1h` score `-0.1126` n `31` status `ready` deltaP `0.1835` edge `0.0467` maxDD `-1.3216`
- `risk_on_and_context->index_1h` score `-0.1126` n `31` status `ready` deltaP `0.1835` edge `0.0467` maxDD `-1.3216`
- `market_context_high->commodity_1h` score `-0.3943` n `149` status `ready` deltaP `3.841` edge `0.0231` maxDD `-2.5251`
- `market_context_high->unknown_4h` score `-0.4793` n `137` status `ready` deltaP `10.0532` edge `0.0981` maxDD `-15.1257`
- `market_context_high->index_1h` score `-0.5516` n `149` status `ready` deltaP `3.4743` edge `0.0124` maxDD `-4.5023`
- `risk_on_high->fx_1h` score `-0.8111` n `31` status `ready` deltaP `-11.3724` edge `-0.0047` maxDD `-0.2106`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
