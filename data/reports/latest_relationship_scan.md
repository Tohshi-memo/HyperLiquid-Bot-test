# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T04:22:35.331795+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3848`

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

- `news_risk_high->crypto_alt_4h` score `-0.5015` n `146` status `ready` deltaP `5.9326` edge `0.1598` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.671` n `146` status `ready` deltaP `1.5831` edge `0.0262` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7339` n `146` status `ready` deltaP `-3.1211` edge `-0.0032` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7645` n `146` status `ready` deltaP `2.6946` edge `-0.0017` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.5438` n `146` status `ready` deltaP `-8.5411` edge `-0.0188` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5976` n `146` status `ready` deltaP `-9.9085` edge `-0.0136` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.8255` n `146` status `ready` deltaP `0.3842` edge `-0.0065` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.1178` n `146` status `ready` deltaP `-7.4297` edge `0.0097` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.4367` n `146` status `ready` deltaP `-18.6638` edge `-0.0171` maxDD `-2.336`
- `news_risk_high->equity_1h` score `-2.5908` n `146` status `ready` deltaP `-6.1869` edge `-0.0233` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-2.782` n `146` status `ready` deltaP `-11.4708` edge `0.004` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.1101` n `146` status `ready` deltaP `-9.4262` edge `0.0391` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.4252` n `146` status `ready` deltaP `-7.7065` edge `-0.0615` maxDD `-9.4709`
- `news_risk_high->metal_4h` score `-5.4048` n `146` status `ready` deltaP `-9.5869` edge `-0.066` maxDD `-9.3056`
- `news_risk_high->metal_24h` score `-5.7672` n `146` status `ready` deltaP `-3.4815` edge `-0.0992` maxDD `-16.6552`
- `news_risk_high->crypto_major_4h` score `-7.7179` n `146` status `ready` deltaP `-12.7068` edge `-0.1565` maxDD `-24.1554`
- `news_risk_high->commodity_24h` score `-10.8106` n `146` status `ready` deltaP `-20.1616` edge `0.0596` maxDD `-43.7525`
- `news_risk_high->equity_4h` score `-10.8973` n `146` status `ready` deltaP `0.6891` edge `-0.0766` maxDD `-52.2214`
- `news_risk_high->crypto_alt_24h` score `-13.2778` n `146` status `ready` deltaP `8.2477` edge `-0.0578` maxDD `-118.6236`
- `news_risk_high->equity_24h` score `-13.4771` n `146` status `ready` deltaP `10.1508` edge `0.2596` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
