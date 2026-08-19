# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T03:22:29.965099+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11618`

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

- `market_context_high->crypto_major_24h` score `2.1778` n `93` status `ready` deltaP `7.0453` edge `0.2553` maxDD `-4.9964`
- `market_context_high->equity_1h` score `1.5875` n `96` status `ready` deltaP `13.2049` edge `0.0744` maxDD `-0.4112`
- `market_context_high->equity_4h` score `1.5332` n `96` status `ready` deltaP `8.8668` edge `0.1575` maxDD `-2.4411`
- `market_context_high->commodity_24h` score `1.3368` n `93` status `ready` deltaP `16.0058` edge `0.248` maxDD `-4.666`
- `market_context_high->metal_4h` score `1.172` n `96` status `ready` deltaP `17.6321` edge `0.0377` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.9645` n `96` status `ready` deltaP `11.3059` edge `0.1071` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.8719` n `96` status `ready` deltaP `15.1634` edge `0.0103` maxDD `-0.0982`
- `market_context_high->crypto_alt_4h` score `0.4259` n `96` status `ready` deltaP `11.128` edge `0.0883` maxDD `-5.4926`
- `market_context_high->unknown_1h` score `0.3295` n `96` status `ready` deltaP `9.2066` edge `-0.0112` maxDD `-0.4843`
- `market_context_high->metal_1h` score `0.1512` n `96` status `ready` deltaP `5.9693` edge `0.0115` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `0.0223` n `93` status `ready` deltaP `15.0874` edge `-0.0661` maxDD `-0.6099`
- `market_context_high->fx_4h` score `-0.0288` n `96` status `ready` deltaP `6.5803` edge `0.0027` maxDD `-0.3539`
- `market_context_high->index_4h` score `-0.0355` n `96` status `ready` deltaP `6.2754` edge `0.0207` maxDD `-0.5728`
- `market_context_high->crypto_alt_1h` score `-0.3177` n `96` status `ready` deltaP `3.4244` edge `0.0166` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.3292` n `96` status `ready` deltaP `-1.3224` edge `0.0025` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.3946` n `96` status `ready` deltaP `2.5324` edge `0.017` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.4873` n `96` status `ready` deltaP `2.1088` edge `0.0085` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8713` n `96` status `ready` deltaP `-7.4414` edge `-0.0055` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-1.8461` n `93` status `ready` deltaP `-2.0329` edge `0.0762` maxDD `-9.9458`
- `market_context_high->fx_24h` score `-4.1424` n `93` status `ready` deltaP `-24.7816` edge `-0.027` maxDD `-1.5722`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
