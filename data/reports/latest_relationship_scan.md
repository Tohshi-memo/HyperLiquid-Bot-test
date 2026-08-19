# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T00:22:22.678031+00:00`
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

- `market_context_high->crypto_major_24h` score `2.4245` n `91` status `ready` deltaP `8.1197` edge `0.2687` maxDD `-4.9964`
- `market_context_high->equity_1h` score `1.5312` n `96` status `ready` deltaP `12.6061` edge `0.0737` maxDD `-0.4112`
- `market_context_high->commodity_24h` score `1.4933` n `91` status `ready` deltaP `17.3802` edge `0.2589` maxDD `-4.666`
- `market_context_high->equity_4h` score `1.4462` n `96` status `ready` deltaP `8.4095` edge `0.1533` maxDD `-2.4411`
- `market_context_high->metal_4h` score `1.1636` n `96` status `ready` deltaP `17.6321` edge `0.037` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.9061` n `96` status `ready` deltaP `10.6961` edge `0.1063` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.7653` n `96` status `ready` deltaP `13.9658` edge `0.0094` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5082` n `96` status `ready` deltaP `9.8054` edge `-0.0003` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.4935` n `96` status `ready` deltaP `11.4329` edge `0.0919` maxDD `-5.4926`
- `market_context_high->unknown_24h` score `0.2116` n `91` status `ready` deltaP `15.6918` edge `-0.0656` maxDD `-0.3771`
- `market_context_high->metal_1h` score `0.12` n `96` status `ready` deltaP `5.6699` edge `0.0109` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.1165` n `96` status `ready` deltaP `5.2083` edge `0.0006` maxDD `-0.3539`
- `market_context_high->index_4h` score `-0.185` n `96` status `ready` deltaP `4.751` edge `0.0184` maxDD `-0.5728`
- `market_context_high->crypto_alt_1h` score `-0.3824` n `96` status `ready` deltaP `2.5262` edge `0.0143` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.4156` n `96` status `ready` deltaP `-2.8194` edge `0.0014` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.458` n `96` status `ready` deltaP `2.5661` edge `0.0092` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.4593` n `96` status `ready` deltaP `1.6342` edge `0.0147` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.897` n `96` status `ready` deltaP `-7.8905` edge `-0.0058` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-1.7254` n `91` status `ready` deltaP `-2.2874` edge `0.0711` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.0463` n `91` status `ready` deltaP `-24.2617` edge `-0.0255` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
