# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T09:37:26.815638+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8411`

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

- `market_context_high->unknown_24h` score `1380.4126` n `135` status `ready` deltaP `-3.7616` edge `115.1522` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `40.2634` n `148` status `ready` deltaP `5.0882` edge `3.3366` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.8079` n `135` status `ready` deltaP `27.1875` edge `0.0382` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.293` n `148` status `ready` deltaP `8.63` edge `0.0027` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1627` n `148` status `ready` deltaP `9.8261` edge `0.0079` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1145` n `148` status `ready` deltaP `7.8734` edge `0.0075` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3852` n `148` status `ready` deltaP `6.9024` edge `0.0329` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.4374` n `135` status `ready` deltaP `12.0833` edge `0.0206` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.4644` n `148` status `ready` deltaP `6.4766` edge `0.04` maxDD `-1.0837`
- `market_context_high->commodity_1h` score `-0.6645` n `148` status `ready` deltaP `-0.5219` edge `0.0065` maxDD `-1.0053`
- `market_context_high->metal_4h` score `-0.6738` n `148` status `ready` deltaP `10.0198` edge `0.0009` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.7432` n `148` status `ready` deltaP `-3.524` edge `-0.0035` maxDD `-1.4631`
- `market_context_high->equity_1h` score `-1.5558` n `148` status `ready` deltaP `-0.3035` edge `-0.0062` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6352` n `148` status `ready` deltaP `2.4599` edge `0.0103` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-1.9146` n `135` status `ready` deltaP `8.0671` edge `0.0831` maxDD `-15.7143`
- `market_context_high->metal_24h` score `-2.1655` n `135` status `ready` deltaP `7.0718` edge `0.0502` maxDD `-8.2244`
- `market_context_high->index_4h` score `-3.0706` n `148` status `ready` deltaP `-9.3895` edge `-0.0311` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.2244` n `135` status `ready` deltaP `0.544` edge `0.0687` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.5092` n `148` status `ready` deltaP `3.5761` edge `-0.0418` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.6566` n `148` status `ready` deltaP `-4.6844` edge `-0.1706` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
