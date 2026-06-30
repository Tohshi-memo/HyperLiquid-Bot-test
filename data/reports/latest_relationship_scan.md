# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T04:37:26.498970+00:00`
- Price records: `672`
- Market context records: `5215`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5650`

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

- `market_context_high->unknown_24h` score `17.5656` n `109` status `ready` deltaP `33.6567` edge `1.2584` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `14.1824` n `109` status `ready` deltaP `31.6545` edge `1.337` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `9.1549` n `109` status `ready` deltaP `27.1661` edge `0.9205` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `4.4243` n `155` status `ready` deltaP `18.8119` edge `0.3455` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.3365` n `155` status `ready` deltaP `13.694` edge `0.43` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.2522` n `155` status `ready` deltaP `14.0696` edge `0.4898` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.1656` n `155` status `ready` deltaP `8.9878` edge `0.1847` maxDD `-2.7986`
- `market_context_high->crypto_alt_1h` score `0.6284` n `155` status `ready` deltaP `4.9527` edge `0.1155` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5872` n `155` status `ready` deltaP `6.7027` edge `0.1288` maxDD `-6.9639`
- `market_context_high->fx_24h` score `0.5832` n `109` status `ready` deltaP `13.7456` edge `0.0465` maxDD `-0.8294`
- `market_context_high->equity_4h` score `0.2605` n `155` status `ready` deltaP `6.9404` edge `0.1393` maxDD `-7.4425`
- `market_context_high->metal_1h` score `-0.1464` n `155` status `ready` deltaP `3.812` edge `0.015` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.1587` n `155` status `ready` deltaP `5.0705` edge `0.0495` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.2302` n `155` status `ready` deltaP `3.2384` edge `0.0096` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.2604` n `155` status `ready` deltaP `1.809` edge `-0.0002` maxDD `-0.6194`
- `market_context_high->index_24h` score `-0.4934` n `109` status `ready` deltaP `13.4015` edge `0.0109` maxDD `-7.413`
- `market_context_high->fx_4h` score `-0.6089` n `155` status `ready` deltaP `3.034` edge `0.0051` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6133` n `155` status `ready` deltaP `0.4259` edge `-0.0006` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.7614` n `155` status `ready` deltaP `4.2289` edge `0.0201` maxDD `-2.9391`
- `market_context_high->equity_24h` score `-1.2432` n `109` status `ready` deltaP `15.4801` edge `0.3003` maxDD `-40.0306`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
