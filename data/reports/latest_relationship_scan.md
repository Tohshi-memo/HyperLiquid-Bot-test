# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T02:52:29.359208+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11618`

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

- `market_context_high->crypto_major_24h` score `2.191` n `91` status `ready` deltaP `6.7308` edge `0.2585` maxDD `-4.9964`
- `market_context_high->equity_1h` score `1.5492` n `96` status `ready` deltaP `12.9055` edge `0.0732` maxDD `-0.4112`
- `market_context_high->equity_4h` score `1.544` n `96` status `ready` deltaP `8.8668` edge `0.1584` maxDD `-2.4411`
- `market_context_high->commodity_24h` score `1.3265` n `91` status `ready` deltaP `15.6441` edge `0.2491` maxDD `-4.666`
- `market_context_high->metal_4h` score `1.1866` n `96` status `ready` deltaP `17.7845` edge `0.0379` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.9633` n `96` status `ready` deltaP `11.3059` edge `0.107` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.8468` n `96` status `ready` deltaP `14.864` edge `0.0102` maxDD `-0.0982`
- `market_context_high->crypto_alt_4h` score `0.4585` n `96` status `ready` deltaP `11.2805` edge `0.09` maxDD `-5.4926`
- `market_context_high->unknown_24h` score `0.3381` n `91` status `ready` deltaP `16.7335` edge `-0.062` maxDD `-0.3771`
- `market_context_high->unknown_1h` score `0.2851` n `96` status `ready` deltaP `8.9072` edge `-0.0129` maxDD `-0.4843`
- `market_context_high->metal_1h` score `0.138` n `96` status `ready` deltaP `5.8196` edge `0.0114` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.0406` n `96` status `ready` deltaP `6.4278` edge `0.0022` maxDD `-0.3539`
- `market_context_high->index_4h` score `-0.0623` n `96` status `ready` deltaP `5.9705` edge `0.0205` maxDD `-0.5728`
- `market_context_high->crypto_alt_1h` score `-0.3169` n `96` status `ready` deltaP `3.4244` edge `0.0167` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.3463` n `96` status `ready` deltaP `-1.6218` edge `0.0023` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.3946` n `96` status `ready` deltaP `2.5324` edge `0.017` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.4683` n `96` status `ready` deltaP `2.4137` edge `0.0089` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8884` n `96` status `ready` deltaP `-7.7408` edge `-0.0057` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-1.533` n `91` status `ready` deltaP `-0.8985` edge `0.0865` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.0391` n `91` status `ready` deltaP `-24.2617` edge `-0.0249` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
