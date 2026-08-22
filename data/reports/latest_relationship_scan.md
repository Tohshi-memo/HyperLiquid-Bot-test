# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T21:41:40.035786+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `market_context_high->unknown_1h` score `1.6021` n `144` status `ready` deltaP `6.379` edge `0.1137` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.808` n `144` status `ready` deltaP `18.8178` edge `-0.0142` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1229` n `144` status `ready` deltaP `8.5196` edge `0.0092` maxDD `-0.3527`
- `market_context_high->index_1h` score `-0.0024` n `144` status `ready` deltaP `7.2438` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1691` n `144` status `ready` deltaP `1.4721` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3096` n `144` status `ready` deltaP `5.1896` edge `0.0327` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.3171` n `144` status `ready` deltaP `7.8252` edge `-0.017` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.3917` n `144` status `ready` deltaP `-0.5032` edge `-0.005` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.5618` n `144` status `ready` deltaP `3.0657` edge `0.0111` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.8994` n `144` status `ready` deltaP `-4.5562` edge `0.0001` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.0816` n `144` status `ready` deltaP `-7.7054` edge `-0.0023` maxDD `-1.1328`
- `market_context_high->fx_24h` score `-1.1795` n `128` status `ready` deltaP `0.0` edge `0.0097` maxDD `-2.2066`
- `market_context_high->crypto_alt_1h` score `-1.6176` n `144` status `ready` deltaP `-2.8817` edge `-0.0387` maxDD `-7.9582`
- `market_context_high->equity_4h` score `-1.6824` n `144` status `ready` deltaP `-0.3557` edge `0.0683` maxDD `-16.1967`
- `market_context_high->commodity_24h` score `-2.1317` n `128` status `ready` deltaP `-5.6424` edge `0.0433` maxDD `-4.666`
- `market_context_high->crypto_alt_4h` score `-2.2641` n `144` status `ready` deltaP `3.9804` edge `-0.0684` maxDD `-7.0785`
- `market_context_high->crypto_major_1h` score `-2.4124` n `144` status `ready` deltaP `-6.4912` edge `-0.1183` maxDD `-7.8171`
- `market_context_high->metal_24h` score `-5.4141` n `128` status `ready` deltaP `-23.9583` edge `-0.2036` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.6904` n `144` status `ready` deltaP `0.254` edge `-0.3429` maxDD `-5.6395`
- `market_context_high->index_24h` score `-6.8148` n `128` status `ready` deltaP `-7.0312` edge `-0.0403` maxDD `-21.1244`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
