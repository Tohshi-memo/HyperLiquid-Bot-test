# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-03T07:22:39.699291+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4510`

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

- `news_risk_high->crypto_alt_4h` score `0.2482` n `146` status `ready` deltaP `6.0851` edge `0.2549` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.3747` n `146` status `ready` deltaP `2.631` edge `0.0572` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6031` n `146` status `ready` deltaP `-0.7259` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.9059` n `146` status `ready` deltaP `1.1976` edge `-0.0035` maxDD `-1.3981`
- `news_risk_high->metal_24h` score `-1.0217` n `137` status `ready` deltaP `10.6828` edge `0.1234` maxDD `-14.0483`
- `news_risk_high->fx_4h` score `-1.2428` n `146` status `ready` deltaP `-3.5061` edge `-0.0108` maxDD `-1.6794`
- `news_risk_high->metal_1h` score `-1.2845` n `146` status `ready` deltaP `-4.9483` edge `-0.0095` maxDD `-3.1082`
- `news_risk_high->index_4h` score `-2.056` n `146` status `ready` deltaP `-2.9694` edge `-0.0137` maxDD `-4.0745`
- `news_risk_high->index_24h` score `-2.2071` n `137` status `ready` deltaP `-3.2213` edge `0.0227` maxDD `-7.402`
- `news_risk_high->commodity_1h` score `-2.3864` n `146` status `ready` deltaP `-9.0764` edge `-0.0017` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4131` n `137` status `ready` deltaP `-17.9706` edge `-0.0187` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.6992` n `146` status `ready` deltaP `-6.9354` edge `-0.0322` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.1935` n `146` status `ready` deltaP `-8.0059` edge `-0.0402` maxDD `-9.4709`
- `news_risk_high->crypto_alt_24h` score `-3.8295` n `137` status `ready` deltaP `20.2352` edge `0.7699` maxDD `-97.3281`
- `news_risk_high->commodity_4h` score `-3.8606` n `146` status `ready` deltaP `-12.6274` edge `-0.0021` maxDD `-9.5011`
- `news_risk_high->equity_24h` score `-4.7461` n `137` status `ready` deltaP `15.3741` edge `0.5115` maxDD `-67.0937`
- `news_risk_high->metal_4h` score `-4.7933` n `146` status `ready` deltaP `-7.1479` edge `-0.0313` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-6.968` n `146` status `ready` deltaP `-13.7738` edge `-0.0869` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-11.5242` n `146` status `ready` deltaP `-1.5975` edge `-0.1136` maxDD `-52.2214`
- `news_risk_high->crypto_major_24h` score `-12.4246` n `137` status `ready` deltaP `-12.8207` edge `0.038` maxDD `-64.6996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
