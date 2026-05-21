# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T21:22:20.993750+00:00`
- Price records: `672`
- Market context records: `1462`
- Flow alert records: `6118`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_alt_24h` score `12.7864` n `164` status `ready` deltaP `28.8999` edge `1.0745` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `11.9562` n `164` status `ready` deltaP `27.5915` edge `0.9256` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.4638` n `164` status `ready` deltaP `15.1254` edge `1.0212` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.166` n `164` status `ready` deltaP `19.9356` edge `0.3229` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.9846` n `164` status `ready` deltaP `13.1606` edge `0.477` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5192` n `222` status `ready` deltaP `7.1687` edge `0.1618` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2636` n `164` status `ready` deltaP `11.8013` edge `0.0482` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.1087` n `222` status `ready` deltaP `3.4877` edge `0.0142` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1395` n `222` status `ready` deltaP `1.8436` edge `0.0361` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.214` n `222` status `ready` deltaP `11.4631` edge `0.2377` maxDD `-19.5565`
- `market_context_high->index_4h` score `-0.4406` n `222` status `ready` deltaP `1.0767` edge `0.065` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.4827` n `222` status `ready` deltaP `0.6056` edge `-0.0027` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5492` n `222` status `ready` deltaP `1.8153` edge `0.0445` maxDD `-4.1892`
- `market_context_high->fx_4h` score `-1.032` n `222` status `ready` deltaP `-3.9222` edge `-0.0091` maxDD `-1.4313`
- `market_context_high->metal_1h` score `-1.1611` n `222` status `ready` deltaP `5.1182` edge `0.0027` maxDD `-6.3532`
- `market_context_high->crypto_major_4h` score `-1.1799` n `222` status `ready` deltaP `5.0044` edge `0.1392` maxDD `-13.3376`
- `market_context_high->commodity_1h` score `-1.2603` n `222` status `ready` deltaP `-1.6481` edge `-0.0019` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.5914` n `222` status `ready` deltaP `-0.739` edge `0.008` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.8043` n `222` status `ready` deltaP `7.7895` edge `0.0669` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.0215` n `222` status `ready` deltaP `-11.4068` edge `-0.0679` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
