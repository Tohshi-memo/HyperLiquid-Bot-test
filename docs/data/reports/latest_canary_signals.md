# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T16:07:29.677565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.1703` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0015` n `12`; crypto_alt avg `0.1861` n `229`; crypto_major avg `0.32` n `8`; equity avg `0.0696` n `88`; fx avg `0.0024` n `6`; index avg `0.0182` n `25`; metal avg `-0.0523` n `20`; unknown avg `-0.019` n `765`
- 1h: commodity avg `0.0652` n `12`; crypto_alt avg `1.2256` n `229`; crypto_major avg `1.22` n `8`; equity avg `0.1497` n `88`; fx avg `0.0103` n `6`; index avg `0.0417` n `25`; metal avg `-0.0759` n `20`; unknown avg `0.7914` n `765`
- 4h: commodity avg `0.0338` n `12`; crypto_alt avg `2.8966` n `229`; crypto_major avg `1.9589` n `8`; equity avg `0.8166` n `88`; fx avg `0.0423` n `6`; index avg `0.1188` n `25`; metal avg `-0.2114` n `20`; unknown avg `0.8675` n `765`
- 24h: commodity avg `-0.0047` n `12`; crypto_alt avg `1.0936` n `229`; crypto_major avg `0.4566` n `8`; equity avg `-0.01` n `88`; fx avg `0.2048` n `6`; index avg `0.0964` n `25`; metal avg `-0.3743` n `20`; unknown avg `0.4827` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
