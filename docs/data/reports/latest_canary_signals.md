# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T05:22:32.473885+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0143` n `12`; crypto_alt avg `0.0029` n `230`; crypto_major avg `-0.0115` n `8`; equity avg `-0.0624` n `114`; fx avg `-0.0251` n `6`; index avg `-0.0162` n `25`; metal avg `0.0164` n `20`; unknown avg `-0.0986` n `793`
- 1h: commodity avg `0.0307` n `12`; crypto_alt avg `0.1739` n `230`; crypto_major avg `0.1488` n `8`; equity avg `-0.0657` n `114`; fx avg `-0.0172` n `6`; index avg `-0.0248` n `25`; metal avg `0.0308` n `20`; unknown avg `-0.1631` n `793`
- 4h: commodity avg `0.0948` n `12`; crypto_alt avg `-0.8629` n `230`; crypto_major avg `-0.2931` n `8`; equity avg `-1.6247` n `114`; fx avg `-0.0021` n `6`; index avg `-0.2882` n `25`; metal avg `-0.2548` n `20`; unknown avg `0.1045` n `793`
- 24h: commodity avg `0.7226` n `12`; crypto_alt avg `-1.389` n `230`; crypto_major avg `-0.0181` n `8`; equity avg `-1.219` n `114`; fx avg `-0.0249` n `6`; index avg `-0.3239` n `25`; metal avg `-0.2009` n `20`; unknown avg `0.039` n `776`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1877`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
