# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T08:37:29.675349+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5903`

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

- `market_context_high->crypto_alt_24h` score `12.7227` n `40` status `ready` deltaP `51.4583` edge `0.7569` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.9446` n `40` status `ready` deltaP `51.3194` edge `0.5827` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `1.3315` n `32` status `ready` deltaP `-8.0793` edge `0.2391` maxDD `-3.2755`
- `news_risk_high->commodity_1h` score `0.7992` n `32` status `ready` deltaP `17.2717` edge `0.0085` maxDD `-0.6947`
- `news_risk_high->fx_24h` score `0.7647` n `32` status `ready` deltaP `11.2847` edge `0.0579` maxDD `-1.5526`
- `news_risk_high->commodity_4h` score `0.5451` n `32` status `ready` deltaP `15.0152` edge `-0.0046` maxDD `-1.6728`
- `market_context_high->commodity_1h` score `0.3097` n `47` status `ready` deltaP `6.9658` edge `0.0307` maxDD `-1.3282`
- `news_risk_high->crypto_alt_1h` score `0.2908` n `32` status `ready` deltaP `13.6976` edge `0.01` maxDD `-3.1233`
- `market_context_high->commodity_4h` score `0.2689` n `47` status `ready` deltaP `4.5764` edge `0.0886` maxDD `-2.7703`
- `news_risk_high->index_4h` score `0.1487` n `32` status `ready` deltaP `-1.372` edge `0.0596` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.1015` n `32` status `ready` deltaP `4.8018` edge `0.0357` maxDD `-0.3761`
- `news_risk_high->index_1h` score `0.088` n `32` status `ready` deltaP `4.9027` edge `-0.0016` maxDD `-0.5845`
- `market_context_high->fx_1h` score `0.0071` n `47` status `ready` deltaP `7.2652` edge `-0.0086` maxDD `-0.7804`
- `market_context_high->fx_4h` score `-0.0353` n `47` status `ready` deltaP `13.113` edge `-0.0047` maxDD `-1.8531`
- `market_context_high->crypto_alt_4h` score `-0.2314` n `47` status `ready` deltaP `2.1439` edge `0.0466` maxDD `-4.9116`
- `news_risk_high->metal_1h` score `-0.3316` n `32` status `ready` deltaP `-1.1976` edge `-0.0026` maxDD `-0.5538`
- `news_risk_high->fx_1h` score `-0.4369` n `32` status `ready` deltaP `-1.1789` edge `0.0026` maxDD `-0.1588`
- `news_risk_high->crypto_major_1h` score `-0.5501` n `32` status `ready` deltaP `5.2208` edge `-0.0333` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.6815` n `40` status `ready` deltaP `0.6597` edge `0.0368` maxDD `-2.506`
- `news_risk_high->equity_1h` score `-0.8808` n `32` status `ready` deltaP `-8.4955` edge `0.026` maxDD `-2.916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
