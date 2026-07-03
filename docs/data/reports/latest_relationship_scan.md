# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T12:07:31.600844+00:00`
- Price records: `672`
- Market context records: `5555`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11378`

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

- `market_context_high->equity_24h` score `4.4551` n `190` status `ready` deltaP `14.9178` edge `0.7797` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.8752` n `191` status `ready` deltaP `11.3428` edge `0.3099` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `1.8168` n `190` status `ready` deltaP `16.2189` edge `0.4973` maxDD `-29.6555`
- `market_context_high->equity_4h` score `1.3785` n `191` status `ready` deltaP `7.6706` edge `0.2276` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.3426` n `191` status `ready` deltaP `6.7896` edge `0.2307` maxDD `-9.46`
- `market_context_high->fx_24h` score `0.6756` n `190` status `ready` deltaP `16.3925` edge `0.0444` maxDD `-1.457`
- `market_context_high->equity_1h` score `0.2275` n `203` status `ready` deltaP `7.4526` edge `0.0658` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.035` n `203` status `ready` deltaP `5.2838` edge `0.0112` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.1937` n `203` status `ready` deltaP `2.0722` edge `0.0662` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.2878` n `203` status `ready` deltaP `1.6615` edge `0.0009` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.3134` n `203` status `ready` deltaP `3.8443` edge `0.0728` maxDD `-6.9639`
- `market_context_high->fx_4h` score `-0.627` n `191` status `ready` deltaP `3.7408` edge `0.0073` maxDD `-1.4258`
- `market_context_high->metal_1h` score `-0.6659` n `203` status `ready` deltaP `0.5892` edge `0.0081` maxDD `-2.0682`
- `market_context_high->index_4h` score `-1.5385` n `191` status `ready` deltaP `1.7726` edge `0.0209` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.6475` n `203` status `ready` deltaP `-5.5153` edge `-0.0117` maxDD `-3.7727`
- `market_context_high->index_24h` score `-2.0107` n `190` status `ready` deltaP `12.5402` edge `0.0573` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.5364` n `191` status `ready` deltaP `-11.5614` edge `-0.0485` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.7179` n `191` status `ready` deltaP `-9.9572` edge `-0.0606` maxDD `-13.9606`
- `market_context_high->crypto_alt_24h` score `-7.445` n `190` status `ready` deltaP `7.2442` edge `0.201` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.4702` n `190` status `ready` deltaP `-4.2379` edge `-0.1917` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
