# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T03:22:14.058162+00:00`
- Price records: `672`
- Market context records: `1181`
- Flow alert records: `5304`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `19.2265` n `144` status `ready` deltaP `44.4445` edge `1.4191` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `8.8466` n `144` status `ready` deltaP `22.2223` edge `0.7907` maxDD `-15.1306`
- `market_context_high->metal_24h` score `4.8776` n `144` status `ready` deltaP `-2.7778` edge `0.5917` maxDD `-6.3373`
- `market_context_high->equity_24h` score `3.9577` n `144` status `ready` deltaP `16.8403` edge `0.4114` maxDD `-12.1758`
- `market_context_high->index_24h` score `3.7005` n `144` status `ready` deltaP `16.493` edge `0.283` maxDD `-4.433`
- `market_context_high->equity_4h` score `2.7403` n `147` status `ready` deltaP `14.3386` edge `0.1991` maxDD `-3.6396`
- `market_context_high->unknown_4h` score `1.5366` n `147` status `ready` deltaP `5.7004` edge `0.2117` maxDD `-6.7322`
- `market_context_high->index_4h` score `1.2078` n `147` status `ready` deltaP `10.2683` edge `0.1005` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.7607` n `147` status `ready` deltaP `10.0778` edge `0.0279` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3979` n `147` status `ready` deltaP `3.438` edge `0.048` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.013` n `147` status `ready` deltaP `7.1011` edge `-0.0001` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.0554` n `147` status `ready` deltaP `7.6821` edge `0.1338` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.1721` n `147` status `ready` deltaP `7.7397` edge `-0.0049` maxDD `-2.2164`
- `market_context_high->crypto_major_1h` score `-0.1737` n `147` status `ready` deltaP `5.1153` edge `0.0202` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.3624` n `147` status `ready` deltaP `0.8422` edge `0.0322` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.9325` n `147` status `ready` deltaP `-4.8026` edge `-0.0082` maxDD `-3.6798`
- `market_context_high->fx_4h` score `-1.1018` n `147` status `ready` deltaP `-5.3706` edge `-0.0071` maxDD `-1.5352`
- `market_context_high->fx_24h` score `-1.3214` n `144` status `ready` deltaP `4.3403` edge `0.0121` maxDD `-10.5019`
- `market_context_high->crypto_alt_4h` score `-1.3912` n `147` status `ready` deltaP `3.2158` edge `0.0967` maxDD `-16.7194`
- `market_context_high->unknown_24h` score `-1.7428` n `144` status `ready` deltaP `4.3403` edge `0.0988` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
