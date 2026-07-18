# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T00:37:28.124653+00:00`
- Price records: `672`
- Market context records: `7085`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11502`

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

- `market_context_high->fx_4h` score `0.7448` n `169` status `ready` deltaP `17.7704` edge `0.0136` maxDD `-0.9333`
- `market_context_high->unknown_1h` score `-0.0762` n `169` status `ready` deltaP `0.4668` edge `0.0464` maxDD `-1.4688`
- `market_context_high->fx_1h` score `-0.1282` n `169` status `ready` deltaP `4.7444` edge `0.0028` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.4053` n `169` status `ready` deltaP `0.7166` edge `0.0297` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.4447` n `169` status `ready` deltaP `1.4004` edge `-0.0044` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.6371` n `169` status `ready` deltaP `2.948` edge `0.0339` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8931` n `169` status `ready` deltaP `-4.9153` edge `-0.0201` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-1.4273` n `169` status `ready` deltaP `-5.6931` edge `-0.0042` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.5565` n `169` status `ready` deltaP `-7.3983` edge `-0.0467` maxDD `-2.9494`
- `market_context_high->equity_1h` score `-1.9755` n `169` status `ready` deltaP `3.4679` edge `-0.0341` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.1531` n `169` status `ready` deltaP `4.4658` edge `-0.0359` maxDD `-12.2591`
- `market_context_high->unknown_4h` score `-2.3372` n `169` status `ready` deltaP `-7.8339` edge `0.0209` maxDD `-4.742`
- `market_context_high->commodity_24h` score `-2.6376` n `169` status `ready` deltaP `-4.0084` edge `-0.0622` maxDD `-4.4704`
- `market_context_high->crypto_major_4h` score `-3.0147` n `169` status `ready` deltaP `3.7117` edge `0.0172` maxDD `-24.6094`
- `market_context_high->crypto_alt_4h` score `-3.0892` n `169` status `ready` deltaP `-0.9318` edge `-0.0113` maxDD `-22.2831`
- `market_context_high->metal_4h` score `-3.8764` n `169` status `ready` deltaP `-2.7313` edge `-0.0065` maxDD `-5.5324`
- `market_context_high->fx_24h` score `-3.9109` n `169` status `ready` deltaP `-4.1543` edge `-0.0155` maxDD `-3.9503`
- `market_context_high->unknown_24h` score `-5.4146` n `169` status `ready` deltaP `-20.7902` edge `-0.0409` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-8.1155` n `169` status `ready` deltaP `3.0136` edge `-0.1735` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.4048` n `169` status `ready` deltaP `-23.455` edge `-0.1182` maxDD `-44.067`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
