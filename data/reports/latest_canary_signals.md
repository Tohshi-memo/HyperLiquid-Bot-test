# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T05:22:27.890563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0` n `5`; crypto_alt avg `-0.0666` n `235`; crypto_major avg `-0.0596` n `8`; equity avg `-0.0074` n `41`; fx avg `0.0` n `1`; index avg `0.0` n `17`; metal avg `-0.0008` n `12`; unknown avg `-0.088` n `1087`
- 1h: commodity avg `0.0` n `5`; crypto_alt avg `0.4723` n `235`; crypto_major avg `0.1672` n `8`; equity avg `-0.0021` n `41`; fx avg `0.0` n `1`; index avg `0.0` n `17`; metal avg `-0.0044` n `12`; unknown avg `0.2034` n `1085`
- 4h: commodity avg `0.0` n `5`; crypto_alt avg `-0.3301` n `235`; crypto_major avg `-0.1922` n `8`; equity avg `-0.033` n `41`; fx avg `0.0` n `1`; index avg `0.0` n `17`; metal avg `-0.0024` n `12`; unknown avg `-0.1265` n `1079`
- 24h: commodity avg `0.0` n `5`; crypto_alt avg `0.3449` n `235`; crypto_major avg `-0.0556` n `8`; equity avg `-0.0954` n `41`; fx avg `0.0` n `1`; index avg `0.0` n `17`; metal avg `-0.0008` n `12`; unknown avg `0.431` n `913`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
