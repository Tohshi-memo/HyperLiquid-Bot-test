# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T06:22:23.769548+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10797`

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

- `market_context_high->equity_4h` score `1.8431` n `96` status `ready` deltaP `10.0863` edge `0.1752` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.7984` n `96` status `ready` deltaP `15.0013` edge `0.08` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.8923` n `96` status `ready` deltaP `15.4628` edge `0.01` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.286` n `96` status `ready` deltaP `11.687` edge `0.0035` maxDD `-1.273`
- `market_context_high->commodity_24h` score `0.0905` n `96` status `ready` deltaP `6.4236` edge `0.1521` maxDD `-4.666`
- `market_context_high->index_4h` score `0.0659` n `96` status `ready` deltaP `7.6473` edge `0.02` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.0092` n `96` status `ready` deltaP `7.19` edge `0.0035` maxDD `-0.3539`
- `market_context_high->unknown_1h` score `0.0` n `96` status `ready` deltaP `5.7635` edge `-0.0157` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.1568` n `96` status `ready` deltaP `3.2747` edge `0.0038` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3642` n `96` status `ready` deltaP `-1.9212` edge `0.002` maxDD `-0.2043`
- `market_context_high->unknown_24h` score `-0.4497` n `96` status `ready` deltaP `17.7083` edge `-0.1049` maxDD `-1.0505`
- `market_context_high->commodity_4h` score `-0.7689` n `96` status `ready` deltaP `-2.6168` edge `0.0039` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8056` n `96` status `ready` deltaP `-0.0187` edge `-0.023` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.8711` n `96` status `ready` deltaP `1.7839` edge `-0.0391` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.9211` n `96` status `ready` deltaP `-8.3396` edge `-0.0059` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.92` n `96` status `ready` deltaP `4.5732` edge `-0.0635` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.9756` n `96` status `ready` deltaP `7.4949` edge `-0.1125` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.1936` n `96` status `ready` deltaP `-15.7986` edge `-0.0025` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.8146` n `96` status `ready` deltaP `-0.8681` edge `-0.0665` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.2683` n `96` status `ready` deltaP `-15.7986` edge `-0.1111` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
