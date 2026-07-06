# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T21:22:25.469549+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `0.5508` n `229`; crypto_major avg `0.7462` n `8`; equity avg `-0.0097` n `91`; fx avg `-0.0013` n `6`; index avg `0.0025` n `25`; metal avg `0.0218` n `20`; unknown avg `1.2548` n `763`
- 1h: commodity avg `0.0019` n `12`; crypto_alt avg `0.7022` n `229`; crypto_major avg `1.0235` n `8`; equity avg `0.0093` n `91`; fx avg `-0.0059` n `6`; index avg `0.0182` n `25`; metal avg `0.0462` n `20`; unknown avg `1.3623` n `763`
- 4h: commodity avg `0.1646` n `12`; crypto_alt avg `0.5432` n `229`; crypto_major avg `0.7084` n `8`; equity avg `-0.3143` n `91`; fx avg `-0.0172` n `6`; index avg `0.007` n `25`; metal avg `0.1428` n `20`; unknown avg `0.6261` n `763`
- 24h: commodity avg `0.0421` n `12`; crypto_alt avg `1.1796` n `229`; crypto_major avg `1.106` n `8`; equity avg `-0.6378` n `90`; fx avg `0.1811` n `6`; index avg `0.0498` n `25`; metal avg `-0.1771` n `20`; unknown avg `0.1512` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
