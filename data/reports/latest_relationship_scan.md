# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T10:37:24.776584+00:00`
- Price records: `672`
- Market context records: `2654`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9223`

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

- `market_context_high->unknown_24h` score `7.9244` n `123` status `ready` deltaP `17.3992` edge `0.5772` maxDD `-1.626`
- `market_context_high->crypto_alt_24h` score `7.1151` n `123` status `ready` deltaP `11.3228` edge `0.8668` maxDD `-19.9486`
- `market_context_high->crypto_alt_4h` score `5.4009` n `123` status `ready` deltaP `25.6606` edge `0.5469` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.0893` n `123` status `ready` deltaP `16.3617` edge `0.4127` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.8764` n `123` status `ready` deltaP `10.4166` edge `0.1919` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.9687` n `133` status `ready` deltaP `9.0991` edge `0.1388` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.6859` n `123` status `ready` deltaP `10.0398` edge `0.0883` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.4456` n `133` status `ready` deltaP `6.8468` edge `0.1109` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.0678` n `123` status `ready` deltaP `8.1301` edge `0.0356` maxDD `-2.3986`
- `market_context_high->metal_4h` score `0.0083` n `123` status `ready` deltaP `6.7073` edge `0.0376` maxDD `-2.5301`
- `market_context_high->index_1h` score `-0.0576` n `133` status `ready` deltaP `4.455` edge `0.0149` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2189` n `133` status `ready` deltaP `1.7401` edge `0.0281` maxDD `-1.9684`
- `market_context_high->commodity_1h` score `-0.475` n `133` status `ready` deltaP `3.5298` edge `0.0034` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.5163` n `133` status `ready` deltaP `-1.2809` edge `0.0015` maxDD `-1.7326`
- `market_context_high->fx_24h` score `-0.521` n `123` status `ready` deltaP `6.6523` edge `-0.0002` maxDD `-0.672`
- `market_context_high->fx_1h` score `-0.612` n `133` status `ready` deltaP `-1.4205` edge `0.0031` maxDD `-0.2373`
- `market_context_high->fx_4h` score `-0.8887` n `123` status `ready` deltaP `-2.185` edge `0.0109` maxDD `-0.6315`
- `market_context_high->equity_1h` score `-1.0162` n `133` status `ready` deltaP `-2.5843` edge `0.0164` maxDD `-2.7085`
- `market_context_high->commodity_4h` score `-1.2047` n `123` status `ready` deltaP `3.7602` edge `0.0125` maxDD `-10.0279`
- `market_context_high->equity_24h` score `-1.3691` n `123` status `ready` deltaP `7.3891` edge `-0.0656` maxDD `-3.1535`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
