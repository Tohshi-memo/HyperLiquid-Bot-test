# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T07:22:26.223114+00:00`
- Price records: `672`
- Market context records: `2119`
- Flow alert records: `7997`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9149`

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

- `market_context_high->crypto_alt_4h` score `13.0883` n `162` status `ready` deltaP `37.1594` edge `0.9366` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.8801` n `162` status `ready` deltaP `41.6403` edge `0.7654` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.1331` n `162` status `ready` deltaP `24.6914` edge `0.4214` maxDD `-2.6599`
- `market_context_high->equity_4h` score `5.0507` n `162` status `ready` deltaP `26.0313` edge `0.3568` maxDD `-5.0894`
- `market_context_high->metal_4h` score `3.137` n `162` status `ready` deltaP `21.3999` edge `0.2575` maxDD `-4.7664`
- `market_context_high->index_4h` score `3.0711` n `162` status `ready` deltaP `22.1827` edge `0.1764` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.8346` n `161` status `ready` deltaP `12.3837` edge `0.2765` maxDD `-4.1604`
- `news_risk_high->unknown_1h` score `2.7766` n `30` status `ready` deltaP `31.2375` edge `0.0534` maxDD `-1.7548`
- `market_context_high->crypto_major_1h` score `2.7054` n `162` status `ready` deltaP `16.2748` edge `0.1925` maxDD `-2.7108`
- `market_context_high->crypto_alt_1h` score `2.6088` n `162` status `ready` deltaP `13.5802` edge `0.2174` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.9305` n `161` status `ready` deltaP `23.7626` edge `0.4923` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.6273` n `161` status `ready` deltaP `24.2021` edge `0.5063` maxDD `-35.8966`
- `news_risk_high->commodity_1h` score `0.9875` n `30` status `ready` deltaP `9.7006` edge `0.0856` maxDD `-2.1052`
- `market_context_high->crypto_major_24h` score `0.9412` n `161` status `ready` deltaP `20.5582` edge `0.8422` maxDD `-62.3533`
- `market_context_high->equity_1h` score `0.6819` n `162` status `ready` deltaP `9.1447` edge `0.0747` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.4195` n `162` status `ready` deltaP `7.838` edge `0.0497` maxDD `-2.3594`
- `market_context_high->unknown_1h` score `0.1266` n `162` status `ready` deltaP `5.3116` edge `0.0471` maxDD `-3.0902`
- `news_risk_high->fx_1h` score `0.0656` n `30` status `ready` deltaP `3.6327` edge `0.0069` maxDD `-0.0524`
- `market_context_high->metal_24h` score `-0.0227` n `161` status `ready` deltaP `10.8158` edge `0.3151` maxDD `-23.2095`
- `market_context_high->index_1h` score `-0.0769` n `162` status `ready` deltaP `3.5152` edge `0.0292` maxDD `-1.3898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
