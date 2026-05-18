# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T03:22:14.190298+00:00`
- Price records: `672`
- Market context records: `1078`
- Flow alert records: `5009`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8728`

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

- `market_context_high->crypto_major_24h` score `16.3811` n `159` status `ready` deltaP `35.1211` edge `1.1773` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.7445` n `159` status `ready` deltaP `12.0615` edge `0.5217` maxDD `-9.5387`
- `market_context_high->equity_24h` score `5.4442` n `159` status `ready` deltaP `14.6473` edge `0.4057` maxDD `-3.6396`
- `market_context_high->metal_24h` score `4.5423` n `159` status `ready` deltaP `-2.5285` edge `0.5621` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.4971` n `159` status `ready` deltaP `14.7687` edge `0.3071` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.5222` n `161` status `ready` deltaP `8.8622` edge `0.1466` maxDD `-3.6396`
- `market_context_high->crypto_major_4h` score `1.4191` n `161` status `ready` deltaP `13.2697` edge `0.1984` maxDD `-6.4882`
- `market_context_high->index_4h` score `0.8378` n `161` status `ready` deltaP `7.2925` edge `0.0895` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5826` n `170` status `ready` deltaP `7.8214` edge `0.0281` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.506` n `170` status `ready` deltaP `2.9447` edge `0.0603` maxDD `-1.3546`
- `market_context_high->crypto_major_1h` score `0.2348` n `170` status `ready` deltaP `7.316` edge `0.0407` maxDD `-3.5923`
- `market_context_high->fx_1h` score `-0.0211` n `170` status `ready` deltaP `6.4072` edge `0.0011` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.1651` n `170` status `ready` deltaP `6.9426` edge `0.001` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.203` n `170` status `ready` deltaP `3.2635` edge `0.0456` maxDD `-3.4088`
- `market_context_high->crypto_alt_4h` score `-0.3932` n `161` status `ready` deltaP `7.2404` edge `0.1694` maxDD `-13.0347`
- `market_context_high->fx_4h` score `-0.6992` n `161` status `ready` deltaP `1.3047` edge `0.0013` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-1.0589` n `170` status `ready` deltaP `-1.4336` edge `0.0021` maxDD `-3.7959`
- `market_context_high->unknown_4h` score `-1.6774` n `161` status `ready` deltaP `9.0403` edge `-0.0784` maxDD `-6.7322`
- `market_context_high->metal_4h` score `-1.9887` n `161` status `ready` deltaP `4.3715` edge `-0.0887` maxDD `-9.2991`
- `market_context_high->fx_24h` score `-3.1025` n `159` status `ready` deltaP `4.7824` edge `-0.022` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
