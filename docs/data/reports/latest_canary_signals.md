# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T05:52:28.559183+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `-0.0288` n `230`; crypto_major avg `-0.0118` n `8`; equity avg `-0.1824` n `92`; fx avg `0.0064` n `6`; index avg `-0.0249` n `25`; metal avg `-0.0045` n `20`; unknown avg `-0.1732` n `766`
- 1h: commodity avg `-0.1718` n `12`; crypto_alt avg `0.239` n `230`; crypto_major avg `0.2392` n `8`; equity avg `0.4118` n `92`; fx avg `0.0445` n `6`; index avg `0.108` n `25`; metal avg `0.1411` n `20`; unknown avg `1.7218` n `766`
- 4h: commodity avg `-0.0568` n `12`; crypto_alt avg `0.1466` n `230`; crypto_major avg `0.2938` n `8`; equity avg `0.2882` n `92`; fx avg `-0.0033` n `6`; index avg `0.0794` n `25`; metal avg `0.3623` n `20`; unknown avg `-0.3528` n `766`
- 24h: commodity avg `0.7848` n `12`; crypto_alt avg `-0.4107` n `230`; crypto_major avg `-0.4719` n `8`; equity avg `-0.7043` n `92`; fx avg `-0.1868` n `6`; index avg `-0.0556` n `25`; metal avg `0.2007` n `20`; unknown avg `-0.1624` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1831`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
