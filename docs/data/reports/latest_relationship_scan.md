# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T04:37:32.519787+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3872`

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

- `news_risk_high->crypto_alt_4h` score `-0.5157` n `146` status `ready` deltaP `5.7802` edge `0.159` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.6453` n `146` status `ready` deltaP `1.7328` edge `0.0285` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7261` n `146` status `ready` deltaP `-2.9714` edge `-0.0032` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7478` n `146` status `ready` deltaP `2.8443` edge `-0.0013` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.5345` n `146` status `ready` deltaP `-8.3914` edge `-0.0186` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5976` n `146` status `ready` deltaP `-9.9085` edge `-0.0136` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8144` n `146` status `ready` deltaP `0.5367` edge `-0.0061` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.119` n `146` status `ready` deltaP `-7.4297` edge `0.0096` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4374` n `146` status `ready` deltaP `-18.6638` edge `-0.0172` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.569` n `146` status `ready` deltaP `-6.0372` edge `-0.0215` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.8003` n `146` status `ready` deltaP `-11.6438` edge `0.0028` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.1053` n `146` status `ready` deltaP `-9.4262` edge `0.0395` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.3904` n `146` status `ready` deltaP `-7.5568` edge `-0.0596` maxDD `-9.4709`
- `news_risk_high->metal_4h` score `-5.4242` n `146` status `ready` deltaP `-9.7394` edge `-0.0666` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-5.835` n `146` status `ready` deltaP `-3.6545` edge `-0.1037` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.6985` n `146` status `ready` deltaP `-12.5543` edge `-0.1559` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-10.7758` n `146` status `ready` deltaP `-20.1616` edge `0.0625` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.8853` n `146` status `ready` deltaP `0.6891` edge `-0.0756` maxDD `-52.2214`
- `news_risk_high->crypto_alt_24h` score `-13.3983` n `146` status `ready` deltaP `8.0747` edge `-0.0721` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-13.5618` n `146` status `ready` deltaP `9.9778` edge `0.2537` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
