# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T10:22:23.201551+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4001`

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

- `news_risk_high->equity_4h` score `1.277` n `62` status `ready` deltaP `11.9886` edge `0.1577` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.6641` n `62` status `ready` deltaP `12.318` edge `0.021` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.3247` n `62` status `ready` deltaP `9.7558` edge `0.1434` maxDD `-6.6786`
- `news_risk_high->fx_24h` score `0.082` n `62` status `ready` deltaP `-2.397` edge `0.067` maxDD `-0.2016`
- `news_risk_high->index_1h` score `0.0629` n `62` status `ready` deltaP `7.4995` edge `0.0034` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.0861` n `62` status `ready` deltaP `-0.4491` edge `0.0469` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.1402` n `62` status `ready` deltaP `2.7091` edge `0.0025` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.1945` n `62` status `ready` deltaP `2.2718` edge `0.0045` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5392` n `62` status `ready` deltaP `-3.9743` edge `-0.0069` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-0.9554` n `62` status `ready` deltaP `1.2687` edge `-0.0404` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.1813` n `62` status `ready` deltaP `-1.9944` edge `-0.0226` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.273` n `62` status `ready` deltaP `-3.1619` edge `0.0183` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.635` n `62` status `ready` deltaP `-11.6235` edge `-0.0028` maxDD `-1.1434`
- `news_risk_high->crypto_major_1h` score `-1.9667` n `62` status `ready` deltaP `-7.881` edge `-0.0296` maxDD `-3.2066`
- `news_risk_high->crypto_alt_4h` score `-2.1703` n `62` status `ready` deltaP `-2.5521` edge `0.0008` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.7918` n `62` status `ready` deltaP `-5.2532` edge `-0.2615` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.5603` n `62` status `ready` deltaP `-31.5844` edge `-0.0123` maxDD `-3.9061`
- `news_risk_high->equity_24h` score `-4.8411` n `62` status `ready` deltaP `21.3877` edge `0.3954` maxDD `-86.0244`
- `news_risk_high->commodity_24h` score `-10.6624` n `62` status `ready` deltaP `-29.3123` edge `-0.1271` maxDD `-27.9483`
- `news_risk_high->crypto_major_24h` score `-14.3769` n `62` status `ready` deltaP `-30.6228` edge `-0.1436` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
