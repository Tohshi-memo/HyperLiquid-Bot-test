# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T23:07:33.172326+00:00`
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

- `market_context_high->unknown_4h` score `67.3823` n `88` status `ready` deltaP `7.525` edge `5.6098` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.2736` n `88` status `ready` deltaP `33.6489` edge `2.9556` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `6.8424` n `88` status `ready` deltaP `29.8137` edge `1.1879` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.0359` n `88` status `ready` deltaP `30.9817` edge `0.3427` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `2.5911` n `31` status `ready` deltaP `12.0388` edge `0.2072` maxDD `-3.7228`
- `market_context_high->metal_24h` score `2.2644` n `88` status `ready` deltaP `25.1262` edge `0.0765` maxDD `-1.4245`
- `news_risk_high->index_1h` score `0.8056` n `31` status `ready` deltaP `12.0388` edge `0.017` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.4301` n `31` status `ready` deltaP `18.8574` edge `0.0232` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `0.283` n `31` status `ready` deltaP `-0.7823` edge `0.0511` maxDD `-0.1177`
- `news_risk_high->crypto_major_1h` score `0.2468` n `31` status `ready` deltaP `18.7077` edge `0.0121` maxDD `-7.0808`
- `news_risk_high->metal_1h` score `0.1811` n `31` status `ready` deltaP `7.4657` edge `-0.0011` maxDD `-0.3692`
- `market_context_high->metal_1h` score `-0.3413` n `88` status `ready` deltaP `3.9467` edge `0.0129` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3568` n `88` status `ready` deltaP `3.2866` edge `0.0006` maxDD `-1.7935`
- `news_risk_high->fx_1h` score `-0.4067` n `31` status `ready` deltaP `-2.8105` edge `-0.0044` maxDD `-0.3199`
- `market_context_high->commodity_4h` score `-0.5777` n `88` status `ready` deltaP `2.6469` edge `0.0189` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.5791` n `88` status `ready` deltaP `4.1574` edge `-0.0042` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9745` n `88` status `ready` deltaP `-7.206` edge `0.0062` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0284` n `88` status `ready` deltaP `-0.7483` edge `0.0115` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2253` n `88` status `ready` deltaP `-12.5612` edge `-0.0049` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5317` n `88` status `ready` deltaP `-7.206` edge `0.0363` maxDD `-8.1039`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
