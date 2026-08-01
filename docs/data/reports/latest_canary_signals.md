# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T07:37:28.501420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0003` n `12`; crypto_alt avg `-0.119` n `230`; crypto_major avg `-0.1128` n `8`; equity avg `-0.005` n `102`; fx avg `0.0058` n `6`; index avg `0.0134` n `25`; metal avg `0.0416` n `20`; unknown avg `0.0126` n `781`
- 1h: commodity avg `-0.0041` n `12`; crypto_alt avg `-0.1928` n `230`; crypto_major avg `-0.1531` n `8`; equity avg `-0.0929` n `102`; fx avg `-0.0039` n `6`; index avg `-0.0024` n `25`; metal avg `0.0591` n `20`; unknown avg `-0.0345` n `781`
- 4h: commodity avg `-0.0993` n `12`; crypto_alt avg `-0.0983` n `230`; crypto_major avg `-0.1382` n `8`; equity avg `-0.0324` n `102`; fx avg `0.0208` n `6`; index avg `-0.0104` n `25`; metal avg `0.0478` n `20`; unknown avg `-0.052` n `765`
- 24h: commodity avg `0.7664` n `12`; crypto_alt avg `0.17` n `230`; crypto_major avg `-1.2862` n `8`; equity avg `-2.3209` n `102`; fx avg `-0.065` n `6`; index avg `-0.3119` n `25`; metal avg `-0.1019` n `20`; unknown avg `4.8863` n `763`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
