# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T01:22:17.522722+00:00`
- Price records: `672`
- Market context records: `1995`
- Flow alert records: `7633`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7585`

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

- `market_context_high->crypto_major_4h` score `8.4011` n `224` status `ready` deltaP `29.4425` edge `0.5568` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `7.879` n `224` status `ready` deltaP `23.8131` edge `0.6123` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `4.5516` n `224` status `ready` deltaP `16.5287` edge `0.37` maxDD `-4.738`
- `market_context_high->equity_4h` score `2.4515` n `224` status `ready` deltaP `14.9608` edge `0.214` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.324` n `189` status `ready` deltaP `15.9917` edge `0.6191` maxDD `-35.8966`
- `market_context_high->metal_24h` score `1.7467` n `189` status `ready` deltaP `16.9285` edge `0.2753` maxDD `-12.7414`
- `market_context_high->equity_24h` score `1.2132` n `189` status `ready` deltaP `14.8719` edge `0.4918` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `1.1355` n `224` status `ready` deltaP `10.1155` edge `0.1258` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.9148` n `224` status `ready` deltaP `8.4608` edge `0.1312` maxDD `-4.9097`
- `market_context_high->index_4h` score `0.7001` n `224` status `ready` deltaP `8.5583` edge `0.0757` maxDD `-2.2861`
- `market_context_high->crypto_major_24h` score `0.5889` n `189` status `ready` deltaP `20.2282` edge `0.7728` maxDD `-62.3533`
- `market_context_high->fx_24h` score `0.5594` n `189` status `ready` deltaP `14.514` edge `0.0273` maxDD `-1.1952`
- `market_context_high->index_24h` score `0.2037` n `189` status `ready` deltaP `3.1819` edge `0.1186` maxDD `-4.1604`
- `market_context_high->equity_1h` score `-0.1747` n `224` status `ready` deltaP `4.1061` edge `0.0369` maxDD `-2.6402`
- `market_context_high->fx_1h` score `-0.595` n `224` status `ready` deltaP `-1.9434` edge `-0.0001` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7378` n `224` status `ready` deltaP `-0.7966` edge `0.007` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.9852` n `224` status `ready` deltaP `1.3313` edge `-0.0016` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.0154` n `224` status `ready` deltaP `1.7617` edge `-0.0244` maxDD `-3.0902`
- `market_context_high->fx_4h` score `-1.1622` n `224` status `ready` deltaP `-8.6345` edge `-0.0033` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.9007` n `224` status `ready` deltaP `1.7884` edge `0.0002` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
