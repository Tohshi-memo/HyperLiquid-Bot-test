# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T09:52:26.115932+00:00`
- Price records: `672`
- Market context records: `8503`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5871`

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

- `news_risk_high->unknown_24h` score `6274.5206` n `52` status `ready` deltaP `44.5646` edge `522.6217` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.0716` n `64` status `ready` deltaP `22.1799` edge `0.4178` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0655` n `64` status `ready` deltaP `17.1113` edge `0.0771` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7493` n `64` status `ready` deltaP `16.1022` edge `0.0861` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.9439` n `64` status `ready` deltaP `5.8308` edge `0.1597` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.9006` n `64` status `ready` deltaP `14.4817` edge `0.1581` maxDD `-5.8012`
- `market_context_high->equity_1h` score `0.7338` n `32` status `ready` deltaP `5.1647` edge `0.0517` maxDD `-0.9985`
- `news_risk_high->crypto_alt_1h` score `0.6183` n `64` status `ready` deltaP `9.9083` edge `0.0659` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3937` n `64` status `ready` deltaP `7.3634` edge `0.0526` maxDD `-2.0972`
- `market_context_high->index_1h` score `0.2987` n `32` status `ready` deltaP `8.9072` edge `-0.0014` maxDD `-0.2417`
- `news_risk_high->fx_1h` score `0.1446` n `64` status `ready` deltaP `6.3342` edge `0.0044` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.079` n `64` status `ready` deltaP `12.0808` edge `0.0218` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0387` n `64` status `ready` deltaP `4.2197` edge `0.0085` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0697` n `64` status `ready` deltaP `1.1052` edge `0.0313` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.1167` n `64` status `ready` deltaP `3.4057` edge `0.0079` maxDD `-0.5599`
- `market_context_high->crypto_major_1h` score `-0.2909` n `32` status `ready` deltaP `2.6759` edge `-0.0142` maxDD `-1.6077`
- `market_context_high->metal_1h` score `-0.3124` n `32` status `ready` deltaP `0.2807` edge `-0.0099` maxDD `-0.5617`
- `market_context_high->commodity_1h` score `-0.7418` n `32` status `ready` deltaP `-1.1789` edge `-0.0247` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.8607` n `32` status `ready` deltaP `-10.4042` edge `0.0059` maxDD `-1.7509`
- `news_risk_high->commodity_1h` score `-1.7119` n `64` status `ready` deltaP `-4.3039` edge `-0.0354` maxDD `-2.9516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
