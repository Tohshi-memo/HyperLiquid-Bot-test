# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T14:52:19.611228+00:00`
- Price records: `672`
- Market context records: `1640`
- Flow alert records: `6630`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->metal_24h` score `9.7377` n `176` status `ready` deltaP `27.0718` edge `0.8736` maxDD `-12.7414`
- `market_context_high->index_24h` score `3.4178` n `176` status `ready` deltaP `19.1282` edge `0.2951` maxDD `-5.3574`
- `market_context_high->crypto_alt_4h` score `2.9895` n `185` status `ready` deltaP `19.281` edge `0.387` maxDD `-16.3135`
- `market_context_high->crypto_major_4h` score `1.531` n `185` status `ready` deltaP `15.0405` edge `0.2982` maxDD `-13.3376`
- `market_context_high->equity_4h` score `1.4951` n `185` status `ready` deltaP `11.5866` edge `0.1568` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.0802` n `176` status `ready` deltaP `18.0685` edge `0.4594` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `-0.0455` n `195` status `ready` deltaP `2.9894` edge `0.0766` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `-0.0825` n `176` status `ready` deltaP `23.7307` edge `0.6935` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.4209` n `176` status `ready` deltaP `6.8142` edge `0.0244` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.4697` n `195` status `ready` deltaP `0.9159` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->equity_1h` score `-0.4913` n `195` status `ready` deltaP `1.1262` edge `0.0324` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.5195` n `185` status `ready` deltaP `-0.0009` edge `0.0423` maxDD `-3.7119`
- `market_context_high->index_1h` score `-0.6384` n `195` status `ready` deltaP `0.3555` edge `0.0076` maxDD `-1.7205`
- `market_context_high->crypto_major_1h` score `-0.699` n `195` status `ready` deltaP `-0.129` edge `0.0391` maxDD `-5.5617`
- `market_context_high->commodity_1h` score `-0.7524` n `195` status `ready` deltaP `1.986` edge `-0.0048` maxDD `-6.0587`
- `market_context_high->crypto_alt_24h` score `-0.8041` n `176` status `ready` deltaP `24.165` edge `0.9528` maxDD `-88.8062`
- `market_context_high->metal_1h` score `-1.3611` n `195` status `ready` deltaP `2.4989` edge `0.0035` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.5017` n `185` status `ready` deltaP `7.3266` edge `0.0952` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-2.1021` n `185` status `ready` deltaP `-10.318` edge `-0.0135` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.5984` n `185` status `ready` deltaP `8.8584` edge `-0.1318` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
