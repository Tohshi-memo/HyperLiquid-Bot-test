# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T10:07:31.391778+00:00`
- Price records: `672`
- Market context records: `8291`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5892`

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

- `news_risk_high->unknown_24h` score `5949.6242` n `54` status `ready` deltaP `34.2593` edge `495.6157` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.7903` n `54` status `ready` deltaP `25.1637` edge `0.4578` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8975` n `54` status `ready` deltaP `20.9304` edge `0.1328` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5538` n `54` status `ready` deltaP `21.5052` edge `0.0885` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9447` n `54` status `ready` deltaP `8.9544` edge `0.259` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8255` n `54` status `ready` deltaP `14.4045` edge `0.0995` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.5178` n `54` status `ready` deltaP `10.3072` edge `0.0975` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.5161` n `54` status `ready` deltaP `17.0789` edge `0.2197` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.0284` n `54` status `ready` deltaP `9.4343` edge `0.0696` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.3848` n `54` status `ready` deltaP `6.1544` edge `0.0199` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1681` n `54` status `ready` deltaP `6.9971` edge `0.003` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0688` n `54` status `ready` deltaP `3.4043` edge `0.0119` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4532` n `54` status `ready` deltaP `4.6127` edge `0.0069` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1084` n `54` status `ready` deltaP `-8.5108` edge `-0.0404` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.038` n `54` status `ready` deltaP `-20.544` edge `-0.0485` maxDD `-5.4165`
- `news_risk_high->metal_24h` score `-5.667` n `54` status `ready` deltaP `-20.7755` edge `-0.0567` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.7348` n `54` status `ready` deltaP `-30.3523` edge `-0.1948` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-10.9358` n `54` status `ready` deltaP `-5.9606` edge `-0.2776` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-11.9807` n `54` status `ready` deltaP `-23.5532` edge `-0.2911` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-31.9186` n `54` status `ready` deltaP `-11.8635` edge `-1.1283` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
