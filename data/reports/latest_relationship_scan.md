# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T09:52:26.501065+00:00`
- Price records: `672`
- Market context records: `7657`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14697`

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

- `market_context_high->index_1h` score `0.0422` n `146` status `ready` deltaP `6.3619` edge `0.0109` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.2017` n `146` status `ready` deltaP `7.7065` edge `0.0188` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.291` n `146` status `ready` deltaP `1.456` edge `0.0162` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3539` n `145` status `ready` deltaP `9.2803` edge `0.0174` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.4248` n `146` status `ready` deltaP `1.0777` edge `-0.0046` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.5517` n `146` status `ready` deltaP `4.9262` edge `0.0478` maxDD `-7.7764`
- `market_context_high->metal_1h` score `-0.6395` n `146` status `ready` deltaP `1.0889` edge `0.0153` maxDD `-1.0307`
- `market_context_high->commodity_4h` score `-0.7092` n `146` status `ready` deltaP `1.6066` edge `0.0047` maxDD `-2.2943`
- `market_context_high->index_4h` score `-0.7269` n `146` status `ready` deltaP `7.6871` edge `0.0257` maxDD `-3.2774`
- `market_context_high->fx_1h` score `-0.7422` n `146` status `ready` deltaP `-1.4727` edge `-0.0021` maxDD `-0.6615`
- `market_context_high->commodity_24h` score `-0.9808` n `145` status `ready` deltaP `8.0128` edge `0.0232` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `-1.1269` n `146` status `ready` deltaP `1.8251` edge `0.0423` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.2065` n `146` status `ready` deltaP `9.1317` edge `0.0522` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.5038` n `146` status `ready` deltaP `-0.9843` edge `-0.0564` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.7045` n `146` status `ready` deltaP `-2.7376` edge `0.0454` maxDD `-4.6535`
- `market_context_high->equity_4h` score `-1.7504` n `146` status `ready` deltaP `0.532` edge `0.1864` maxDD `-20.4824`
- `market_context_high->equity_24h` score `-1.8513` n `145` status `ready` deltaP `13.667` edge `0.1621` maxDD `-34.5784`
- `market_context_high->metal_24h` score `-2.2567` n `146` status `ready` deltaP `-3.2772` edge `0.0582` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.7803` n `146` status `ready` deltaP `-8.6465` edge `-0.0056` maxDD `-2.1425`
- `market_context_high->index_24h` score `-3.4644` n `145` status `ready` deltaP `-20.0397` edge `-0.0258` maxDD `-8.114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
