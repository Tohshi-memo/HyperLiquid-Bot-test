# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T14:07:27.484473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0293` n `12`; crypto_alt avg `-0.0494` n `230`; crypto_major avg `0.0137` n `8`; equity avg `0.5327` n `109`; fx avg `0.0057` n `6`; index avg `0.0475` n `25`; metal avg `0.0576` n `20`; unknown avg `0.0461` n `781`
- 1h: commodity avg `-0.1737` n `12`; crypto_alt avg `0.5022` n `230`; crypto_major avg `0.3945` n `8`; equity avg `1.5149` n `109`; fx avg `0.0063` n `6`; index avg `0.1747` n `25`; metal avg `0.0891` n `20`; unknown avg `0.6016` n `781`
- 4h: commodity avg `0.1212` n `12`; crypto_alt avg `0.4416` n `230`; crypto_major avg `-0.0948` n `8`; equity avg `0.703` n `109`; fx avg `0.013` n `6`; index avg `0.0618` n `25`; metal avg `-0.1891` n `20`; unknown avg `0.2724` n `781`
- 24h: commodity avg `0.2523` n `12`; crypto_alt avg `0.2468` n `230`; crypto_major avg `-0.9216` n `8`; equity avg `-1.3578` n `109`; fx avg `0.0288` n `6`; index avg `-0.3737` n `25`; metal avg `0.0743` n `20`; unknown avg `113.3468` n `749`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
