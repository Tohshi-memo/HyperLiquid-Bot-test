# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T13:07:29.202766+00:00`
- Price records: `672`
- Market context records: `5881`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10248`

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

- `news_risk_high->fx_4h` score `3.7764` n `30` status `ready` deltaP `39.3902` edge `0.0567` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0501` n `30` status `ready` deltaP `24.8303` edge `0.0192` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4822` n `231` status `ready` deltaP `8.691` edge `0.1756` maxDD `-4.1352`
- `news_risk_high->crypto_major_1h` score `0.9681` n `30` status `ready` deltaP `11.8363` edge `0.0919` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.3105` n `30` status `ready` deltaP `5.4691` edge `0.0495` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.2309` n `235` status `ready` deltaP `5.2179` edge `0.0386` maxDD `-4.4103`
- `news_risk_high->metal_1h` score `-0.4071` n `30` status `ready` deltaP `1.8363` edge `-0.0278` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4698` n `235` status `ready` deltaP `3.3966` edge `0.0053` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.5039` n `235` status `ready` deltaP `-0.946` edge `-0.0012` maxDD `-1.9006`
- `market_context_high->crypto_major_1h` score `-0.5118` n `235` status `ready` deltaP `3.8221` edge `0.041` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.5638` n `235` status `ready` deltaP `1.1983` edge `0.0045` maxDD `-0.7819`
- `market_context_high->crypto_alt_1h` score `-0.5778` n `235` status `ready` deltaP `2.845` edge `0.0404` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.7338` n `235` status `ready` deltaP `-1.6945` edge `-0.001` maxDD `-0.5751`
- `news_risk_high->index_1h` score `-1.2595` n `30` status `ready` deltaP `-12.8443` edge `-0.0244` maxDD `-1.1161`
- `market_context_high->crypto_major_4h` score `-1.4025` n `231` status `ready` deltaP `9.545` edge `0.1938` maxDD `-25.6458`
- `news_risk_high->commodity_4h` score `-1.8007` n `30` status `ready` deltaP `-13.5772` edge `-0.0528` maxDD `-2.3372`
- `market_context_high->index_4h` score `-1.8095` n `231` status `ready` deltaP `0.4112` edge `0.0152` maxDD `-3.165`
- `news_risk_high->index_4h` score `-2.3214` n `30` status `ready` deltaP `-17.1646` edge `-0.0798` maxDD `-2.9371`
- `market_context_high->commodity_4h` score `-2.3377` n `231` status `ready` deltaP `-1.2829` edge `-0.0149` maxDD `-6.3754`
- `market_context_high->metal_4h` score `-2.483` n `231` status `ready` deltaP `-2.0826` edge `-0.0298` maxDD `-5.725`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
