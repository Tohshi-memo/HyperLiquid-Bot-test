# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T05:37:25.458941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0074` n `12`; crypto_alt avg `-0.2037` n `232`; crypto_major avg `-0.1622` n `8`; equity avg `-0.1117` n `133`; fx avg `0.0204` n `6`; index avg `-0.0084` n `26`; metal avg `-0.0126` n `20`; unknown avg `-0.0883` n `793`
- 1h: commodity avg `-0.0464` n `12`; crypto_alt avg `-0.5406` n `232`; crypto_major avg `-0.4165` n `8`; equity avg `0.0657` n `133`; fx avg `-0.025` n `6`; index avg `0.0351` n `26`; metal avg `-0.0275` n `20`; unknown avg `-0.3686` n `791`
- 4h: commodity avg `-0.0864` n `12`; crypto_alt avg `-0.1474` n `232`; crypto_major avg `0.2295` n `8`; equity avg `0.3597` n `133`; fx avg `-0.0182` n `6`; index avg `0.1034` n `26`; metal avg `-0.0772` n `20`; unknown avg `8.5791` n `791`
- 24h: commodity avg `-0.0042` n `12`; crypto_alt avg `2.3581` n `232`; crypto_major avg `4.2629` n `8`; equity avg `2.2045` n `133`; fx avg `-0.1242` n `6`; index avg `0.422` n `26`; metal avg `0.5153` n `20`; unknown avg `25.1237` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
