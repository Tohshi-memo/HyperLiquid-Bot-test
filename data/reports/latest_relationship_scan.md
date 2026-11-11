# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T01:22:27.518243+00:00`
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

- `market_context_high->unknown_4h` score `80.9326` n `88` status `ready` deltaP `7.525` edge `6.739` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.8819` n `88` status `ready` deltaP `33.4753` edge `2.9228` maxDD `-16.7984`
- `market_context_high->crypto_alt_24h` score `7.2122` n `88` status `ready` deltaP `31.3762` edge `1.2249` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1281` n `88` status `ready` deltaP `31.8497` edge `0.3446` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.1593` n `37` status `ready` deltaP `17.4179` edge `0.2184` maxDD `-3.6997`
- `market_context_high->metal_24h` score `2.7254` n `88` status `ready` deltaP `26.6887` edge `0.1045` maxDD `-1.4245`
- `news_risk_high->index_1h` score `1.2815` n `37` status `ready` deltaP `17.4179` edge `0.0208` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.9` n `37` status `ready` deltaP `21.3101` edge `0.0671` maxDD `-6.1688`
- `news_risk_high->metal_1h` score `0.8599` n `37` status `ready` deltaP `14.1164` edge `0.003` maxDD `-0.3692`
- `news_risk_high->crypto_major_1h` score `0.5256` n `37` status `ready` deltaP `21.3101` edge `0.0305` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.2233` n `37` status `ready` deltaP `-4.046` edge `0.0407` maxDD `-0.2537`
- `market_context_high->metal_1h` score `-0.3617` n `88` status `ready` deltaP `3.797` edge `0.0122` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3731` n `88` status `ready` deltaP `2.9872` edge `0.0005` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.642` n `88` status `ready` deltaP `2.1896` edge `0.0137` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.7253` n `88` status `ready` deltaP `2.7855` edge `-0.0138` maxDD `-2.4871`
- `news_risk_high->fx_1h` score `-0.7897` n `37` status `ready` deltaP `-4.5032` edge `-0.0066` maxDD `-0.3348`
- `market_context_high->index_1h` score `-1.0368` n `88` status `ready` deltaP `-8.1042` edge `0.0042` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.1176` n `88` status `ready` deltaP `-1.9678` edge `0.0082` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.1817` n `88` status `ready` deltaP `-11.8127` edge `-0.0043` maxDD `-0.8088`
- `market_context_high->fx_24h` score `-1.4753` n `88` status `ready` deltaP `6.4236` edge `-0.0058` maxDD `-3.4642`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
