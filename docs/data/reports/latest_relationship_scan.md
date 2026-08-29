# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T00:22:26.609302+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `56.2098` n `50` status `ready` deltaP `17.6776` edge `4.5663` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.4963` n `50` status `ready` deltaP `46.6066` edge `2.6081` maxDD `-2.8629`
- `news_risk_high->crypto_major_24h` score `8.9799` n `50` status `ready` deltaP `26.2877` edge `0.6224` maxDD `-2.6128`
- `news_risk_high->unknown_4h` score `8.7507` n `71` status `ready` deltaP `17.5863` edge `0.643` maxDD `-1.4812`
- `news_risk_high->equity_24h` score `6.6871` n `50` status `ready` deltaP `30.1005` edge `0.4494` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `5.5185` n `120` status `ready` deltaP `11.0109` edge `0.4597` maxDD `-3.1917`
- `news_risk_high->metal_24h` score `4.4646` n `50` status `ready` deltaP `43.4073` edge `0.0869` maxDD `-0.0053`
- `news_risk_high->unknown_1h` score `3.4958` n `71` status `ready` deltaP `8.9567` edge `0.2673` maxDD `-0.8558`
- `market_context_high->metal_24h` score `3.2818` n `120` status `ready` deltaP `28.7406` edge `0.1838` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.4346` n `50` status `ready` deltaP `26.9948` edge `0.038` maxDD `-0.2064`
- `news_risk_high->fx_4h` score `2.2077` n `71` status `ready` deltaP `32.4587` edge `0.0225` maxDD `-0.3931`
- `market_context_high->unknown_4h` score `2.1933` n `120` status `ready` deltaP `17.246` edge `0.1085` maxDD `-0.5894`
- `market_context_high->unknown_1h` score `0.9084` n `120` status `ready` deltaP `8.7924` edge `0.0621` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6069` n `71` status `ready` deltaP `12.5095` edge `0.0059` maxDD `-0.0975`
- `news_risk_high->commodity_1h` score `0.3759` n `71` status `ready` deltaP `11.4616` edge `0.0038` maxDD `-0.5618`
- `market_context_high->metal_4h` score `0.0254` n `120` status `ready` deltaP `12.2357` edge `0.0134` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.388` n `120` status `ready` deltaP `3.6128` edge `-0.0006` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.4359` n `71` status `ready` deltaP `-0.4322` edge `-0.0096` maxDD `-0.8054`
- `market_context_high->crypto_alt_4h` score `-0.6901` n `120` status `ready` deltaP `15.7723` edge `0.291` maxDD `-31.4361`
- `news_risk_high->index_4h` score `-0.6965` n `71` status `ready` deltaP `-0.7407` edge `-0.0202` maxDD `-1.7996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
