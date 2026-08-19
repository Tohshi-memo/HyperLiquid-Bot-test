# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T00:07:30.920305+00:00`
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

- `market_context_high->crypto_major_24h` score `2.4353` n `91` status `ready` deltaP `8.1197` edge `0.2696` maxDD `-4.9964`
- `market_context_high->equity_1h` score `1.5108` n `96` status `ready` deltaP `12.4564` edge `0.073` maxDD `-0.4112`
- `market_context_high->commodity_24h` score `1.4979` n `91` status `ready` deltaP `17.3802` edge `0.2595` maxDD `-4.666`
- `market_context_high->equity_4h` score `1.4076` n `96` status `ready` deltaP `8.2571` edge `0.1511` maxDD `-2.4411`
- `market_context_high->metal_4h` score `1.1478` n `96` status `ready` deltaP `17.4796` edge `0.0367` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.8915` n `96` status `ready` deltaP `10.5437` edge `0.1061` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.751` n `96` status `ready` deltaP `13.8161` edge `0.0092` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.4938` n `96` status `ready` deltaP `9.6557` edge `-0.0005` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.4887` n `96` status `ready` deltaP `11.4329` edge `0.0915` maxDD `-5.4926`
- `market_context_high->unknown_24h` score `0.2068` n `91` status `ready` deltaP `15.6918` edge `-0.066` maxDD `-0.3771`
- `market_context_high->metal_1h` score `0.12` n `96` status `ready` deltaP `5.6699` edge `0.0109` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.1252` n `96` status `ready` deltaP `5.0559` edge `0.0005` maxDD `-0.3539`
- `market_context_high->index_4h` score `-0.202` n `96` status `ready` deltaP `4.5985` edge `0.018` maxDD `-0.5728`
- `market_context_high->crypto_alt_1h` score `-0.3839` n `96` status `ready` deltaP `2.5262` edge `0.0141` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.4242` n `96` status `ready` deltaP `-2.9691` edge `0.0013` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.4596` n `96` status `ready` deltaP `2.5661` edge `0.009` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.4694` n `96` status `ready` deltaP `1.4845` edge `0.0144` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9063` n `96` status `ready` deltaP `-8.0402` edge `-0.006` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-1.7485` n `91` status `ready` deltaP `-2.461` edge `0.0693` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.0614` n `91` status `ready` deltaP `-24.4353` edge `-0.0256` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
