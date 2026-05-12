# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-12T00:37:23.628665+00:00`
- Price records: `672`
- Market context records: `986`
- Flow alert records: `3181`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `13.1066` n `210` status `ready` deltaP `31.2011` edge `0.9176` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.4834` n `210` status `ready` deltaP `10.597` edge `0.3863` maxDD `0.0`
- `market_context_high->commodity_1h` score `-0.4238` n `210` status `ready` deltaP `3.2042` edge `0.0241` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.5818` n `210` status `ready` deltaP `1.5577` edge `-0.0008` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.6478` n `210` status `ready` deltaP `1.122` edge `0.0154` maxDD `-4.4826`
- `market_context_high->index_24h` score `-0.7165` n `210` status `ready` deltaP `2.715` edge `0.1217` maxDD `-5.9609`
- `market_context_high->fx_4h` score `-0.7229` n `210` status `ready` deltaP `0.924` edge `0.0008` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.7601` n `210` status `ready` deltaP `2.7614` edge `0.0036` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1619` n `210` status `ready` deltaP `-0.9978` edge `-0.013` maxDD `-3.5069`
- `market_context_high->crypto_major_1h` score `-1.23` n `210` status `ready` deltaP `4.8619` edge `-0.0178` maxDD `-11.4508`
- `market_context_high->equity_24h` score `-1.2573` n `210` status `ready` deltaP `4.2004` edge `0.1277` maxDD `-10.5047`
- `market_context_high->equity_4h` score `-1.5753` n `210` status `ready` deltaP `1.4144` edge `0.0745` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.8016` n `210` status `ready` deltaP `-2.1251` edge `0.0163` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.9634` n `210` status `ready` deltaP `-1.5428` edge `-0.0455` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-2.1722` n `210` status `ready` deltaP `-0.6522` edge `-0.0327` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.9551` n `210` status `ready` deltaP `7.0718` edge `0.0772` maxDD `-22.648`
- `market_context_high->unknown_4h` score `-3.2154` n `210` status `ready` deltaP `7.5551` edge `-0.1305` maxDD `-8.3588`
- `market_context_high->commodity_4h` score `-3.2775` n `210` status `ready` deltaP `-2.1251` edge `0.0578` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.4756` n `210` status `ready` deltaP `-2.3738` edge `0.004` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.5662` n `210` status `ready` deltaP `-1.1372` edge `-0.0217` maxDD `-20.2343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
