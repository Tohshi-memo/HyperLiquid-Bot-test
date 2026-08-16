# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T13:22:28.878036+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11798`

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

- `market_context_high->unknown_24h` score `204.3883` n `88` status `ready` deltaP `-21.512` edge `26.6154` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `7.6117` n `88` status `ready` deltaP `41.3037` edge `0.3647` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.4746` n `123` status `ready` deltaP `14.2785` edge `0.0748` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.0915` n `125` status `ready` deltaP `2.0563` edge `0.0198` maxDD `-0.624`
- `market_context_high->fx_1h` score `-0.1721` n `125` status `ready` deltaP `0.7042` edge `0.0014` maxDD `-0.2527`
- `market_context_high->fx_4h` score `-0.2005` n `123` status `ready` deltaP `4.2683` edge `0.0063` maxDD `-0.504`
- `market_context_high->metal_1h` score `-0.5268` n `125` status `ready` deltaP `1.5042` edge `-0.006` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.8092` n `125` status `ready` deltaP `-7.2862` edge `-0.003` maxDD `-0.5064`
- `market_context_high->metal_4h` score `-0.9313` n `123` status `ready` deltaP `7.7236` edge `-0.0135` maxDD `-4.5909`
- `market_context_high->fx_24h` score `-1.555` n `88` status `ready` deltaP `-9.4066` edge `0.0241` maxDD `-1.8596`
- `market_context_high->equity_1h` score `-1.6541` n `125` status `ready` deltaP `-9.4335` edge `-0.0452` maxDD `-4.9849`
- `market_context_high->metal_24h` score `-1.7147` n `88` status `ready` deltaP `-6.4867` edge `0.0746` maxDD `-7.0954`
- `market_context_high->crypto_alt_1h` score `-1.9867` n `125` status `ready` deltaP `-1.5461` edge `-0.0213` maxDD `-7.0497`
- `market_context_high->index_24h` score `-1.9941` n `88` status `ready` deltaP `-5.019` edge `-0.0682` maxDD `-2.3194`
- `market_context_high->crypto_major_1h` score `-1.9989` n `125` status `ready` deltaP `-4.5497` edge `-0.0309` maxDD `-5.4277`
- `market_context_high->index_4h` score `-2.1372` n `123` status `ready` deltaP `-13.0589` edge `-0.0098` maxDD `-0.8328`
- `market_context_high->crypto_major_4h` score `-3.5653` n `123` status `ready` deltaP `0.3049` edge `-0.0634` maxDD `-13.1929`
- `market_context_high->crypto_major_24h` score `-4.6369` n `88` status `ready` deltaP `-3.267` edge `0.013` maxDD `-35.189`
- `market_context_high->unknown_1h` score `-7.194` n `125` status `ready` deltaP `-0.297` edge `-0.5518` maxDD `-1.3246`
- `market_context_high->crypto_alt_4h` score `-8.2524` n `123` status `ready` deltaP `-12.754` edge `-0.1148` maxDD `-26.3633`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
