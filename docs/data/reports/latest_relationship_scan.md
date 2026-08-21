# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-21T05:37:34.196718+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13819`

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

- `market_context_high->index_1h` score `0.3083` n `105` status `ready` deltaP `10.2581` edge `0.006` maxDD `-0.5622`
- `market_context_high->equity_1h` score `0.2993` n `105` status `ready` deltaP `8.2706` edge `0.0513` maxDD `-3.1861`
- `market_context_high->fx_4h` score `0.0834` n `105` status `ready` deltaP `7.9428` edge `0.008` maxDD `-0.3539`
- `market_context_high->equity_4h` score `0.0229` n `105` status `ready` deltaP `4.2828` edge `0.1363` maxDD `-8.3685`
- `market_context_high->commodity_24h` score `-0.1675` n `96` status `ready` deltaP `4.6875` edge `0.1306` maxDD `-4.666`
- `market_context_high->fx_1h` score `-0.2146` n `105` status `ready` deltaP `0.6259` edge `0.0042` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2484` n `105` status `ready` deltaP `6.5302` edge `-0.0178` maxDD `-1.273`
- `market_context_high->metal_1h` score `-0.2904` n `105` status `ready` deltaP `2.4893` edge `-0.0021` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.3058` n `105` status `ready` deltaP `5.4283` edge `0.017` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.4146` n `105` status `ready` deltaP `7.6305` edge `-0.0627` maxDD `-0.4843`
- `market_context_high->commodity_4h` score `-0.6686` n `105` status `ready` deltaP `-1.7378` edge `0.0109` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.7456` n `105` status `ready` deltaP `-1.1448` edge `-0.0078` maxDD `-2.413`
- `market_context_high->commodity_1h` score `-0.7487` n `105` status `ready` deltaP `-5.7285` edge `-0.0012` maxDD `-1.1941`
- `market_context_high->crypto_major_1h` score `-0.8791` n `105` status `ready` deltaP `-0.2595` edge `-0.0265` maxDD `-2.7581`
- `market_context_high->crypto_alt_4h` score `-2.4309` n `105` status `ready` deltaP `1.2326` edge `-0.0838` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-2.856` n `105` status `ready` deltaP `3.329` edge `-0.1581` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.5716` n `96` status `ready` deltaP `-18.2291` edge `-0.0178` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.5858` n `96` status `ready` deltaP `1.0416` edge `-0.0499` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.9588` n `96` status `ready` deltaP `-21.0069` edge `-0.1649` maxDD `-11.4635`
- `market_context_high->unknown_24h` score `-5.3948` n `96` status `ready` deltaP `11.9791` edge `-0.4788` maxDD `-1.0505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
