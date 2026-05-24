# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T09:07:15.724123+00:00`
- Price records: `672`
- Market context records: `1720`
- Flow alert records: `6859`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->metal_24h` score `6.59` n `141` status `ready` deltaP `25.3148` edge `0.623` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `6.2008` n `141` status `ready` deltaP `17.0962` edge `0.9348` maxDD `-35.8966`
- `market_context_high->crypto_alt_4h` score `6.0345` n `196` status `ready` deltaP `21.7335` edge `0.5346` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.503` n `196` status `ready` deltaP `23.1769` edge `0.4613` maxDD `-10.9117`
- `market_context_high->index_24h` score `3.8534` n `141` status `ready` deltaP `16.9587` edge `0.3309` maxDD `-4.1604`
- `market_context_high->unknown_4h` score `3.0643` n `196` status `ready` deltaP `13.9466` edge `0.3895` maxDD `-11.1695`
- `market_context_high->equity_4h` score `3.0057` n `196` status `ready` deltaP `16.2643` edge `0.2515` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.4554` n `141` status `ready` deltaP `15.6789` edge `0.5066` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7285` n `196` status `ready` deltaP `7.4209` edge `0.1136` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.53` n `196` status `ready` deltaP `8.6642` edge `0.0953` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.1813` n `196` status `ready` deltaP `4.7477` edge `0.0908` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0179` n `196` status `ready` deltaP `4.6713` edge `0.0512` maxDD `-2.8014`
- `market_context_high->crypto_alt_24h` score `-0.0537` n `141` status `ready` deltaP `23.03` edge `1.0229` maxDD `-88.8062`
- `market_context_high->metal_4h` score `-0.3203` n `196` status `ready` deltaP `12.1391` edge `0.1472` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.4503` n `196` status `ready` deltaP `1.2221` edge `0.0175` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.5533` n `196` status `ready` deltaP `5.4962` edge `0.026` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6638` n `196` status `ready` deltaP `-3.1162` edge `-0.0011` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.8039` n `141` status `ready` deltaP `4.6222` edge `0.0071` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `-0.9591` n `141` status `ready` deltaP `21.3183` edge `0.5935` maxDD `-62.3533`
- `market_context_high->unknown_1h` score `-1.5588` n `196` status `ready` deltaP `1.387` edge `0.0078` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
