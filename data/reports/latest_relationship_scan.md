# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T20:36:18.409790+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11621`

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

- `market_context_high->crypto_major_24h` score `2.7098` n `91` status `ready` deltaP `9.8558` edge `0.2809` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.6346` n `91` status `ready` deltaP `18.9427` edge `0.2666` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.3371` n `96` status `ready` deltaP `10.9594` edge `0.0685` maxDD `-0.4112`
- `market_context_high->equity_4h` score `0.9873` n `96` status `ready` deltaP `6.1229` edge `0.1303` maxDD `-2.4411`
- `market_context_high->metal_4h` score `0.9027` n `96` status `ready` deltaP `15.3455` edge `0.0305` maxDD `-1.273`
- `market_context_high->index_1h` score `0.7234` n `96` status `ready` deltaP `13.5167` edge `0.0089` maxDD `-0.0982`
- `market_context_high->crypto_major_4h` score `0.666` n `96` status `ready` deltaP `8.7144` edge `0.0995` maxDD `-3.1677`
- `market_context_high->unknown_1h` score `0.5442` n `96` status `ready` deltaP `9.9551` edge `0.0017` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.168` n `96` status `ready` deltaP `9.2988` edge `0.079` maxDD `-5.4926`
- `market_context_high->unknown_24h` score `0.0634` n `91` status `ready` deltaP `14.6501` edge `-0.071` maxDD `-0.3771`
- `market_context_high->metal_1h` score `0.0517` n `96` status `ready` deltaP `4.9214` edge `0.0102` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.1941` n `96` status `ready` deltaP `3.8363` edge `-0.0002` maxDD `-0.3539`
- `market_context_high->crypto_alt_1h` score `-0.4042` n `96` status `ready` deltaP `2.2268` edge `0.0135` maxDD `-2.413`
- `market_context_high->index_4h` score `-0.41` n `96` status `ready` deltaP `2.4644` edge `0.0149` maxDD `-0.5728`
- `market_context_high->fx_1h` score `-0.4397` n `96` status `ready` deltaP `-3.2685` edge `0.0013` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.4627` n `96` status `ready` deltaP `2.5661` edge `0.0086` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.5192` n `96` status `ready` deltaP `0.736` edge `0.013` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8907` n `96` status `ready` deltaP `-7.7408` edge `-0.006` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.0542` n `91` status `ready` deltaP `-4.8916` edge `0.0463` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.2739` n `91` status `ready` deltaP `-26.8659` edge `-0.0271` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
