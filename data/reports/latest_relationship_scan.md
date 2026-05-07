# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T23:22:14.841902+00:00`
- Price records: `593`
- Market context records: `695`
- Flow alert records: `1965`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `10.3066` n `146` status `ready` deltaP `25.1812` edge `0.7244` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6083` n `146` status `ready` deltaP `8.3694` edge `0.4997` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1945` n `149` status `ready` deltaP `7.4563` edge `0.0125` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2625` n `149` status `ready` deltaP `3.1882` edge `0.0029` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5133` n `149` status `ready` deltaP `2.1557` edge `0.0403` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5799` n `149` status `ready` deltaP `0.9155` edge `0.0049` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.0987` n `149` status `ready` deltaP `-1.2941` edge `-0.0019` maxDD `-4.4826`
- `market_context_high->crypto_major_4h` score `-1.1994` n `149` status `ready` deltaP `15.5305` edge `0.1133` maxDD `-22.648`
- `market_context_high->unknown_1h` score `-1.2264` n `149` status `ready` deltaP `-4.4793` edge `-0.012` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3786` n `149` status `ready` deltaP `4.5133` edge `-0.0135` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.4557` n `146` status `ready` deltaP `-4.3499` edge `0.1072` maxDD `-5.9609`
- `market_context_high->index_4h` score `-1.6172` n `149` status `ready` deltaP `2.8509` edge `-0.0015` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.6206` n `149` status `ready` deltaP `6.0973` edge `-0.0034` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.9727` n `149` status `ready` deltaP `4.2432` edge `0.0643` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.6039` n `149` status `ready` deltaP `-0.9885` edge `0.0048` maxDD `-10.5498`
- `market_context_high->equity_24h` score `-2.7019` n `146` status `ready` deltaP `-6.4019` edge `0.078` maxDD `-10.5047`
- `market_context_high->metal_1h` score `-3.2866` n `149` status `ready` deltaP `-4.6888` edge `-0.0467` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7959` n `149` status `ready` deltaP `-6.1398` edge `0.0747` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.4428` n `149` status `ready` deltaP `2.2775` edge `-0.1976` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.9452` n `146` status `ready` deltaP `-10.7867` edge `-0.0449` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
