# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T20:52:32.921463+00:00`
- Price records: `672`
- Market context records: `5077`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10324`

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

- `market_context_high->unknown_1h` score `12.5328` n `103` status `ready` deltaP `4.664` edge `1.0634` maxDD `-1.674`
- `market_context_high->unknown_24h` score `12.3958` n `78` status `ready` deltaP `27.5908` edge `0.8833` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `9.5389` n `92` status `ready` deltaP `21.1691` edge `0.756` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `7.3384` n `92` status `ready` deltaP `21.9844` edge `0.5869` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `6.5892` n `92` status `ready` deltaP `20.4202` edge `0.5714` maxDD `-8.3416`
- `market_context_high->equity_4h` score `1.8813` n `92` status `ready` deltaP `8.5233` edge `0.2131` maxDD `-6.3852`
- `market_context_high->crypto_alt_1h` score `1.1082` n `103` status `ready` deltaP `7.4356` edge `0.1238` maxDD `-3.8153`
- `market_context_high->crypto_major_1h` score `1.0992` n `103` status `ready` deltaP `8.6376` edge `0.1365` maxDD `-5.1989`
- `market_context_high->metal_4h` score `0.8947` n `92` status `ready` deltaP `9.6832` edge `0.1179` maxDD `-1.9651`
- `market_context_high->metal_1h` score `0.7445` n `103` status `ready` deltaP `11.0241` edge `0.0382` maxDD `-1.3057`
- `market_context_high->equity_1h` score `0.6089` n `103` status `ready` deltaP `9.0009` edge `0.0754` maxDD `-2.5875`
- `market_context_high->index_4h` score `0.2915` n `92` status `ready` deltaP `8.3112` edge `0.045` maxDD `-1.0893`
- `market_context_high->index_1h` score `-0.0` n `103` status `ready` deltaP `3.8472` edge `0.0136` maxDD `-0.4734`
- `market_context_high->commodity_1h` score `-0.3396` n `103` status `ready` deltaP `1.7601` edge `0.0107` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.4952` n `92` status `ready` deltaP `9.4711` edge `0.0115` maxDD `-4.2725`
- `market_context_high->fx_24h` score `-0.5425` n `78` status `ready` deltaP `1.0417` edge `-0.0003` maxDD `-1.7626`
- `market_context_high->fx_4h` score `-1.0022` n `92` status `ready` deltaP `-4.328` edge `-0.0007` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.0362` n `103` status `ready` deltaP `-10.0401` edge `-0.0037` maxDD `-0.6441`
- `market_context_high->commodity_24h` score `-2.3165` n `78` status `ready` deltaP `8.8542` edge `0.0157` maxDD `-19.4034`
- `market_context_high->metal_24h` score `-4.0412` n `78` status `ready` deltaP `-1.1886` edge `0.0353` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
