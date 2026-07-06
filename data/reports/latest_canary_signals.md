# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T06:57:59.046767+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0201` n `12`; crypto_alt avg `-0.0153` n `229`; crypto_major avg `0.039` n `8`; equity avg `0.0489` n `88`; fx avg `0.0206` n `6`; index avg `0.0124` n `25`; metal avg `-0.0844` n `20`; unknown avg `-0.0424` n `765`
- 1h: commodity avg `0.0743` n `12`; crypto_alt avg `-0.0172` n `229`; crypto_major avg `-0.05` n `8`; equity avg `0.0932` n `88`; fx avg `0.0314` n `6`; index avg `0.0601` n `25`; metal avg `-0.0701` n `20`; unknown avg `-0.0416` n `731`
- 4h: commodity avg `0.2025` n `12`; crypto_alt avg `-0.9205` n `229`; crypto_major avg `-0.7312` n `8`; equity avg `0.7393` n `88`; fx avg `0.0186` n `6`; index avg `0.1853` n `25`; metal avg `-0.2` n `20`; unknown avg `-0.1362` n `731`
- 24h: commodity avg `-0.0354` n `12`; crypto_alt avg `-0.1387` n `229`; crypto_major avg `0.8557` n `8`; equity avg `-0.5891` n `88`; fx avg `0.0895` n `6`; index avg `-0.0219` n `25`; metal avg `-0.3183` n `20`; unknown avg `1.0019` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
