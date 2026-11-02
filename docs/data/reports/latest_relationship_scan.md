# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T08:22:30.181322+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4849`

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

- `market_context_high->unknown_4h` score `734.6621` n `34` status `ready` deltaP `8.8415` edge `61.1629` maxDD `0.0`
- `market_context_high->unknown_1h` score `196.9357` n `34` status `ready` deltaP `7.0448` edge `16.3754` maxDD `-0.2178`
- `news_risk_high->crypto_alt_24h` score `6.3117` n `103` status `ready` deltaP `27.7727` edge `0.8921` maxDD `-17.4445`
- `market_context_high->equity_4h` score `5.5358` n `34` status `ready` deltaP `7.9537` edge `0.4785` maxDD `-2.283`
- `market_context_high->crypto_alt_4h` score `5.5154` n `34` status `ready` deltaP `24.3813` edge `0.3265` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `4.2989` n `34` status `ready` deltaP `21.7001` edge `0.2472` maxDD `-1.6901`
- `market_context_high->equity_1h` score `3.5146` n `34` status `ready` deltaP `11.615` edge `0.2555` maxDD `-1.2043`
- `news_risk_high->crypto_alt_4h` score `2.7305` n `126` status `ready` deltaP `10.8425` edge `0.2939` maxDD `-7.4246`
- `market_context_high->index_4h` score `2.5788` n `34` status `ready` deltaP `24.6862` edge `0.073` maxDD `-0.1474`
- `market_context_high->crypto_major_1h` score `2.1577` n `34` status `ready` deltaP `11.615` edge `0.1414` maxDD `-1.1219`
- `market_context_high->crypto_alt_1h` score `1.3857` n `34` status `ready` deltaP `9.572` edge `0.158` maxDD `-1.5324`
- `market_context_high->fx_1h` score `1.0775` n `34` status `ready` deltaP `14.2568` edge `0.0119` maxDD `-0.0388`
- `market_context_high->commodity_4h` score `0.9691` n `34` status `ready` deltaP `19.9337` edge `0.0326` maxDD `-1.633`
- `market_context_high->metal_4h` score `0.7677` n `34` status `ready` deltaP `14.3113` edge `0.0455` maxDD `-0.7323`
- `market_context_high->index_1h` score `0.5185` n `34` status `ready` deltaP `4.8345` edge `0.0351` maxDD `-0.2628`
- `market_context_high->metal_1h` score `0.1345` n `34` status `ready` deltaP `4.1916` edge `0.015` maxDD `-0.3895`
- `news_risk_high->crypto_alt_1h` score `-0.3378` n `137` status `ready` deltaP `1.8434` edge `0.0517` maxDD `-4.584`
- `market_context_high->fx_4h` score `-0.382` n `34` status `ready` deltaP `-1.2195` edge `0.0154` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `-0.5758` n `34` status `ready` deltaP `-4.5351` edge `0.0103` maxDD `-0.6439`
- `news_risk_high->fx_1h` score `-0.6147` n `137` status `ready` deltaP `-0.8141` edge `-0.0033` maxDD `-0.6065`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
