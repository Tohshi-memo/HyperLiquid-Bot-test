# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T00:37:28.206720+00:00`
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

- `market_context_high->unknown_4h` score `80.671` n `88` status `ready` deltaP `7.525` edge `6.7172` maxDD `-0.9161`
- `market_context_high->equity_24h` score `35.0074` n `88` status `ready` deltaP `33.6489` edge `2.9321` maxDD `-16.7984`
- `market_context_high->crypto_alt_24h` score `7.0978` n `88` status `ready` deltaP `30.8554` edge `1.2137` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1432` n `88` status `ready` deltaP `32.0233` edge `0.3447` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.3056` n `37` status `ready` deltaP `17.867` edge `0.2276` maxDD `-3.6997`
- `market_context_high->metal_24h` score `2.5722` n `88` status `ready` deltaP `26.1679` edge `0.0952` maxDD `-1.4245`
- `news_risk_high->index_1h` score `1.3342` n `37` status `ready` deltaP `17.867` edge `0.0222` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.9507` n `37` status `ready` deltaP `21.4598` edge `0.0726` maxDD `-6.1688`
- `news_risk_high->metal_1h` score `0.8791` n `37` status `ready` deltaP `14.2661` edge `0.0036` maxDD `-0.3692`
- `news_risk_high->crypto_major_1h` score `0.5584` n `37` status `ready` deltaP `21.3101` edge `0.0347` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.2245` n `37` status `ready` deltaP `-4.046` edge `0.0406` maxDD `-0.2537`
- `market_context_high->metal_1h` score `-0.3425` n `88` status `ready` deltaP `3.9467` edge `0.0128` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3739` n `88` status `ready` deltaP `2.9872` edge `0.0004` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.6232` n `88` status `ready` deltaP `2.342` edge `0.0151` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.675` n `88` status `ready` deltaP `3.2428` edge `-0.0104` maxDD `-2.4871`
- `news_risk_high->fx_1h` score `-0.816` n `37` status `ready` deltaP `-4.8026` edge `-0.0068` maxDD `-0.3348`
- `market_context_high->index_1h` score `-1.0026` n `88` status `ready` deltaP `-7.6551` edge `0.0056` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0908` n `88` status `ready` deltaP `-1.6629` edge `0.0096` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.1988` n `88` status `ready` deltaP `-12.1121` edge `-0.0045` maxDD `-0.8088`
- `market_context_high->fx_24h` score `-1.5314` n `88` status `ready` deltaP `5.9028` edge `-0.007` maxDD `-3.4642`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
