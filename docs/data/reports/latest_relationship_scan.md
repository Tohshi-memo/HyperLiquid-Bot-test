# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T10:52:25.362000+00:00`
- Price records: `672`
- Market context records: `5655`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8684`

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

- `market_context_high->equity_24h` score `2.4128` n `186` status `ready` deltaP `15.0537` edge `0.6086` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.8246` n `237` status `ready` deltaP `11.0045` edge `0.2246` maxDD `-14.0065`
- `market_context_high->fx_24h` score `0.5345` n `186` status `ready` deltaP `18.4028` edge `0.0563` maxDD `-2.0891`
- `market_context_high->equity_4h` score `0.5013` n `237` status `ready` deltaP `7.6863` edge `0.1544` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.0399` n `237` status `ready` deltaP `6.8315` edge `0.1427` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2713` n `246` status `ready` deltaP `1.7757` edge `0.001` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3649` n `246` status `ready` deltaP `5.6083` edge `0.0329` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5593` n `246` status `ready` deltaP `-0.5988` edge `-0.0002` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.7118` n `246` status `ready` deltaP `0.9213` edge `0.0307` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.83` n `246` status `ready` deltaP `2.8029` edge `0.0367` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-0.9261` n `246` status `ready` deltaP `0.4917` edge `-0.0039` maxDD `-3.7906`
- `market_context_high->index_1h` score `-0.9293` n `246` status `ready` deltaP `0.6` edge `0.0054` maxDD `-0.9472`
- `market_context_high->fx_4h` score `-1.2591` n `237` status `ready` deltaP `2.2853` edge `0.0067` maxDD `-1.335`
- `market_context_high->index_4h` score `-2.0355` n `237` status `ready` deltaP `-1.689` edge `0.0088` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.3584` n `186` status `ready` deltaP `9.0782` edge `0.0358` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0607` n `237` status `ready` deltaP `-14.8265` edge `-0.0552` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.8009` n `237` status `ready` deltaP `-2.1875` edge `-0.0346` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.5746` n `186` status `ready` deltaP `4.0211` edge `0.046` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.4187` n `186` status `ready` deltaP `-13.5641` edge `-0.2528` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-12.7493` n `186` status `ready` deltaP `-14.6169` edge `-0.1041` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
