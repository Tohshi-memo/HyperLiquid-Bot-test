# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T13:07:24.904907+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5016`

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

- `market_context_high->unknown_4h` score `124.7111` n `82` status `ready` deltaP `3.0488` edge `10.4033` maxDD `-0.4826`
- `market_context_high->unknown_1h` score `103.6337` n `94` status `ready` deltaP `-1.1689` edge `8.6854` maxDD `-0.9839`
- `market_context_high->crypto_alt_24h` score `11.1636` n `46` status `ready` deltaP `28.0042` edge `0.8709` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `10.7554` n `46` status `ready` deltaP `34.4429` edge `0.7319` maxDD `-4.5519`
- `news_risk_high->crypto_major_4h` score `10.6001` n `65` status `ready` deltaP `37.7345` edge `0.6521` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `9.0265` n `65` status `ready` deltaP `25.4434` edge `0.5926` maxDD `-0.1344`
- `news_risk_high->crypto_alt_4h` score `7.2159` n `65` status `ready` deltaP `23.75` edge `0.5774` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `5.9799` n `82` status `ready` deltaP `25.9146` edge `0.3959` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.1126` n `65` status `ready` deltaP `28.4722` edge `0.1529` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8128` n `65` status `ready` deltaP `25.9123` edge `0.206` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.0904` n `65` status `ready` deltaP `33.5906` edge `0.0598` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9424` n `65` status `ready` deltaP `12.7107` edge `0.196` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.5256` n `65` status `ready` deltaP `21.5174` edge `0.1086` maxDD `-0.993`
- `market_context_high->equity_24h` score `2.4852` n `46` status `ready` deltaP `5.5102` edge `0.2695` maxDD `-6.264`
- `market_context_high->crypto_alt_4h` score `2.2414` n `82` status `ready` deltaP `7.1646` edge `0.2971` maxDD `-7.6465`
- `market_context_high->crypto_major_1h` score `2.2389` n `94` status `ready` deltaP `15.7058` edge `0.1269` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.0974` n `65` status `ready` deltaP `25.7669` edge `0.018` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.5606` n `65` status `ready` deltaP `5.1681` edge `0.1475` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.3599` n `46` status `ready` deltaP `25.536` edge `0.1059` maxDD `-1.8102`
- `market_context_high->fx_1h` score `1.0973` n `94` status `ready` deltaP `16.6582` edge `0.0068` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
