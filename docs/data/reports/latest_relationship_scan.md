# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T10:52:24.043089+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11776`

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

- `news_risk_high->unknown_24h` score `49.4328` n `56` status `ready` deltaP `13.9385` edge `4.081` maxDD `-2.3617`
- `news_risk_high->crypto_alt_24h` score `24.1552` n `56` status `ready` deltaP `36.2351` edge `1.992` maxDD `-14.9839`
- `market_context_high->unknown_24h` score `8.3949` n `111` status `ready` deltaP `17.4456` edge `0.6565` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.2855` n `80` status `ready` deltaP `10.9756` edge `0.5096` maxDD `-1.7183`
- `market_context_high->metal_24h` score `3.9419` n `111` status `ready` deltaP `30.7667` edge `0.2253` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `2.8587` n `111` status `ready` deltaP `18.8585` edge `0.1532` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.6859` n `80` status `ready` deltaP `5.6737` edge `0.2217` maxDD `-0.8558`
- `news_risk_high->equity_24h` score `2.5467` n `56` status `ready` deltaP `22.9167` edge `0.3629` maxDD `-12.4677`
- `news_risk_high->fx_4h` score `2.3937` n `80` status `ready` deltaP `34.8171` edge `0.0223` maxDD `-0.3953`
- `news_risk_high->crypto_major_24h` score `2.0287` n `56` status `ready` deltaP `19.2708` edge `0.3715` maxDD `-16.524`
- `news_risk_high->metal_24h` score `1.6456` n `56` status `ready` deltaP `36.2847` edge `0.0405` maxDD `-3.7137`
- `news_risk_high->index_24h` score `1.3391` n `56` status `ready` deltaP `19.1964` edge `0.0256` maxDD `-1.0255`
- `market_context_high->unknown_1h` score `1.0731` n `119` status `ready` deltaP `8.7619` edge `0.0802` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.7244` n `80` status `ready` deltaP `14.0419` edge `0.0056` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4338` n `80` status `ready` deltaP `12.3503` edge `0.0053` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.274` n `111` status `ready` deltaP `7.2292` edge `0.0084` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.3988` n `80` status `ready` deltaP `0.1572` edge `-0.0085` maxDD `-0.8275`
- `market_context_high->crypto_major_4h` score `-0.4751` n `111` status `ready` deltaP `14.7125` edge `0.2074` maxDD `-20.9394`
- `news_risk_high->index_4h` score `-0.5285` n `80` status `ready` deltaP `1.9207` edge `-0.0164` maxDD `-1.7996`
- `market_context_high->crypto_alt_4h` score `-0.5667` n `111` status `ready` deltaP `17.2902` edge `0.2967` maxDD `-31.4361`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
