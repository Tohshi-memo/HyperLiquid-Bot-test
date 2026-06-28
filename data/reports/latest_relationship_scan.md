# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T21:36:36.937405+00:00`
- Price records: `672`
- Market context records: `5080`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10338`

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

- `market_context_high->unknown_24h` score `12.1846` n `76` status `ready` deltaP `27.3209` edge `0.8675` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `11.7475` n `104` status `ready` deltaP `2.6486` edge `1.0131` maxDD `-1.8108`
- `market_context_high->unknown_4h` score `9.3745` n `92` status `ready` deltaP `21.1691` edge `0.7423` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `6.937` n `92` status `ready` deltaP `20.2677` edge `0.5649` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `6.2509` n `92` status `ready` deltaP `18.7036` edge `0.5551` maxDD `-8.377`
- `market_context_high->equity_4h` score `2.1098` n `92` status `ready` deltaP `10.2399` edge `0.2207` maxDD `-6.3852`
- `market_context_high->equity_1h` score `1.0862` n `104` status `ready` deltaP `10.0645` edge `0.0766` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.9247` n `104` status `ready` deltaP `7.3123` edge `0.1308` maxDD `-5.1989`
- `market_context_high->metal_1h` score `0.9024` n `104` status `ready` deltaP `12.9088` edge `0.0388` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.8818` n `104` status `ready` deltaP `6.0917` edge `0.1139` maxDD `-3.8153`
- `market_context_high->metal_4h` score `0.7375` n `92` status `ready` deltaP `9.6832` edge `0.1048` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.2999` n `92` status `ready` deltaP `8.3112` edge `0.0457` maxDD `-1.0893`
- `market_context_high->index_1h` score `0.2959` n `104` status `ready` deltaP `5.7692` edge `0.016` maxDD `-0.3843`
- `market_context_high->commodity_4h` score `-0.4094` n `92` status `ready` deltaP `9.4711` edge `0.0111` maxDD `-3.6686`
- `market_context_high->fx_24h` score `-0.6065` n `76` status `ready` deltaP `0.2467` edge `-0.0032` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.6903` n `104` status `ready` deltaP `0.4721` edge `0.0053` maxDD `-1.278`
- `market_context_high->fx_4h` score `-1.1302` n `92` status `ready` deltaP `-6.0446` edge `-0.0042` maxDD `-1.3653`
- `market_context_high->fx_1h` score `-1.7713` n `104` status `ready` deltaP `-11.8782` edge `-0.0051` maxDD `-0.732`
- `market_context_high->commodity_24h` score `-1.9201` n `76` status `ready` deltaP `9.8227` edge `0.0299` maxDD `-17.6575`
- `market_context_high->metal_24h` score `-4.2489` n `76` status `ready` deltaP `-2.8418` edge `0.0197` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
