# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T09:52:33.214733+00:00`
- Price records: `672`
- Market context records: `8290`
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

- `news_risk_high->unknown_24h` score `5949.3595` n `54` status `ready` deltaP `34.0857` edge `495.5948` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.8421` n `54` status `ready` deltaP `25.3161` edge `0.4611` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9155` n `54` status `ready` deltaP `21.0801` edge `0.1333` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5756` n `54` status `ready` deltaP `21.6576` edge `0.0893` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9612` n `54` status `ready` deltaP `9.1069` edge `0.2601` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8255` n `54` status `ready` deltaP `14.4045` edge `0.0995` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.52` n `54` status `ready` deltaP `17.0789` edge `0.2202` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `1.519` n `54` status `ready` deltaP `10.3072` edge `0.0976` maxDD `-1.1783`
- `news_risk_high->metal_4h` score `1.0138` n `54` status `ready` deltaP `9.2818` edge `0.0694` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.3848` n `54` status `ready` deltaP `6.1544` edge `0.0199` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1603` n `54` status `ready` deltaP `6.8474` edge `0.003` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0832` n `54` status `ready` deltaP `3.2546` edge `0.0117` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4532` n `54` status `ready` deltaP `4.6127` edge `0.0069` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.0916` n `54` status `ready` deltaP `-8.3611` edge `-0.04` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.038` n `54` status `ready` deltaP `-20.544` edge `-0.0485` maxDD `-5.4165`
- `news_risk_high->metal_24h` score `-5.6447` n `54` status `ready` deltaP `-20.6019` edge `-0.056` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.719` n `54` status `ready` deltaP `-30.1999` edge `-0.1945` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-10.9454` n `54` status `ready` deltaP `-5.9606` edge `-0.2784` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-11.9982` n `54` status `ready` deltaP `-23.7268` edge `-0.2914` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-31.8898` n `54` status `ready` deltaP `-11.8635` edge `-1.1259` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
