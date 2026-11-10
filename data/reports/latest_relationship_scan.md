# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T17:07:37.653990+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11448`

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

- `market_context_high->unknown_4h` score `52.6383` n `88` status `ready` deltaP `6.9152` edge `4.3852` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.9516` n `88` status `ready` deltaP `33.7344` edge `2.9282` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.5675` n `88` status `ready` deltaP `27.0915` edge `0.3296` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `5.5243` n `88` status `ready` deltaP `25.7208` edge `1.0462` maxDD `-33.4213`
- `market_context_high->metal_24h` score `1.055` n `88` status `ready` deltaP `21.0631` edge `0.0028` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3053` n `88` status `ready` deltaP `4.2461` edge `0.0139` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4354` n `88` status `ready` deltaP `1.9393` edge `-0.0005` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.4693` n `88` status `ready` deltaP `3.5615` edge `0.0267` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.5895` n `88` status `ready` deltaP `3.8525` edge `-0.0035` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9753` n `88` status `ready` deltaP `-7.206` edge `0.0061` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0306` n `88` status `ready` deltaP `-0.5959` edge `0.0102` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2556` n `88` status `ready` deltaP `-13.16` edge `-0.0048` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5411` n `88` status `ready` deltaP `-7.206` edge `0.0351` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.7659` n `88` status `ready` deltaP `1.6807` edge `-0.0397` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.8535` n `88` status `ready` deltaP `-2.1896` edge `-0.0049` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.0432` n `88` status `ready` deltaP `0.7799` edge `-0.0155` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-2.8478` n `88` status `ready` deltaP `-2.8647` edge `-0.0837` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.29` n `88` status `ready` deltaP `0.9146` edge `-0.1491` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.4489` n `88` status `ready` deltaP `3.9219` edge `-0.2184` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.2356` n `88` status `ready` deltaP `-23.4698` edge `-0.0608` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
