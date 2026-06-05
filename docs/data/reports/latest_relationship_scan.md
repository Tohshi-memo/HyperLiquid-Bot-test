# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T13:22:28.511747+00:00`
- Price records: `672`
- Market context records: `2972`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `16.3642` n `110` status `ready` deltaP `9.1288` edge `1.6945` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `9.7051` n `110` status `ready` deltaP `35.4861` edge `0.6086` maxDD `-1.2464`
- `market_context_high->unknown_24h` score `9.5358` n `110` status `ready` deltaP `16.1427` edge `0.7335` maxDD `-1.7175`
- `market_context_high->equity_24h` score `7.1373` n `110` status `ready` deltaP `16.4773` edge `0.6853` maxDD `-12.6963`
- `market_context_high->index_24h` score `3.8756` n `110` status `ready` deltaP `16.3858` edge `0.3118` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.0009` n `111` status `ready` deltaP `15.9471` edge `0.1827` maxDD `-0.7819`
- `market_context_high->index_4h` score `1.8709` n `111` status `ready` deltaP `19.3557` edge `0.1057` maxDD `-1.9733`
- `market_context_high->crypto_alt_4h` score `1.12` n `111` status `ready` deltaP `22.653` edge `0.4487` maxDD `-30.8239`
- `market_context_high->equity_1h` score `1.0153` n `111` status `ready` deltaP `7.2221` edge `0.0698` maxDD `-1.0004`
- `market_context_high->index_1h` score `0.4817` n `111` status `ready` deltaP `7.9625` edge `0.0262` maxDD `-0.7983`
- `market_context_high->commodity_4h` score `0.4696` n `111` status `ready` deltaP `10.5554` edge `0.0773` maxDD `-4.6634`
- `market_context_high->crypto_alt_1h` score `0.2782` n `111` status `ready` deltaP `9.9113` edge `0.1331` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `0.089` n `111` status `ready` deltaP `10.0529` edge `0.098` maxDD `-9.622`
- `market_context_high->unknown_4h` score `-0.2503` n `111` status `ready` deltaP `1.7812` edge `0.0726` maxDD `-3.7602`
- `market_context_high->fx_1h` score `-0.3548` n `111` status `ready` deltaP `-0.4423` edge `0.0041` maxDD `-0.1244`
- `market_context_high->commodity_1h` score `-0.603` n `111` status `ready` deltaP `-1.6453` edge `-0.0038` maxDD `-3.3365`
- `market_context_high->metal_1h` score `-0.7887` n `111` status `ready` deltaP `-2.1107` edge `0.0017` maxDD `-3.4325`
- `market_context_high->unknown_1h` score `-0.9818` n `111` status `ready` deltaP `2.5598` edge `-0.0258` maxDD `-3.1801`
- `market_context_high->fx_4h` score `-1.3555` n `111` status `ready` deltaP `-5.5785` edge `0.0021` maxDD `-0.5631`
- `market_context_high->crypto_major_4h` score `-1.4872` n `111` status `ready` deltaP `9.6105` edge `0.2578` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
