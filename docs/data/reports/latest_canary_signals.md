# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T08:52:30.807841+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0139` n `12`; crypto_alt avg `-0.0187` n `229`; crypto_major avg `-0.0224` n `8`; equity avg `-0.033` n `88`; fx avg `-0.0087` n `6`; index avg `0.0062` n `25`; metal avg `-0.0006` n `20`; unknown avg `0.0088` n `765`
- 1h: commodity avg `-0.0147` n `12`; crypto_alt avg `0.0232` n `229`; crypto_major avg `0.1041` n `8`; equity avg `0.0089` n `88`; fx avg `-0.0066` n `6`; index avg `0.0248` n `25`; metal avg `0.0073` n `20`; unknown avg `0.5662` n `765`
- 4h: commodity avg `0.0033` n `12`; crypto_alt avg `-0.507` n `229`; crypto_major avg `-0.4566` n `8`; equity avg `-0.0402` n `88`; fx avg `-0.0206` n `6`; index avg `0.0038` n `25`; metal avg `0.0084` n `20`; unknown avg `0.7053` n `745`
- 24h: commodity avg `-0.0554` n `12`; crypto_alt avg `1.481` n `229`; crypto_major avg `2.5555` n `8`; equity avg `0.3898` n `88`; fx avg `-0.0507` n `6`; index avg `-0.0236` n `25`; metal avg `-0.1565` n `20`; unknown avg `5.8634` n `733`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
