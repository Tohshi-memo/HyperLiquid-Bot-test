# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T22:52:29.517584+00:00`
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

- `market_context_high->unknown_4h` score `65.0027` n `88` status `ready` deltaP `7.525` edge `5.4115` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.276` n `88` status `ready` deltaP `33.6489` edge `2.9558` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `6.799` n `88` status `ready` deltaP `29.6401` edge `1.1835` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.016` n `88` status `ready` deltaP `30.808` edge `0.3422` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `2.9153` n `30` status `ready` deltaP `14.0818` edge `0.2206` maxDD `-3.7228`
- `market_context_high->metal_24h` score `2.2109` n `88` status `ready` deltaP `24.9526` edge `0.0732` maxDD `-1.4245`
- `news_risk_high->index_1h` score `0.969` n `30` status `ready` deltaP `13.9321` edge `0.018` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6511` n `30` status `ready` deltaP `21.008` edge `0.0372` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.5115` n `30` status `ready` deltaP `20.8583` edge `0.0317` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `0.4398` n `30` status `ready` deltaP `0.9381` edge `0.0527` maxDD `-0.1177`
- `news_risk_high->metal_1h` score `0.1069` n `30` status `ready` deltaP `6.0679` edge `-0.0013` maxDD `-0.3692`
- `market_context_high->metal_1h` score `-0.3413` n `88` status `ready` deltaP `3.9467` edge `0.0129` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3568` n `88` status `ready` deltaP `3.2866` edge `0.0006` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.5649` n `88` status `ready` deltaP `4.3098` edge `-0.0034` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.5651` n `88` status `ready` deltaP `2.7993` edge `0.0195` maxDD `-4.182`
- `news_risk_high->fx_1h` score `-0.7585` n `30` status `ready` deltaP `-4.3812` edge `-0.005` maxDD `-0.3199`
- `market_context_high->index_1h` score `-0.9823` n `88` status `ready` deltaP `-7.3557` edge `0.0062` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0284` n `88` status `ready` deltaP `-0.7483` edge `0.0115` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2175` n `88` status `ready` deltaP `-12.4115` edge `-0.0049` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5333` n `88` status `ready` deltaP `-7.206` edge `0.0361` maxDD `-8.1039`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
