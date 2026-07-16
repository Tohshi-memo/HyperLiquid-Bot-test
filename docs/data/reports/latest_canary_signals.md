# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T01:37:25.803961+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0243` n `12`; crypto_alt avg `0.2429` n `230`; crypto_major avg `0.2747` n `8`; equity avg `0.0672` n `94`; fx avg `-0.0078` n `6`; index avg `0.0191` n `25`; metal avg `0.0223` n `20`; unknown avg `0.1421` n `768`
- 1h: commodity avg `-0.0244` n `12`; crypto_alt avg `-0.027` n `230`; crypto_major avg `0.0651` n `8`; equity avg `-0.2421` n `94`; fx avg `0.0039` n `6`; index avg `-0.087` n `25`; metal avg `-0.1635` n `20`; unknown avg `-0.0715` n `768`
- 4h: commodity avg `-0.0985` n `12`; crypto_alt avg `-0.1677` n `230`; crypto_major avg `-0.2891` n `8`; equity avg `-0.6214` n `94`; fx avg `-0.0086` n `6`; index avg `-0.178` n `25`; metal avg `-0.1884` n `20`; unknown avg `0.1082` n `766`
- 24h: commodity avg `-0.0285` n `12`; crypto_alt avg `-0.0792` n `230`; crypto_major avg `0.3636` n `8`; equity avg `-1.6179` n `93`; fx avg `0.1756` n `6`; index avg `-0.4151` n `25`; metal avg `-0.049` n `20`; unknown avg `0.0238` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
