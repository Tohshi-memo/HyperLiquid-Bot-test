# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T21:52:27.496076+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8464`

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

- `market_context_high->unknown_24h` score `1239.6855` n `148` status `ready` deltaP `-2.135` edge `103.4141` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.0084` n `149` status `ready` deltaP `4.385` edge `1.7367` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.138` n `148` status `ready` deltaP `21.9782` edge `0.0171` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1961` n `149` status `ready` deltaP `7.5684` edge `0.0017` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.1174` n `149` status `ready` deltaP `8.0276` edge `0.0061` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.1186` n `149` status `ready` deltaP `6.9242` edge `0.0038` maxDD `-0.4545`
- `market_context_high->commodity_4h` score `-0.3097` n `149` status `ready` deltaP `7.8112` edge `0.044` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.4146` n `149` status `ready` deltaP `6.0815` edge `0.0346` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.6177` n `149` status `ready` deltaP `-0.1909` edge `0.0082` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.6685` n `148` status `ready` deltaP `11.5381` edge `0.0246` maxDD `-1.2451`
- `market_context_high->index_1h` score `-0.7577` n `149` status `ready` deltaP `-3.9234` edge `-0.0027` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8777` n `149` status `ready` deltaP `7.0746` edge `-0.0056` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.4179` n `149` status `ready` deltaP `0.7897` edge `0.0042` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6437` n `149` status `ready` deltaP `2.147` edge `0.0113` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1647` n `149` status `ready` deltaP `-10.5511` edge `-0.0312` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.5103` n `149` status `ready` deltaP `3.5092` edge `-0.0415` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.5361` n `148` status `ready` deltaP `-0.2393` edge `0.0089` maxDD `-10.1587`
- `market_context_high->crypto_major_24h` score `-3.5669` n `148` status `ready` deltaP `-1.4076` edge `0.0378` maxDD `-29.1905`
- `market_context_high->equity_24h` score `-3.9257` n `148` status `ready` deltaP `4.5279` edge `-0.0609` maxDD `-15.7143`
- `market_context_high->equity_4h` score `-5.5402` n `149` status `ready` deltaP `-4.6969` edge `-0.1556` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
