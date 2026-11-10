# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T23:52:35.720921+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11740`

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

- `market_context_high->unknown_4h` score `77.4251` n `88` status `ready` deltaP `7.525` edge `6.4467` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.2532` n `88` status `ready` deltaP `33.6489` edge `2.9539` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `6.9786` n `88` status `ready` deltaP `30.3346` edge `1.2019` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.0919` n `88` status `ready` deltaP `31.5025` edge `0.3439` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.0851` n `34` status `ready` deltaP `15.4544` edge `0.2256` maxDD `-3.7228`
- `market_context_high->metal_24h` score `2.4213` n `88` status `ready` deltaP `25.6471` edge `0.0861` maxDD `-1.4245`
- `news_risk_high->index_1h` score `1.1112` n `34` status `ready` deltaP `15.4544` edge `0.0197` maxDD `-0.4103`
- `news_risk_high->metal_1h` score `0.6011` n `34` status `ready` deltaP `11.1659` edge `0.0011` maxDD `-0.3692`
- `news_risk_high->crypto_alt_1h` score `0.5242` n `34` status `ready` deltaP `19.0472` edge `0.034` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.2559` n `34` status `ready` deltaP `18.8975` edge `0.012` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.2288` n `34` status `ready` deltaP `-5.3364` edge `0.0442` maxDD `-0.215`
- `news_risk_high->fx_1h` score `-0.315` n `34` status `ready` deltaP `-1.1976` edge `-0.0034` maxDD `-0.3199`
- `market_context_high->metal_1h` score `-0.3425` n `88` status `ready` deltaP `3.9467` edge `0.0128` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3576` n `88` status `ready` deltaP `3.2866` edge `0.0005` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.6099` n `88` status `ready` deltaP `2.342` edge `0.0168` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.6239` n `88` status `ready` deltaP `3.7001` edge `-0.0069` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9753` n `88` status `ready` deltaP `-7.206` edge `0.0061` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0569` n `88` status `ready` deltaP `-1.2056` edge `0.0109` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2253` n `88` status `ready` deltaP `-12.5612` edge `-0.0049` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5395` n `88` status `ready` deltaP `-7.206` edge `0.0353` maxDD `-8.1039`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
