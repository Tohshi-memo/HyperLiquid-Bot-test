# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T07:37:32.726316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `-0.0433` n `230`; crypto_major avg `-0.0164` n `8`; equity avg `-0.0071` n `112`; fx avg `-0.0002` n `6`; index avg `-0.0011` n `25`; metal avg `0.0084` n `20`; unknown avg `0.1902` n `784`
- 1h: commodity avg `0.0045` n `12`; crypto_alt avg `0.0104` n `230`; crypto_major avg `-0.0174` n `8`; equity avg `0.0412` n `112`; fx avg `-0.0072` n `6`; index avg `0.0042` n `25`; metal avg `0.01` n `20`; unknown avg `0.0988` n `784`
- 4h: commodity avg `0.0127` n `12`; crypto_alt avg `0.0678` n `230`; crypto_major avg `0.0607` n `8`; equity avg `-0.0821` n `112`; fx avg `-0.0053` n `6`; index avg `-0.0433` n `25`; metal avg `-0.0051` n `20`; unknown avg `0.0876` n `751`
- 24h: commodity avg `-0.2182` n `12`; crypto_alt avg `-0.0599` n `230`; crypto_major avg `0.6293` n `8`; equity avg `1.1341` n `112`; fx avg `-0.0577` n `6`; index avg `0.0725` n `25`; metal avg `0.0659` n `20`; unknown avg `0.2309` n `750`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
