# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T17:37:44.493107+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11460`

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

- `market_context_high->unknown_4h` score `52.6457` n `88` status `ready` deltaP `7.0676` edge `4.3848` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.9852` n `88` status `ready` deltaP `33.7344` edge `2.931` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `5.671` n `88` status `ready` deltaP `26.0674` edge `1.0627` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.5921` n `88` status `ready` deltaP `27.2648` edge `0.3305` maxDD `-2.3671`
- `market_context_high->metal_24h` score `1.1439` n `88` status `ready` deltaP `21.4097` edge `0.0079` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3053` n `88` status `ready` deltaP `4.2461` edge `0.0139` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4175` n `88` status `ready` deltaP `2.2387` edge `-0.0002` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.474` n `88` status `ready` deltaP `3.5615` edge `0.0261` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.5879` n `88` status `ready` deltaP `3.8525` edge `-0.0033` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.966` n `88` status `ready` deltaP `-7.0563` edge `0.0063` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.026` n `88` status `ready` deltaP `-0.5959` edge `0.0108` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2471` n `88` status `ready` deltaP `-13.0103` edge `-0.0047` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5138` n `88` status `ready` deltaP `-7.0563` edge `0.0376` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.744` n `88` status `ready` deltaP `1.8304` edge `-0.0379` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.8353` n `88` status `ready` deltaP `-1.8847` edge `-0.0046` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.0059` n `88` status `ready` deltaP `1.1265` edge `-0.0147` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-2.833` n `88` status `ready` deltaP `-2.715` edge `-0.0828` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.2648` n `88` status `ready` deltaP `0.9146` edge `-0.147` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.3997` n `88` status `ready` deltaP `3.9219` edge `-0.2143` maxDD `-34.2787`
- `market_context_high->commodity_24h` score `-9.2572` n `88` status `ready` deltaP `-23.4698` edge `-0.0626` maxDD `-25.5228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
