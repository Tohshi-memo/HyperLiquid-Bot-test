# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T06:20:59.113058+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13755`

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

- `market_context_high->index_1h` score `0.3215` n `105` status `ready` deltaP `10.4078` edge `0.0061` maxDD `-0.5622`
- `market_context_high->equity_1h` score `0.3137` n `105` status `ready` deltaP `8.4203` edge `0.0515` maxDD `-3.1861`
- `market_context_high->equity_4h` score `0.0689` n `105` status `ready` deltaP `4.5877` edge `0.1381` maxDD `-8.3685`
- `market_context_high->fx_4h` score `0.066` n `105` status `ready` deltaP `7.6379` edge `0.0078` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.1722` n `96` status `ready` deltaP `4.6875` edge `0.13` maxDD `-4.666`
- `market_context_high->fx_1h` score `-0.2146` n `105` status `ready` deltaP `0.6259` edge `0.0042` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2445` n `105` status `ready` deltaP `6.5302` edge `-0.0173` maxDD `-1.273`
- `market_context_high->metal_1h` score `-0.288` n `105` status `ready` deltaP `2.4893` edge `-0.0019` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.3043` n `105` status `ready` deltaP `5.4283` edge `0.0172` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.429` n `105` status `ready` deltaP `7.4808` edge `-0.0629` maxDD `-0.4843`
- `market_context_high->commodity_4h` score `-0.6386` n `105` status `ready` deltaP `-1.2805` edge `0.0117` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7455` n `105` status `ready` deltaP `-5.7285` edge `-0.0008` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-0.7846` n `105` status `ready` deltaP `-1.4442` edge `-0.0108` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.9305` n `105` status `ready` deltaP `-0.7086` edge `-0.0301` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-2.5479` n `105` status `ready` deltaP `0.7753` edge `-0.0905` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.9368` n `105` status `ready` deltaP `3.0241` edge `-0.1628` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.5331` n `96` status `ready` deltaP `-17.8819` edge `-0.0169` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.5843` n `96` status `ready` deltaP `1.0416` edge `-0.0497` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.9666` n `96` status `ready` deltaP `-21.0069` edge `-0.1659` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-5.6129` n `96` status `ready` deltaP `11.4583` edge `-0.4935` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
