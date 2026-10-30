# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T23:52:27.072154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0208` n `13`; crypto_alt avg `0.0762` n `238`; crypto_major avg `0.0382` n `8`; equity avg `-0.0363` n `156`; fx avg `0.0042` n `6`; index avg `-0.0003` n `27`; metal avg `0.005` n `20`; unknown avg `0.0601` n `1262`
- 1h: commodity avg `-0.0086` n `13`; crypto_alt avg `0.4978` n `238`; crypto_major avg `0.413` n `8`; equity avg `0.1313` n `156`; fx avg `0.0131` n `6`; index avg `0.0082` n `27`; metal avg `-0.0009` n `20`; unknown avg `0.2813` n `1255`
- 4h: commodity avg `-0.1275` n `13`; crypto_alt avg `1.3265` n `238`; crypto_major avg `0.4312` n `8`; equity avg `0.2368` n `156`; fx avg `-0.0335` n `6`; index avg `0.027` n `27`; metal avg `0.0045` n `20`; unknown avg `0.7149` n `1149`
- 24h: commodity avg `0.0884` n `13`; crypto_alt avg `2.7319` n `238`; crypto_major avg `0.4299` n `8`; equity avg `-2.5051` n `156`; fx avg `-0.1372` n `6`; index avg `-0.2533` n `27`; metal avg `-0.8745` n `20`; unknown avg `-0.4312` n `1014`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
