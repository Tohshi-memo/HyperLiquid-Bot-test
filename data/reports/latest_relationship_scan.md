# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T23:22:36.245067+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `55.9024` n `50` status `ready` deltaP `16.9844` edge `4.5453` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.4471` n `50` status `ready` deltaP `46.6066` edge `2.604` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `8.7965` n `71` status `ready` deltaP `17.7387` edge `0.6458` maxDD `-1.4812`
- `news_risk_high->crypto_major_24h` score `8.7459` n `50` status `ready` deltaP `26.2877` edge `0.6029` maxDD `-2.6128`
- `news_risk_high->equity_24h` score `6.5599` n `50` status `ready` deltaP `30.1005` edge `0.4388` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `5.2111` n `120` status `ready` deltaP `10.3177` edge `0.4387` maxDD `-3.1917`
- `news_risk_high->metal_24h` score `4.4454` n `50` status `ready` deltaP `43.4073` edge `0.0853` maxDD `-0.0053`
- `news_risk_high->unknown_1h` score `3.497` n `71` status `ready` deltaP `8.9567` edge `0.2674` maxDD `-0.8558`
- `market_context_high->metal_24h` score `3.2626` n `120` status `ready` deltaP `28.7406` edge `0.1822` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.425` n `50` status `ready` deltaP `26.9948` edge `0.0372` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2391` n `120` status `ready` deltaP `17.3984` edge `0.1113` maxDD `-0.5894`
- `news_risk_high->fx_4h` score `2.1554` n `71` status `ready` deltaP `31.849` edge `0.0222` maxDD `-0.3931`
- `market_context_high->unknown_1h` score `0.9096` n `120` status `ready` deltaP `8.7924` edge `0.0622` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.583` n `71` status `ready` deltaP `12.2101` edge `0.0059` maxDD `-0.0975`
- `news_risk_high->commodity_1h` score `0.3844` n `71` status `ready` deltaP `11.6113` edge `0.0039` maxDD `-0.5618`
- `market_context_high->metal_4h` score `0.061` n `120` status `ready` deltaP `12.8455` edge `0.0139` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.4036` n `120` status `ready` deltaP `3.3134` edge `-0.0006` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.4437` n `71` status `ready` deltaP `-0.5819` edge `-0.0096` maxDD `-0.8054`
- `news_risk_high->metal_1h` score `-0.7009` n `71` status `ready` deltaP `-0.8539` edge `-0.0266` maxDD `-2.605`
- `news_risk_high->index_4h` score `-0.7124` n `71` status `ready` deltaP `-1.0456` edge `-0.0202` maxDD `-1.7996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
