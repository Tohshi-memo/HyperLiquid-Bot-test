# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T10:07:25.719313+00:00`
- Price records: `672`
- Market context records: `5651`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8684`

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

- `market_context_high->equity_24h` score `2.5124` n `183` status `ready` deltaP `14.7541` edge `0.6189` maxDD `-31.6316`
- `market_context_high->fx_24h` score `0.8167` n `183` status `ready` deltaP `19.3221` edge `0.0583` maxDD `-1.8577`
- `market_context_high->crypto_major_4h` score `0.763` n `237` status `ready` deltaP `10.6996` edge `0.2215` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4965` n `237` status `ready` deltaP `7.6863` edge `0.154` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `-0.0399` n `237` status `ready` deltaP `6.3742` edge `0.1391` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2522` n `243` status `ready` deltaP `2.1137` edge `0.0012` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3627` n `243` status `ready` deltaP `5.5907` edge `0.0332` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5479` n `243` status `ready` deltaP `-0.393` edge `-0.0001` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.6894` n `243` status `ready` deltaP `1.0652` edge `0.0316` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.7719` n `243` status `ready` deltaP `3.1985` edge `0.0389` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.9399` n `243` status `ready` deltaP `0.467` edge `0.0054` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.9711` n `243` status `ready` deltaP `0.0191` edge `-0.0045` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2678` n `237` status `ready` deltaP `2.1328` edge `0.0066` maxDD `-1.335`
- `market_context_high->index_4h` score `-2.0233` n `237` status `ready` deltaP `-1.5366` edge `0.0088` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.332` n `183` status `ready` deltaP `9.6767` edge `0.0352` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0607` n `237` status `ready` deltaP `-14.8265` edge `-0.0552` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.7996` n `237` status `ready` deltaP `-2.1875` edge `-0.0345` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.4818` n `183` status `ready` deltaP `4.1012` edge `0.0532` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.383` n `183` status `ready` deltaP `-12.9383` edge `-0.2524` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-12.9041` n `183` status `ready` deltaP `-15.7275` edge `-0.1096` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
