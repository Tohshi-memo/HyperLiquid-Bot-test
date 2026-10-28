# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T22:37:32.304294+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8352`

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

- `market_context_high->unknown_24h` score `1242.0375` n `148` status `ready` deltaP `-2.135` edge `103.6101` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.0708` n `149` status `ready` deltaP `4.385` edge `1.7419` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.0651` n `148` status `ready` deltaP `21.4574` edge `0.0145` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.22` n `149` status `ready` deltaP `7.8678` edge `0.0017` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.0785` n `149` status `ready` deltaP `7.3815` edge `0.0041` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0995` n `149` status `ready` deltaP `8.327` edge `0.0064` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.3361` n `149` status `ready` deltaP `7.8112` edge `0.0418` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.3764` n `149` status `ready` deltaP `6.3809` edge `0.0375` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.6476` n `149` status `ready` deltaP `-0.4903` edge `0.0077` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.7294` n `148` status `ready` deltaP `11.0173` edge `0.023` maxDD `-1.2451`
- `market_context_high->index_1h` score `-0.7328` n `149` status `ready` deltaP `-3.4743` edge `-0.0025` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8674` n `149` status `ready` deltaP `7.227` edge `-0.0053` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.3953` n `149` status `ready` deltaP `1.0891` edge `0.0051` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5892` n `149` status `ready` deltaP `2.5961` edge `0.0153` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1174` n `149` status `ready` deltaP `-10.0937` edge `-0.0303` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.4674` n `149` status `ready` deltaP `3.5092` edge `-0.036` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.5553` n `148` status `ready` deltaP `-0.2393` edge `0.0073` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-3.6603` n `148` status `ready` deltaP `-1.9285` edge `0.0293` maxDD `-29.1905`
- `market_context_high->equity_24h` score `-4.163` n `148` status `ready` deltaP `4.0071` edge `-0.0772` maxDD `-15.7143`
- `market_context_high->equity_4h` score `-5.5041` n `149` status `ready` deltaP `-4.3921` edge `-0.153` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
