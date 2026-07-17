# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T14:09:43.481831+00:00`
- Price records: `672`
- Market context records: `7036`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `market_context_high->fx_1h` score `-0.224` n `210` status `ready` deltaP `2.2726` edge `0.0017` maxDD `-0.3126`
- `market_context_high->fx_4h` score `-0.2502` n `210` status `ready` deltaP `12.8789` edge `0.0095` maxDD `-1.1951`
- `market_context_high->crypto_alt_1h` score `-0.3338` n `210` status `ready` deltaP `1.8363` edge `0.0314` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.6865` n `210` status `ready` deltaP `0.4505` edge `0.0001` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.708` n `210` status `ready` deltaP `-2.1885` edge `0.0006` maxDD `-2.1427`
- `market_context_high->commodity_1h` score `-0.7943` n `210` status `ready` deltaP `-3.5244` edge `-0.0167` maxDD `-1.9306`
- `market_context_high->crypto_major_1h` score `-0.9751` n `210` status `ready` deltaP `3.6869` edge `0.0294` maxDD `-7.1523`
- `market_context_high->unknown_1h` score `-1.0665` n `210` status `ready` deltaP `-2.3938` edge `0.006` maxDD `-2.6467`
- `market_context_high->unknown_24h` score `-1.5355` n `200` status `ready` deltaP `-8.5972` edge `0.329` maxDD `-19.8169`
- `market_context_high->equity_1h` score `-1.7722` n `210` status `ready` deltaP `4.1374` edge `-0.0125` maxDD `-14.716`
- `market_context_high->unknown_4h` score `-1.8626` n `210` status `ready` deltaP `-6.0525` edge `0.0879` maxDD `-7.5546`
- `market_context_high->index_4h` score `-1.9469` n `210` status `ready` deltaP `5.6402` edge `-0.0173` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-2.0257` n `210` status `ready` deltaP `4.5021` edge `0.0086` maxDD `-5.5324`
- `market_context_high->commodity_4h` score `-2.0498` n `210` status `ready` deltaP `-3.5076` edge `-0.0314` maxDD `-2.9494`
- `market_context_high->commodity_24h` score `-2.3587` n `200` status `ready` deltaP `-0.8819` edge `-0.0598` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.5896` n `210` status `ready` deltaP `2.2866` edge `0.0313` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-2.8966` n `210` status `ready` deltaP `3.4481` edge `0.0341` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.7254` n `200` status `ready` deltaP `-2.6111` edge `-0.0118` maxDD `-3.8327`
- `market_context_high->equity_4h` score `-7.2344` n `210` status `ready` deltaP `5.1074` edge `-0.0745` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.0495` n `200` status `ready` deltaP `-13.4861` edge `-0.0633` maxDD `-41.0734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
