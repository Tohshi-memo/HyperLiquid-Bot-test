# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T10:07:34.577538+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4861`

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

- `news_risk_high->crypto_alt_24h` score `3.591` n `110` status `ready` deltaP `22.942` edge `0.7639` maxDD `-31.1834`
- `news_risk_high->crypto_alt_4h` score `1.0508` n `132` status `ready` deltaP `8.7629` edge `0.2509` maxDD `-9.6345`
- `news_risk_high->crypto_alt_1h` score `-0.4407` n `144` status `ready` deltaP `1.9877` edge `0.0474` maxDD `-5.3723`
- `news_risk_high->fx_1h` score `-0.4959` n `144` status `ready` deltaP `1.3348` edge `-0.0024` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7022` n `144` status `ready` deltaP `-0.5032` edge `-0.0067` maxDD `-1.3981`
- `news_risk_high->metal_24h` score `-0.8648` n `110` status `ready` deltaP `13.084` edge `0.1275` maxDD `-14.0483`
- `news_risk_high->metal_1h` score `-1.2506` n `144` status `ready` deltaP `-4.3871` edge `-0.0089` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.3673` n `132` status `ready` deltaP `-5.4647` edge `-0.0137` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-2.2562` n `132` status `ready` deltaP `-4.5686` edge `-0.0287` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.4194` n `110` status `ready` deltaP `-17.9861` edge `-0.0194` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.475` n `144` status `ready` deltaP `-9.4644` edge `-0.0065` maxDD `-3.2657`
- `news_risk_high->metal_4h` score `-2.8394` n `132` status `ready` deltaP `-2.2404` edge `-0.0286` maxDD `-9.3056`
- `news_risk_high->equity_1h` score `-2.9783` n `144` status `ready` deltaP `-8.088` edge `-0.0603` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2845` n `144` status `ready` deltaP `-8.3333` edge `-0.0456` maxDD `-9.4709`
- `news_risk_high->index_24h` score `-3.3009` n `110` status `ready` deltaP `-14.5045` edge `-0.0423` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.8236` n `132` status `ready` deltaP `-12.5554` edge `-0.0152` maxDD `-8.245`
- `news_risk_high->equity_24h` score `-6.3256` n `110` status `ready` deltaP `3.709` edge `0.1738` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.2314` n `132` status `ready` deltaP `-13.9459` edge `-0.1077` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-8.5776` n `132` status `ready` deltaP `-3.9588` edge `-0.2372` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-10.5417` n `110` status `ready` deltaP `-25.5082` edge `-0.1332` maxDD `-23.6844`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
