# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T12:07:33.180359+00:00`
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

- `market_context_high->equity_4h` score `0.6859` n `103` status `ready` deltaP `7.1617` edge `0.1475` maxDD `-6.3801`
- `market_context_high->equity_1h` score `0.2861` n `105` status `ready` deltaP `8.7197` edge `0.0472` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.2616` n `105` status `ready` deltaP `9.809` edge `0.0051` maxDD `-0.5622`
- `market_context_high->metal_4h` score `0.2435` n `103` status `ready` deltaP `12.9144` edge `0.0027` maxDD `-1.273`
- `market_context_high->fx_4h` score `0.0553` n `103` status `ready` deltaP `7.6426` edge `0.0064` maxDD `-0.3539`
- `market_context_high->metal_1h` score `-0.046` n `105` status `ready` deltaP `4.5851` edge `0.0043` maxDD `-0.4291`
- `market_context_high->commodity_24h` score `-0.0912` n `96` status `ready` deltaP `4.3403` edge `0.1427` maxDD `-4.666`
- `market_context_high->fx_1h` score `-0.1866` n `105` status `ready` deltaP `1.2247` edge `0.0038` maxDD `-0.2043`
- `market_context_high->index_4h` score `-0.2169` n `103` status `ready` deltaP `5.6048` edge `0.0162` maxDD `-1.5103`
- `market_context_high->unknown_1h` score `-0.3498` n `105` status `ready` deltaP `7.3311` edge `-0.0553` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.4144` n `105` status `ready` deltaP `1.8492` edge `0.0147` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.5712` n `105` status `ready` deltaP `1.986` edge `-0.002` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7445` n `103` status `ready` deltaP `-2.7631` edge `0.008` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7938` n `105` status `ready` deltaP `-6.477` edge `-0.002` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-0.8989` n `103` status `ready` deltaP `6.207` edge `0.0107` maxDD `-5.4926`
- `market_context_high->unknown_24h` score `-1.0773` n `96` status `ready` deltaP `17.7083` edge `-0.1572` maxDD `-1.0505`
- `market_context_high->crypto_major_4h` score `-1.1997` n `103` status `ready` deltaP `8.1326` edge `-0.0521` maxDD `-3.1677`
- `market_context_high->fx_24h` score `-3.6138` n `96` status `ready` deltaP `-19.7916` edge `-0.0109` maxDD `-1.9981`
- `market_context_high->index_24h` score `-3.7091` n `96` status `ready` deltaP `-0.1736` edge `-0.0576` maxDD `-18.3411`
- `market_context_high->metal_24h` score `-4.8152` n `96` status `ready` deltaP `-19.7917` edge `-0.1546` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
