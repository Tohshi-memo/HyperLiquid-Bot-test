# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T10:22:31.374802+00:00`
- Price records: `672`
- Market context records: `7239`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13725`

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

- `risk_on_high->crypto_major_4h` score `5.9041` n `34` status `ready` deltaP `26.9279` edge `0.3508` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `5.9041` n `34` status `ready` deltaP `26.9279` edge `0.3508` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.3086` n `34` status `ready` deltaP `17.4049` edge `0.2823` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.3086` n `34` status `ready` deltaP `17.4049` edge `0.2823` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.1084` n `34` status `ready` deltaP `22.5784` edge `0.0402` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.1084` n `34` status `ready` deltaP `22.5784` edge `0.0402` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.0274` n `34` status `ready` deltaP `4.9856` edge `0.1367` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.0274` n `34` status `ready` deltaP `4.9856` edge `0.1367` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.2879` n `34` status `ready` deltaP `7.7756` edge `0.0141` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.2879` n `34` status `ready` deltaP `7.7756` edge `0.0141` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.2232` n `34` status `ready` deltaP `2.7474` edge `0.0303` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.2232` n `34` status `ready` deltaP `2.7474` edge `0.0303` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.1264` n `34` status `ready` deltaP `3.2192` edge `0.0222` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.1264` n `34` status `ready` deltaP `3.2192` edge `0.0222` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.2107` n `165` status `ready` deltaP `3.1836` edge `0.0007` maxDD `-0.5817`
- `risk_on_high->commodity_4h` score `-0.626` n `34` status `ready` deltaP `0.1345` edge `-0.0103` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.626` n `34` status `ready` deltaP `0.1345` edge `-0.0103` maxDD `-0.7546`
- `market_context_high->commodity_1h` score `-0.6494` n `165` status `ready` deltaP `-1.1649` edge `-0.0134` maxDD `-1.9668`
- `market_context_high->crypto_alt_1h` score `-0.7335` n `165` status `ready` deltaP `-0.7739` edge `0.015` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.7571` n `165` status `ready` deltaP `2.8915` edge `0.0247` maxDD `-7.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
