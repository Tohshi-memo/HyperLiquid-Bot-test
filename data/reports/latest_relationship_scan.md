# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T21:52:22.811736+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7305`

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

- `market_context_high->unknown_24h` score `3361.112` n `91` status `ready` deltaP `-10.8688` edge `280.2081` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `127.41` n `91` status `ready` deltaP `1.3334` edge `10.6219` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `77.5732` n `108` status `ready` deltaP `-5.1951` edge `6.5277` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `18.8783` n `81` status `ready` deltaP `44.9267` edge `1.2788` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.6977` n `91` status `ready` deltaP `23.7428` edge `1.0089` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.5052` n `108` status `ready` deltaP `20.7317` edge `0.4592` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.9616` n `91` status `ready` deltaP `43.9313` edge `0.1389` maxDD `-0.1315`
- `market_context_high->metal_4h` score `1.5538` n `91` status `ready` deltaP `19.2559` edge `0.0436` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.8875` n `91` status `ready` deltaP `12.5354` edge `0.0194` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.8361` n `108` status `ready` deltaP `8.8767` edge `0.1059` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.6886` n `91` status `ready` deltaP `16.2641` edge `0.0632` maxDD `-0.6672`
- `market_context_high->equity_4h` score `0.5039` n `91` status `ready` deltaP `1.9851` edge `0.1907` maxDD `-4.48`
- `market_context_high->equity_1h` score `0.4425` n `91` status `ready` deltaP `6.044` edge `0.104` maxDD `-2.3383`
- `market_context_high->fx_4h` score `0.4391` n `91` status `ready` deltaP `11.1448` edge `0.0014` maxDD `-0.1285`
- `market_context_high->fx_1h` score `0.4021` n `91` status `ready` deltaP `10.5416` edge `-0.0003` maxDD `-0.1407`
- `market_context_high->crypto_major_1h` score `0.3071` n `91` status `ready` deltaP `8.3915` edge `0.0862` maxDD `-5.2213`
- `market_context_high->metal_24h` score `-0.3285` n `91` status `ready` deltaP `8.711` edge `0.1645` maxDD `-10.5088`
- `market_context_high->index_1h` score `-0.4635` n `91` status `ready` deltaP `2.2982` edge `0.0019` maxDD `-1.1344`
- `market_context_high->commodity_1h` score `-0.4703` n `91` status `ready` deltaP `-3.4004` edge `0.0138` maxDD `-0.4475`
- `market_context_high->crypto_major_4h` score `-0.4814` n `91` status `ready` deltaP `14.594` edge `0.115` maxDD `-14.5879`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
