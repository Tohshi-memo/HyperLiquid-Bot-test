# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T03:37:30.487763+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11865`

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

- `market_context_high->commodity_24h` score `3.9082` n `69` status `ready` deltaP `34.5259` edge `0.1304` maxDD `-0.4576`
- `market_context_high->equity_24h` score `1.7393` n `69` status `ready` deltaP `16.4779` edge `0.056` maxDD `-0.6726`
- `market_context_high->crypto_major_24h` score `1.5204` n `69` status `ready` deltaP `2.4079` edge `0.2483` maxDD `-5.6792`
- `market_context_high->index_24h` score `1.4745` n `69` status `ready` deltaP `21.7014` edge `-0.0218` maxDD `0.0`
- `market_context_high->commodity_4h` score `1.2391` n `102` status `ready` deltaP `13.9886` edge `0.0583` maxDD `-0.864`
- `market_context_high->metal_4h` score `-0.2837` n `102` status `ready` deltaP `15.7312` edge `0.0122` maxDD `-4.5909`
- `market_context_high->commodity_1h` score `-0.2982` n `110` status `ready` deltaP `-0.2776` edge `0.0093` maxDD `-0.9873`
- `market_context_high->fx_1h` score `-0.3396` n `110` status `ready` deltaP `-0.7485` edge `-0.0015` maxDD `-0.2968`
- `market_context_high->metal_1h` score `-0.5362` n `110` status `ready` deltaP `3.6581` edge `0.0025` maxDD `-1.7257`
- `market_context_high->fx_4h` score `-0.7426` n `102` status `ready` deltaP `-4.0292` edge `-0.0071` maxDD `-0.5665`
- `market_context_high->crypto_major_4h` score `-0.7723` n `102` status `ready` deltaP `2.1132` edge `0.0077` maxDD `-4.6638`
- `market_context_high->index_1h` score `-0.9371` n `110` status `ready` deltaP `-3.7098` edge `-0.0012` maxDD `-0.5064`
- `market_context_high->crypto_alt_1h` score `-1.1005` n `110` status `ready` deltaP `-4.3849` edge `-0.0109` maxDD `-4.4101`
- `market_context_high->equity_1h` score `-1.1057` n `110` status `ready` deltaP `-5.4953` edge `-0.022` maxDD `-3.3165`
- `market_context_high->crypto_major_1h` score `-1.7775` n `110` status `ready` deltaP `-4.3849` edge `-0.0185` maxDD `-4.0312`
- `market_context_high->index_4h` score `-1.8702` n `102` status `ready` deltaP `-10.5392` edge `-0.0047` maxDD `-0.8045`
- `market_context_high->fx_24h` score `-3.1679` n `69` status `ready` deltaP `-30.4499` edge `-0.0424` maxDD `-1.8596`
- `market_context_high->equity_4h` score `-3.435` n `102` status `ready` deltaP `-18.4033` edge `-0.137` maxDD `-8.1221`
- `market_context_high->metal_24h` score `-5.5072` n `69` status `ready` deltaP `-23.196` edge `-0.0531` maxDD `-7.0954`
- `market_context_high->crypto_alt_4h` score `-5.688` n `102` status `ready` deltaP `-8.7368` edge `-0.0476` maxDD `-16.786`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
