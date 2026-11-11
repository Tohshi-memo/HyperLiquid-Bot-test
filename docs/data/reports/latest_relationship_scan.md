# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T00:07:31.336437+00:00`
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

- `market_context_high->unknown_4h` score `80.4551` n `88` status `ready` deltaP `7.525` edge `6.6992` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.2448` n `88` status `ready` deltaP `33.6489` edge `2.9532` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `7.0267` n `88` status `ready` deltaP `30.5082` edge `1.2069` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1094` n `88` status `ready` deltaP `31.6761` edge `0.3442` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.2894` n `35` status `ready` deltaP `16.3131` edge `0.2369` maxDD `-3.7228`
- `market_context_high->metal_24h` score `2.4724` n `88` status `ready` deltaP `25.8207` edge `0.0892` maxDD `-1.4245`
- `news_risk_high->index_1h` score `1.2063` n `35` status `ready` deltaP `16.3131` edge `0.0219` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7147` n `35` status `ready` deltaP `19.9059` edge `0.0527` maxDD `-6.1688`
- `news_risk_high->metal_1h` score `0.7077` n `35` status `ready` deltaP `12.2583` edge `0.0027` maxDD `-0.3692`
- `news_risk_high->crypto_major_1h` score `0.4129` n `35` status `ready` deltaP `19.7562` edge `0.0264` maxDD `-7.0808`
- `market_context_high->metal_1h` score `-0.3437` n `88` status `ready` deltaP `3.9467` edge `0.0127` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3576` n `88` status `ready` deltaP `3.2866` edge `0.0005` maxDD `-1.7935`
- `news_risk_high->commodity_1h` score `-0.4173` n `35` status `ready` deltaP `-6.6809` edge `0.0421` maxDD `-0.2537`
- `news_risk_high->fx_1h` score `-0.5989` n `35` status `ready` deltaP `-2.4765` edge `-0.0044` maxDD `-0.3199`
- `market_context_high->commodity_4h` score `-0.6146` n `88` status `ready` deltaP `2.342` edge `0.0162` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.6412` n `88` status `ready` deltaP `3.5477` edge `-0.0081` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9847` n `88` status `ready` deltaP `-7.3557` edge `0.0059` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0679` n `88` status `ready` deltaP `-1.3581` edge `0.0105` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2167` n `88` status `ready` deltaP `-12.4115` edge `-0.0048` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5574` n `88` status `ready` deltaP `-7.3557` edge `0.034` maxDD `-8.1039`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
