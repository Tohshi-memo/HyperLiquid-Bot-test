# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T22:07:27.589690+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4092`

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

- `news_risk_high->equity_4h` score `1.3589` n `82` status `ready` deltaP `12.0427` edge `0.1845` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.6059` n `82` status `ready` deltaP `11.8902` edge `0.019` maxDD `-0.4888`
- `news_risk_high->equity_1h` score `0.3319` n `82` status `ready` deltaP `5.9698` edge `0.0577` maxDD `-1.396`
- `news_risk_high->index_1h` score `0.2986` n `82` status `ready` deltaP `11.8519` edge `0.0046` maxDD `-0.2931`
- `news_risk_high->fx_4h` score `0.0538` n `82` status `ready` deltaP `7.3171` edge `0.0027` maxDD `-0.2336`
- `news_risk_high->index_24h` score `-0.1586` n `82` status `ready` deltaP `0.9722` edge `0.14` maxDD `-6.6786`
- `news_risk_high->fx_1h` score `-0.2075` n `82` status `ready` deltaP `1.6066` edge `0.0013` maxDD `-0.0888`
- `news_risk_high->fx_24h` score `-0.2775` n `82` status `ready` deltaP `-1.7056` edge `0.0325` maxDD `-0.2073`
- `news_risk_high->metal_1h` score `-0.373` n `82` status `ready` deltaP `-1.0479` edge `-0.0051` maxDD `-0.5256`
- `news_risk_high->crypto_major_1h` score `-0.8099` n `82` status `ready` deltaP `-2.3331` edge `0.0056` maxDD `-4.1772`
- `news_risk_high->crypto_alt_1h` score `-0.877` n `82` status `ready` deltaP `1.026` edge `0.0035` maxDD `-5.8225`
- `news_risk_high->crypto_major_4h` score `-1.065` n `82` status `ready` deltaP `-2.1341` edge `0.0463` maxDD `-9.1553`
- `news_risk_high->metal_4h` score `-1.1708` n `82` status `ready` deltaP `-3.3537` edge `-0.0372` maxDD `-1.5773`
- `news_risk_high->equity_24h` score `-1.9615` n `82` status `ready` deltaP `24.8045` edge `0.7418` maxDD `-86.0244`
- `news_risk_high->crypto_alt_4h` score `-2.5035` n `82` status `ready` deltaP `-5.7927` edge `-0.0187` maxDD `-14.0916`
- `news_risk_high->commodity_1h` score `-2.9177` n `82` status `ready` deltaP `-17.8217` edge `-0.0066` maxDD `-1.7518`
- `news_risk_high->metal_24h` score `-3.0522` n `82` status `ready` deltaP `3.1344` edge `-0.2226` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-3.9965` n `82` status `ready` deltaP `-25.7622` edge `-0.0015` maxDD `-4.1171`
- `news_risk_high->commodity_24h` score `-9.3577` n `82` status `ready` deltaP `-26.1254` edge `-0.0322` maxDD `-28.5419`
- `news_risk_high->crypto_major_24h` score `-11.7385` n `82` status `ready` deltaP `-23.9823` edge `0.032` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
