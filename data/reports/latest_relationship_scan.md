# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T12:22:26.680515+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10803`

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

- `market_context_high->equity_4h` score `0.7401` n `103` status `ready` deltaP `7.3141` edge `0.151` maxDD `-6.3801`
- `market_context_high->equity_1h` score `0.3017` n `105` status `ready` deltaP `8.7197` edge `0.0485` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.276` n `105` status `ready` deltaP `9.9587` edge `0.0053` maxDD `-0.5622`
- `market_context_high->metal_4h` score `0.2451` n `103` status `ready` deltaP `12.9144` edge `0.0029` maxDD `-1.273`
- `market_context_high->fx_4h` score `0.0466` n `103` status `ready` deltaP `7.4902` edge `0.0063` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.0304` n `105` status `ready` deltaP `4.7348` edge `0.0046` maxDD `-0.4291`
- `market_context_high->commodity_24h` score `-0.1057` n `96` status `ready` deltaP `4.1667` edge `0.142` maxDD `-4.666`
- `market_context_high->fx_1h` score `-0.1944` n `105` status `ready` deltaP `1.075` edge `0.0038` maxDD `-0.2043`
- `market_context_high->index_4h` score `-0.2036` n `103` status `ready` deltaP `5.7572` edge `0.0169` maxDD `-1.5103`
- `market_context_high->unknown_1h` score `-0.3498` n `105` status `ready` deltaP `7.3311` edge `-0.0553` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.4129` n `105` status `ready` deltaP `1.8492` edge `0.0149` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.558` n `105` status `ready` deltaP `2.1357` edge `-0.0013` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7461` n `103` status `ready` deltaP `-2.7631` edge `0.0078` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8024` n `105` status `ready` deltaP `-6.6267` edge `-0.0021` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-0.9109` n `103` status `ready` deltaP `6.207` edge `0.0097` maxDD `-5.4926`
- `market_context_high->unknown_24h` score `-1.1121` n `96` status `ready` deltaP `17.7083` edge `-0.1601` maxDD `-1.0505`
- `market_context_high->crypto_major_4h` score `-1.2093` n `103` status `ready` deltaP `8.1326` edge `-0.0529` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.6325` n `96` status `ready` deltaP `-19.9652` edge `-0.0113` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.693` n `96` status `ready` deltaP `0.0` edge `-0.0567` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.8344` n `96` status `ready` deltaP `-19.9653` edge `-0.1559` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
