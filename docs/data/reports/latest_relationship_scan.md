# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T00:52:23.757504+00:00`
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

- `market_context_high->unknown_4h` score `80.8078` n `88` status `ready` deltaP `7.525` edge `6.7286` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.9738` n `88` status `ready` deltaP `33.6489` edge `2.9293` maxDD `-16.7984`
- `market_context_high->crypto_alt_24h` score `7.1333` n `88` status `ready` deltaP `31.029` edge `1.2171` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1432` n `88` status `ready` deltaP `32.0233` edge `0.3447` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `3.2576` n `37` status `ready` deltaP `17.7173` edge `0.2246` maxDD `-3.6997`
- `market_context_high->metal_24h` score `2.622` n `88` status `ready` deltaP `26.3415` edge `0.0982` maxDD `-1.4245`
- `news_risk_high->index_1h` score `1.3162` n `37` status `ready` deltaP `17.7173` edge `0.0217` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.9234` n `37` status `ready` deltaP `21.3101` edge `0.0701` maxDD `-6.1688`
- `news_risk_high->metal_1h` score `0.8767` n `37` status `ready` deltaP `14.2661` edge `0.0034` maxDD `-0.3692`
- `news_risk_high->crypto_major_1h` score `0.5428` n `37` status `ready` deltaP `21.3101` edge `0.0327` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.2245` n `37` status `ready` deltaP `-4.046` edge `0.0406` maxDD `-0.2537`
- `market_context_high->metal_1h` score `-0.3449` n `88` status `ready` deltaP `3.9467` edge `0.0126` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3739` n `88` status `ready` deltaP `2.9872` edge `0.0004` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.6263` n `88` status `ready` deltaP `2.342` edge `0.0147` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.6923` n `88` status `ready` deltaP `3.0903` edge `-0.0116` maxDD `-2.4871`
- `news_risk_high->fx_1h` score `-0.8029` n `37` status `ready` deltaP `-4.6529` edge `-0.0067` maxDD `-0.3348`
- `market_context_high->index_1h` score `-1.0143` n `88` status `ready` deltaP `-7.8048` edge `0.0051` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0939` n `88` status `ready` deltaP `-1.6629` edge `0.0092` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.1902` n `88` status `ready` deltaP `-11.9624` edge `-0.0044` maxDD `-0.8088`
- `market_context_high->fx_24h` score `-1.5127` n `88` status `ready` deltaP `6.0764` edge `-0.0066` maxDD `-3.4642`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
