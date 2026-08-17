# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T16:22:31.711234+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0219` n `12`; crypto_alt avg `-0.03` n `230`; crypto_major avg `0.0603` n `8`; equity avg `0.002` n `114`; fx avg `0.001` n `6`; index avg `0.0073` n `25`; metal avg `0.0022` n `20`; unknown avg `-0.0208` n `792`
- 1h: commodity avg `0.0335` n `12`; crypto_alt avg `0.0949` n `230`; crypto_major avg `0.1677` n `8`; equity avg `0.0402` n `114`; fx avg `0.0089` n `6`; index avg `-0.0064` n `25`; metal avg `0.0148` n `20`; unknown avg `-0.0263` n `792`
- 4h: commodity avg `0.1056` n `12`; crypto_alt avg `0.056` n `230`; crypto_major avg `0.3373` n `8`; equity avg `0.6378` n `114`; fx avg `0.0219` n `6`; index avg `0.0811` n `25`; metal avg `0.211` n `20`; unknown avg `0.0388` n `792`
- 24h: commodity avg `-0.0121` n `12`; crypto_alt avg `-0.223` n `230`; crypto_major avg `0.7966` n `8`; equity avg `1.6676` n `114`; fx avg `0.0085` n `6`; index avg `0.2186` n `25`; metal avg `0.3288` n `20`; unknown avg `0.0933` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1632`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
