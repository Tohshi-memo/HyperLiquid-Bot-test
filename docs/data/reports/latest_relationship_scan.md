# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T06:22:25.880759+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5900`

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

- `news_risk_high->unknown_24h` score `5188.6811` n `60` status `ready` deltaP `32.5014` edge `432.2155` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.5943` n `50` status `ready` deltaP `60.8042` edge `1.1839` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `4.4937` n `68` status `ready` deltaP `16.2213` edge `0.3427` maxDD `-3.4427`
- `market_context_high->commodity_24h` score `4.1327` n `50` status `ready` deltaP `31.8995` edge `0.2849` maxDD `-8.5873`
- `news_risk_high->index_4h` score `1.589` n `68` status `ready` deltaP `15.6115` edge `0.0664` maxDD `-0.3783`
- `market_context_high->fx_4h` score `0.7978` n `50` status `ready` deltaP `18.8232` edge `0.0206` maxDD `-1.3685`
- `news_risk_high->equity_1h` score `0.6492` n `68` status `ready` deltaP `9.9419` edge `0.0701` maxDD `-2.916`
- `market_context_high->crypto_alt_4h` score `0.4813` n `50` status `ready` deltaP `7.2012` edge `0.1094` maxDD `-5.323`
- `market_context_high->commodity_4h` score `0.1893` n `50` status `ready` deltaP `6.5549` edge `0.0652` maxDD `-2.7703`
- `news_risk_high->fx_4h` score `0.1248` n `68` status `ready` deltaP `12.2938` edge `0.0242` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.0977` n `68` status `ready` deltaP `5.165` edge `0.0257` maxDD `-0.8085`
- `market_context_high->fx_24h` score `0.0949` n `50` status `ready` deltaP `9.5633` edge `0.0464` maxDD `-2.506`
- `news_risk_high->crypto_alt_1h` score `0.0554` n `68` status `ready` deltaP `6.0321` edge `0.0351` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.0427` n `68` status `ready` deltaP `3.267` edge `0.005` maxDD `-0.2475`
- `market_context_high->fx_1h` score `-0.0789` n `50` status `ready` deltaP `5.7964` edge `0.0015` maxDD `-0.6874`
- `news_risk_high->index_1h` score `-0.0863` n `68` status `ready` deltaP `2.1663` edge `0.0068` maxDD `-0.5845`
- `news_risk_high->metal_1h` score `-0.1676` n `68` status `ready` deltaP `2.0166` edge `0.0054` maxDD `-0.5599`
- `market_context_high->commodity_1h` score `-0.1835` n `50` status `ready` deltaP `1.7964` edge `0.0186` maxDD `-1.3282`
- `news_risk_high->crypto_major_1h` score `-0.2895` n `68` status `ready` deltaP `1.3209` edge `0.0261` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.488` n `50` status `ready` deltaP `-1.8503` edge `0.0125` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
