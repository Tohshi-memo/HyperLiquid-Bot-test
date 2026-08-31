# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T22:07:25.379550+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `risk_on_high->unknown_4h` score `7.7922` n `107` status `ready` deltaP `23.4215` edge `0.5549` maxDD `-2.2689`
- `risk_on_and_context->unknown_4h` score `7.7922` n `107` status `ready` deltaP `23.4215` edge `0.5549` maxDD `-2.2689`
- `market_context_high->unknown_4h` score `6.245` n `159` status `ready` deltaP `20.1181` edge `0.4557` maxDD `-2.5526`
- `risk_on_high->unknown_1h` score `2.1789` n `107` status `ready` deltaP `5.4676` edge `0.2028` maxDD `-1.9477`
- `risk_on_and_context->unknown_1h` score `2.1789` n `107` status `ready` deltaP `5.4676` edge `0.2028` maxDD `-1.9477`
- `market_context_high->unknown_1h` score `1.955` n `159` status `ready` deltaP `4.8093` edge `0.1939` maxDD `-2.0436`
- `risk_on_high->commodity_24h` score `1.8493` n `92` status `ready` deltaP `14.2814` edge `0.1577` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.8493` n `92` status `ready` deltaP `14.2814` edge `0.1577` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.2732` n `61` status `ready` deltaP `2.5719` edge `0.1236` maxDD `-1.1049`
- `risk_on_high->fx_24h` score `0.7548` n `92` status `ready` deltaP `40.859` edge `0.0229` maxDD `-3.5486`
- `risk_on_and_context->fx_24h` score `0.7548` n `92` status `ready` deltaP `40.859` edge `0.0229` maxDD `-3.5486`
- `risk_on_high->crypto_alt_24h` score `0.423` n `92` status `ready` deltaP `12.6888` edge `0.66` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.423` n `92` status `ready` deltaP `12.6888` edge `0.66` maxDD `-42.8959`
- `market_context_high->commodity_1h` score `0.1887` n `159` status `ready` deltaP `9.4801` edge `0.0175` maxDD `-1.5315`
- `news_risk_high->commodity_4h` score `0.1799` n `61` status `ready` deltaP `6.2725` edge `0.0229` maxDD `-1.3325`
- `news_risk_high->fx_4h` score `0.1086` n `61` status `ready` deltaP `10.196` edge `0.0004` maxDD `-0.7461`
- `risk_on_high->commodity_1h` score `0.0076` n `107` status `ready` deltaP `5.7712` edge `0.0147` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `0.0076` n `107` status `ready` deltaP `5.7712` edge `0.0147` maxDD `-0.8428`
- `risk_on_high->index_1h` score `-0.0446` n `107` status `ready` deltaP `5.8481` edge `-0.0002` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0446` n `107` status `ready` deltaP `5.8481` edge `-0.0002` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
