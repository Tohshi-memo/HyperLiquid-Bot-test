# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-11T06:37:33.990539+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11726`

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

- `market_context_high->unknown_4h` score `78.8626` n `88` status `ready` deltaP `7.525` edge `6.5665` maxDD `-0.9161`
- `market_context_high->equity_24h` score `34.2522` n `88` status `ready` deltaP `31.7392` edge `2.8819` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `12.9475` n `46` status `ready` deltaP `36.8041` edge `0.9458` maxDD `-6.9762`
- `market_context_high->crypto_alt_24h` score `8.4061` n `88` status `ready` deltaP `33.9804` edge `1.3606` maxDD `-33.4213`
- `market_context_high->index_24h` score `6.1797` n `88` status `ready` deltaP `31.8497` edge `0.3489` maxDD `-2.3671`
- `news_risk_high->equity_1h` score `4.1321` n `49` status `ready` deltaP `21.673` edge `0.2711` maxDD `-3.6997`
- `market_context_high->metal_24h` score `3.8751` n `88` status `ready` deltaP `30.3346` edge `0.176` maxDD `-1.4245`
- `news_risk_high->crypto_major_4h` score `3.8725` n `46` status `ready` deltaP `23.754` edge `0.3131` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `3.4313` n `46` status `ready` deltaP `34.6302` edge `0.0927` maxDD `-1.0104`
- `news_risk_high->commodity_4h` score `3.2862` n `46` status `ready` deltaP `26.2792` edge `0.124` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.0227` n `46` status `ready` deltaP `29.1026` edge `0.1015` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.369` n `46` status `ready` deltaP `28.4067` edge `0.2782` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `1.5879` n `49` status `ready` deltaP `20.0813` edge `0.0239` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5546` n `49` status `ready` deltaP `19.9316` edge `0.0268` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.99` n `49` status `ready` deltaP `21.0894` edge `0.0801` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.8379` n `49` status `ready` deltaP `21.0894` edge `0.072` maxDD `-7.0808`
- `news_risk_high->commodity_1h` score `-0.0687` n `49` status `ready` deltaP `-1.8239` edge `0.0399` maxDD `-0.3438`
- `market_context_high->commodity_1h` score `-0.3911` n `88` status `ready` deltaP `2.8375` edge `-0.0008` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.394` n `88` status `ready` deltaP `3.1982` edge `0.0135` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.6637` n `88` status `ready` deltaP `1.4274` edge `0.016` maxDD `-4.182`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
