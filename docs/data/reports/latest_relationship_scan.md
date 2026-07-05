# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T03:22:30.274981+00:00`
- Price records: `672`
- Market context records: `5731`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8882`

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

- `market_context_high->equity_24h` score `0.9024` n `218` status `ready` deltaP `15.703` edge `0.5189` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1167` n `281` status `ready` deltaP `7.1983` edge `0.1256` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2303` n `285` status `ready` deltaP `2.6363` edge `0.001` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4136` n `285` status `ready` deltaP `2.234` edge `-0.0004` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6118` n `285` status `ready` deltaP `3.3617` edge `0.0273` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6172` n `285` status `ready` deltaP `0.5873` edge `0.0038` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.7973` n `285` status `ready` deltaP `3.2304` edge `0.0355` maxDD `-5.5448`
- `market_context_high->commodity_1h` score `-0.801` n `285` status `ready` deltaP `-2.3369` edge `-0.0064` maxDD `-3.7906`
- `market_context_high->crypto_alt_1h` score `-0.9192` n `285` status `ready` deltaP `1.6352` edge `0.0329` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-1.1196` n `218` status `ready` deltaP `10.8611` edge `0.0424` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1553` n `281` status `ready` deltaP `1.5022` edge `0.0106` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2481` n `281` status `ready` deltaP `2.8226` edge `0.0057` maxDD `-1.4288`
- `market_context_high->crypto_major_4h` score `-1.959` n `281` status `ready` deltaP `7.399` edge `0.1516` maxDD `-21.1342`
- `market_context_high->metal_4h` score `-2.6194` n `281` status `ready` deltaP `-7.3442` edge `-0.0493` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.9664` n `218` status `ready` deltaP `0.8792` edge `0.0283` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-3.1836` n `281` status `ready` deltaP `5.4167` edge `0.1052` maxDD `-22.529`
- `market_context_high->commodity_4h` score `-3.7857` n `281` status `ready` deltaP `-2.9278` edge `-0.0284` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.2769` n `218` status `ready` deltaP `7.5433` edge `0.039` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.6487` n `218` status `ready` deltaP `-7.4286` edge `-0.2426` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.5463` n `218` status `ready` deltaP `-10.9216` edge `-0.0754` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
