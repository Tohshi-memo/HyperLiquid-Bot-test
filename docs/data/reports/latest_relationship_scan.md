# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T07:37:28.428388+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4274`

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

- `news_risk_high->crypto_alt_4h` score `-0.0341` n `140` status `ready` deltaP `7.9616` edge `0.2062` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4963` n `140` status `ready` deltaP `3.1437` edge `0.0382` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6534` n `140` status `ready` deltaP `-1.7836` edge `-0.0018` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7387` n `140` status `ready` deltaP `2.6133` edge `0.001` maxDD `-1.3981`
- `news_risk_high->index_4h` score `-1.3789` n `140` status `ready` deltaP `2.7439` edge `0.0079` maxDD `-3.9042`
- `news_risk_high->fx_4h` score `-1.5332` n `140` status `ready` deltaP `-8.8502` edge `-0.0124` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.8991` n `140` status `ready` deltaP `-10.519` edge `0.0768` maxDD `-6.6786`
- `news_risk_high->metal_1h` score `-2.0783` n `140` status `ready` deltaP `-6.3601` edge `-0.0156` maxDD `-2.5487`
- `news_risk_high->crypto_major_1h` score `-2.5096` n `140` status `ready` deltaP `-5.0599` edge `-0.0185` maxDD `-8.2184`
- `news_risk_high->fx_24h` score `-2.5468` n `140` status `ready` deltaP `-24.0484` edge `-0.0259` maxDD `-1.8902`
- `news_risk_high->commodity_1h` score `-2.5809` n `140` status `ready` deltaP `-11.6125` edge `-0.001` maxDD `-3.2657`
- `news_risk_high->equity_1h` score `-3.5124` n `140` status `ready` deltaP `-5.1968` edge `0.0023` maxDD `-15.8287`
- `news_risk_high->crypto_major_4h` score `-3.734` n `140` status `ready` deltaP `-7.2169` edge `0.025` maxDD `-17.0446`
- `news_risk_high->commodity_4h` score `-4.3465` n `140` status `ready` deltaP `-18.3711` edge `-0.0043` maxDD `-9.5011`
- `news_risk_high->metal_4h` score `-5.1329` n `140` status `ready` deltaP `-11.2674` edge `-0.0686` maxDD `-8.3886`
- `news_risk_high->equity_24h` score `-5.5845` n `140` status `ready` deltaP `12.3554` edge `0.686` maxDD `-87.0329`
- `news_risk_high->metal_24h` score `-7.9419` n `140` status `ready` deltaP `-14.7454` edge `-0.2751` maxDD `-13.074`
- `news_risk_high->equity_4h` score `-8.3734` n `140` status `ready` deltaP `3.2012` edge `0.0288` maxDD `-47.1674`
- `news_risk_high->commodity_24h` score `-10.6599` n `140` status `ready` deltaP `-19.523` edge `0.0679` maxDD `-43.7525`
- `news_risk_high->crypto_alt_24h` score `-12.2643` n `140` status `ready` deltaP `6.5126` edge `0.0837` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
