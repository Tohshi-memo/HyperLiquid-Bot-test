# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T02:22:26.303770+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10829`

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

- `market_context_high->equity_4h` score `2.1247` n `96` status `ready` deltaP `11.6107` edge `0.1885` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.7709` n `96` status `ready` deltaP `14.5522` edge `0.0807` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9294` n `96` status `ready` deltaP `15.9119` edge `0.0101` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.3596` n `96` status `ready` deltaP `11.9918` edge `0.0076` maxDD `-1.273`
- `market_context_high->index_4h` score `0.2568` n `96` status `ready` deltaP `9.629` edge `0.0227` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.1498` n `96` status `ready` deltaP `6.4236` edge `0.1597` maxDD `-4.666`
- `market_context_high->fx_4h` score `0.002` n `96` status `ready` deltaP `7.0376` edge `0.0036` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.0957` n `96` status `ready` deltaP `3.8735` edge `0.0049` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.2229` n `96` status `ready` deltaP `17.7083` edge `-0.086` maxDD `-1.0505`
- `market_context_high->unknown_1h` score `-0.2243` n `96` status `ready` deltaP `5.6138` edge `-0.0334` maxDD `-0.4843`
- `market_context_high->fx_1h` score `-0.358` n `96` status `ready` deltaP `-1.7715` edge `0.0018` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.7113` n `96` status `ready` deltaP `-1.8546` edge `0.0062` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8656` n `96` status `ready` deltaP `-0.6175` edge `-0.0267` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.9288` n `96` status `ready` deltaP `1.3348` edge `-0.0435` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9764` n `96` status `ready` deltaP `-9.2378` edge `-0.007` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-2.0506` n `96` status `ready` deltaP `3.811` edge `-0.0693` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.2387` n `96` status `ready` deltaP `6.2754` edge `-0.1263` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.0597` n `96` status `ready` deltaP `-14.4097` edge `-0.0006` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-3.7729` n `96` status `ready` deltaP `-13.0208` edge `-0.0661` maxDD `-11.4635`
- `market_context_high->index_24h` score `-3.7889` n `96` status `ready` deltaP `-0.8681` edge `-0.0632` maxDD `-18.3411`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
