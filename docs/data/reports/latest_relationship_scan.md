# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T14:07:26.693562+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3915`

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

- `news_risk_high->equity_24h` score `0.6045` n `114` status `ready` deltaP `25.5509` edge `1.0658` maxDD `-86.0244`
- `news_risk_high->index_4h` score `0.1339` n `114` status `ready` deltaP `10.6413` edge `0.0144` maxDD `-1.7877`
- `news_risk_high->index_1h` score `-0.282` n `114` status `ready` deltaP `5.4759` edge `0.0015` maxDD `-0.9325`
- `news_risk_high->index_24h` score `-0.4788` n `114` status `ready` deltaP `-1.3962` edge `0.1314` maxDD `-6.6786`
- `news_risk_high->fx_1h` score `-0.4941` n `114` status `ready` deltaP `-0.2547` edge `0.0005` maxDD `-0.1984`
- `news_risk_high->crypto_alt_1h` score `-0.5344` n `114` status `ready` deltaP `2.2455` edge `0.0393` maxDD `-5.8225`
- `news_risk_high->crypto_alt_4h` score `-0.6579` n `114` status `ready` deltaP `3.014` edge `0.1592` maxDD `-14.0916`
- `news_risk_high->equity_4h` score `-0.8092` n `114` status `ready` deltaP `10.9462` edge `0.1395` maxDD `-18.3927`
- `news_risk_high->crypto_major_1h` score `-0.8437` n `114` status `ready` deltaP `-2.4189` edge `0.0085` maxDD `-4.7103`
- `news_risk_high->metal_1h` score `-0.8623` n `114` status `ready` deltaP `-1.9041` edge `-0.0088` maxDD `-1.0293`
- `news_risk_high->crypto_major_4h` score `-1.0428` n `114` status `ready` deltaP `-2.3669` edge `0.0632` maxDD `-9.1553`
- `news_risk_high->fx_4h` score `-1.0839` n `114` status `ready` deltaP `-1.2142` edge `-0.0013` maxDD `-0.4745`
- `news_risk_high->fx_24h` score `-1.2286` n `114` status `ready` deltaP `-13.856` edge `-0.0017` maxDD `-0.4086`
- `news_risk_high->equity_1h` score `-1.4018` n `114` status `ready` deltaP `-0.8772` edge `0.0164` maxDD `-10.2217`
- `news_risk_high->metal_4h` score `-2.1216` n `114` status `ready` deltaP `-5.0305` edge `-0.0426` maxDD `-2.3861`
- `news_risk_high->commodity_1h` score `-2.8352` n `114` status `ready` deltaP `-13.9064` edge `-0.0069` maxDD `-3.2657`
- `news_risk_high->metal_24h` score `-3.257` n `114` status `ready` deltaP `-2.3644` edge `-0.2122` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-5.0659` n `114` status `ready` deltaP `-24.754` edge `-0.0217` maxDD `-9.5011`
- `news_risk_high->crypto_major_24h` score `-6.1407` n `114` status `ready` deltaP `-16.357` edge `0.1721` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-10.3564` n `114` status `ready` deltaP `-23.9634` edge `-0.0015` maxDD `-38.809`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
