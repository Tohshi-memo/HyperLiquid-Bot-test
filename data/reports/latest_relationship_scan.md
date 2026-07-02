# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T12:37:27.216190+00:00`
- Price records: `672`
- Market context records: `5455`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11440`

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

- `market_context_high->crypto_major_24h` score `3.6571` n `192` status `ready` deltaP `17.1875` edge `0.6442` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.646` n `197` status `ready` deltaP `14.9777` edge `0.3499` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.2315` n `197` status `ready` deltaP `12.0783` edge `0.2693` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `2.0283` n `197` status `ready` deltaP `10.0509` edge `0.2661` maxDD `-9.46`
- `market_context_high->equity_24h` score `0.5872` n `192` status `ready` deltaP `8.8542` edge `0.4978` maxDD `-31.6316`
- `market_context_high->equity_1h` score `0.4451` n `199` status `ready` deltaP `8.0131` edge `0.0802` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.1367` n `199` status `ready` deltaP `6.6342` edge `0.0165` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.1104` n `192` status `ready` deltaP `10.2431` edge `0.0318` maxDD `-0.9375`
- `market_context_high->metal_1h` score `-0.2437` n `199` status `ready` deltaP `4.1111` edge `0.0198` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.3489` n `199` status `ready` deltaP `0.8072` edge `0.0617` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.4662` n `199` status `ready` deltaP `1.9942` edge `0.0724` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.5393` n `199` status `ready` deltaP `0.5612` edge `0.0002` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.8868` n `197` status `ready` deltaP `7.0083` edge `0.0403` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.0573` n `197` status `ready` deltaP `1.5158` edge `0.0043` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.3541` n `199` status `ready` deltaP `-1.9724` edge `-0.0049` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.6201` n `192` status `ready` deltaP `13.5416` edge `0.0715` maxDD `-15.8923`
- `market_context_high->metal_4h` score `-2.5947` n `197` status `ready` deltaP `-7.8146` edge `-0.0281` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2514` n `197` status `ready` deltaP `-6.0813` edge `-0.0423` maxDD `-14.3822`
- `market_context_high->crypto_alt_24h` score `-7.1239` n `192` status `ready` deltaP `8.3333` edge `0.2205` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.1516` n `192` status `ready` deltaP `-3.6458` edge `-0.1548` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
