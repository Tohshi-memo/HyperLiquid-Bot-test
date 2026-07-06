# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T10:52:28.212482+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0171` n `12`; crypto_alt avg `0.0253` n `229`; crypto_major avg `-0.0284` n `8`; equity avg `-0.1141` n `88`; fx avg `-0.0042` n `6`; index avg `-0.0145` n `25`; metal avg `-0.0081` n `20`; unknown avg `-0.0182` n `765`
- 1h: commodity avg `-0.0598` n `12`; crypto_alt avg `0.5203` n `229`; crypto_major avg `0.5045` n `8`; equity avg `-0.0245` n `88`; fx avg `-0.002` n `6`; index avg `-0.0032` n `25`; metal avg `0.1459` n `20`; unknown avg `0.1138` n `765`
- 4h: commodity avg `-0.1517` n `12`; crypto_alt avg `0.3683` n `229`; crypto_major avg `0.003` n `8`; equity avg `-0.085` n `88`; fx avg `-0.0166` n `6`; index avg `0.0062` n `25`; metal avg `0.2051` n `20`; unknown avg `0.0838` n `765`
- 24h: commodity avg `-0.2063` n `12`; crypto_alt avg `0.4643` n `229`; crypto_major avg `0.8735` n `8`; equity avg `-0.7126` n `88`; fx avg `0.0746` n `6`; index avg `-0.0078` n `25`; metal avg `-0.1403` n `20`; unknown avg `1.0499` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
