# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T00:37:29.868000+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11618`

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

- `market_context_high->crypto_major_24h` score `2.4185` n `91` status `ready` deltaP `8.1197` edge `0.2682` maxDD `-4.9964`
- `market_context_high->equity_1h` score `1.5324` n `96` status `ready` deltaP `12.6061` edge `0.0738` maxDD `-0.4112`
- `market_context_high->equity_4h` score `1.4812` n `96` status `ready` deltaP `8.562` edge `0.1552` maxDD `-2.4411`
- `market_context_high->commodity_24h` score `1.478` n `91` status `ready` deltaP `17.2066` edge `0.2581` maxDD `-4.666`
- `market_context_high->metal_4h` score `1.1794` n `96` status `ready` deltaP `17.7845` edge `0.0373` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.9231` n `96` status `ready` deltaP `10.8485` edge `0.1067` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.7785` n `96` status `ready` deltaP `14.1155` edge `0.0095` maxDD `-0.0982`
- `market_context_high->crypto_alt_4h` score `0.5141` n `96` status `ready` deltaP `11.5854` edge `0.0926` maxDD `-5.4926`
- `market_context_high->unknown_1h` score `0.4938` n `96` status `ready` deltaP `9.6557` edge `-0.0005` maxDD `-0.4843`
- `market_context_high->unknown_24h` score `0.2164` n `91` status `ready` deltaP `15.6918` edge `-0.0652` maxDD `-0.3771`
- `market_context_high->metal_1h` score `0.12` n `96` status `ready` deltaP `5.6699` edge `0.0109` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.1078` n `96` status `ready` deltaP `5.3607` edge `0.0007` maxDD `-0.3539`
- `market_context_high->index_4h` score `-0.168` n `96` status `ready` deltaP `4.9034` edge `0.0188` maxDD `-0.5728`
- `market_context_high->crypto_alt_1h` score `-0.3707` n `96` status `ready` deltaP `2.6759` edge `0.0148` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.4156` n `96` status `ready` deltaP `-2.8194` edge `0.0014` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.4468` n `96` status `ready` deltaP `1.7839` edge `0.0153` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.4573` n `96` status `ready` deltaP `2.5661` edge `0.0093` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.897` n `96` status `ready` deltaP `-7.8905` edge `-0.0058` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-1.7015` n `91` status `ready` deltaP `-2.1138` edge `0.073` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.0451` n `91` status `ready` deltaP `-24.2617` edge `-0.0254` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
