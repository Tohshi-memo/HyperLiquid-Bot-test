# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T07:07:29.018600+00:00`
- Price records: `672`
- Market context records: `7225`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13702`

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

- `risk_on_high->crypto_major_4h` score `5.8001` n `34` status `ready` deltaP `26.3182` edge `0.3462` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `5.8001` n `34` status `ready` deltaP `26.3182` edge `0.3462` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.2905` n `34` status `ready` deltaP `17.2525` edge `0.2818` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.2905` n `34` status `ready` deltaP `17.2525` edge `0.2818` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.1155` n `34` status `ready` deltaP `22.7281` edge `0.0398` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.1155` n `34` status `ready` deltaP `22.7281` edge `0.0398` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.0454` n `34` status `ready` deltaP `4.9856` edge `0.1382` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.0454` n `34` status `ready` deltaP `4.9856` edge `0.1382` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.2567` n `34` status `ready` deltaP `7.4762` edge `0.0121` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.2567` n `34` status `ready` deltaP `7.4762` edge `0.0121` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.2244` n `34` status `ready` deltaP `2.7474` edge `0.0304` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.2244` n `34` status `ready` deltaP `2.7474` edge `0.0304` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.1137` n `34` status `ready` deltaP `4.4387` edge `0.0157` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.1137` n `34` status `ready` deltaP `4.4387` edge `0.0157` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.3781` n `178` status `ready` deltaP `2.5096` edge `0.0007` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.5602` n `178` status `ready` deltaP `0.1901` edge `-0.011` maxDD `-1.9668`
- `risk_on_high->commodity_4h` score `-0.5615` n `34` status `ready` deltaP `0.8967` edge `-0.01` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.5615` n `34` status `ready` deltaP `0.8967` edge `-0.01` maxDD `-0.7546`
- `market_context_high->crypto_major_1h` score `-0.6597` n `178` status `ready` deltaP `4.2707` edge `0.028` maxDD `-7.6171`
- `market_context_high->crypto_alt_1h` score `-0.6602` n `178` status `ready` deltaP `0.3364` edge `0.017` maxDD `-5.9775`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
