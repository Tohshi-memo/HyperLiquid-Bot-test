# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T21:07:16.700298+00:00`
- Price records: `672`
- Market context records: `1154`
- Flow alert records: `5226`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8749`

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

- `market_context_high->crypto_major_24h` score `20.2074` n `148` status `ready` deltaP `44.3459` edge `1.5015` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `9.8325` n `148` status `ready` deltaP `20.7161` edge `0.8829` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.8508` n `148` status `ready` deltaP `20.1952` edge `0.6126` maxDD `-6.4404`
- `market_context_high->index_24h` score `6.1643` n `148` status `ready` deltaP `18.8063` edge `0.4441` maxDD `-3.4627`
- `market_context_high->metal_24h` score `5.6636` n `148` status `ready` deltaP `-2.1772` edge `0.6532` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.5199` n `164` status `ready` deltaP `12.3475` edge `0.194` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.1977` n `164` status `ready` deltaP `9.4512` edge `0.1051` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5245` n `164` status `ready` deltaP `7.8903` edge `0.0228` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4254` n `164` status `ready` deltaP `3.6329` edge `0.049` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `0.254` n `164` status `ready` deltaP `9.1464` edge `0.1637` maxDD `-8.3693`
- `market_context_high->fx_1h` score `0.1126` n `164` status `ready` deltaP `8.1532` edge `0.0006` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.1063` n `164` status `ready` deltaP `7.799` edge `0.0382` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.2292` n `164` status `ready` deltaP `3.2971` edge `0.0432` maxDD `-3.4088`
- `market_context_high->metal_1h` score `-0.2625` n `164` status `ready` deltaP `6.7` edge `-0.0055` maxDD `-2.2164`
- `market_context_high->fx_4h` score `-0.8911` n `164` status `ready` deltaP `-1.8293` edge `-0.0024` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-0.944` n `164` status `ready` deltaP `6.25` edge `0.1338` maxDD `-16.7194`
- `market_context_high->commodity_1h` score `-1.187` n `164` status `ready` deltaP `-2.3003` edge `-0.0028` maxDD `-3.7959`
- `market_context_high->unknown_24h` score `-1.9484` n `148` status `ready` deltaP `4.3497` edge `0.0816` maxDD `-10.1706`
- `market_context_high->metal_4h` score `-2.4681` n `164` status `ready` deltaP `6.8598` edge `-0.056` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-2.5989` n `164` status `ready` deltaP `8.2317` edge `-0.1498` maxDD `-6.7322`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
