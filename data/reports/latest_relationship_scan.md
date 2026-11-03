# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T05:52:27.284790+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4558`

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

- `news_risk_high->crypto_alt_4h` score `0.2168` n `146` status `ready` deltaP `5.7802` edge `0.2529` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4495` n `146` status `ready` deltaP `1.8825` edge `0.0526` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.5953` n `146` status `ready` deltaP `-0.5762` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->metal_24h` score `-0.8883` n `131` status `ready` deltaP `12.182` edge `0.1305` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-0.9299` n `146` status `ready` deltaP `0.8982` edge `-0.0035` maxDD `-1.3981`
- `news_risk_high->fx_4h` score `-1.2087` n `146` status `ready` deltaP `-2.8963` edge `-0.0105` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2938` n `146` status `ready` deltaP `-5.098` edge `-0.0097` maxDD `-3.1082`
- `news_risk_high->crypto_alt_24h` score `-1.4271` n `131` status `ready` deltaP `21.9015` edge `0.8339` maxDD `-80.6962`
- `news_risk_high->index_24h` score `-2.1133` n `131` status `ready` deltaP `-2.3908` edge `0.0292` maxDD `-7.402`
- `news_risk_high->index_4h` score `-2.1192` n `146` status `ready` deltaP `-3.8841` edge `-0.0157` maxDD `-4.0745`
- `news_risk_high->equity_24h` score `-2.2324` n `131` status `ready` deltaP `17.0404` edge `0.6097` maxDD `-67.0937`
- `news_risk_high->commodity_1h` score `-2.3864` n `146` status `ready` deltaP `-9.0764` edge `-0.0017` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4336` n `131` status `ready` deltaP `-18.5751` edge `-0.0173` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.7046` n `146` status `ready` deltaP `-6.9354` edge `-0.0329` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2415` n `146` status `ready` deltaP `-8.3053` edge `-0.0422` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.782` n `146` status `ready` deltaP `-12.1701` edge `0.0014` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-4.8889` n `146` status `ready` deltaP `-7.7577` edge `-0.0352` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.0442` n `146` status `ready` deltaP `-14.2312` edge `-0.0902` maxDD `-24.1554`
- `news_risk_high->crypto_major_24h` score `-10.1937` n `131` status `ready` deltaP `-12.6921` edge `0.0594` maxDD `-53.6073`
- `news_risk_high->commodity_24h` score `-11.7827` n `131` status `ready` deltaP `-23.9305` edge `-0.0848` maxDD `-36.6713`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
