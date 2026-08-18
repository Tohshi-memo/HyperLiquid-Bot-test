# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T20:07:33.509597+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11621`

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

- `market_context_high->crypto_major_24h` score `2.7333` n `91` status `ready` deltaP `10.0294` edge `0.2817` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.6514` n `91` status `ready` deltaP `19.1163` edge `0.2676` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.2939` n `96` status `ready` deltaP `10.66` edge `0.0669` maxDD `-0.4112`
- `market_context_high->equity_4h` score `0.9245` n `96` status `ready` deltaP `5.8181` edge `0.1271` maxDD `-2.4411`
- `market_context_high->metal_4h` score `0.8723` n `96` status `ready` deltaP `15.0406` edge `0.03` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6971` n `96` status `ready` deltaP `13.2173` edge `0.0087` maxDD `-0.0982`
- `market_context_high->crypto_major_4h` score `0.6552` n `96` status `ready` deltaP `8.7144` edge `0.0986` maxDD `-3.1677`
- `market_context_high->unknown_1h` score `0.5166` n `96` status `ready` deltaP `9.6557` edge `0.0014` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.139` n `96` status `ready` deltaP `9.1463` edge `0.0776` maxDD `-5.4926`
- `market_context_high->metal_1h` score `0.0242` n `96` status `ready` deltaP `4.622` edge `0.0099` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `0.0225` n `91` status `ready` deltaP `14.3029` edge `-0.0721` maxDD `-0.3771`
- `market_context_high->fx_4h` score `-0.1941` n `96` status `ready` deltaP `3.8363` edge `-0.0002` maxDD `-0.3539`
- `market_context_high->crypto_alt_1h` score `-0.4182` n `96` status `ready` deltaP `2.0771` edge `0.0127` maxDD `-2.413`
- `market_context_high->index_4h` score `-0.4368` n `96` status `ready` deltaP `2.1595` edge `0.0147` maxDD `-0.5728`
- `market_context_high->fx_1h` score `-0.4397` n `96` status `ready` deltaP `-3.2685` edge `0.0013` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.4532` n `96` status `ready` deltaP `2.7185` edge `0.0088` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.5333` n `96` status `ready` deltaP `0.5863` edge `0.0122` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.8721` n `96` status `ready` deltaP `-7.4414` edge `-0.0056` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.098` n `91` status `ready` deltaP `-5.2388` edge `0.043` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.304` n `91` status `ready` deltaP `-27.2131` edge `-0.0273` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
