# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T22:43:04.548796+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `12`; crypto_alt avg `-0.1522` n `228`; crypto_major avg `-0.2274` n `8`; equity avg `0.0481` n `88`; fx avg `0.0035` n `6`; index avg `0.0229` n `23`; metal avg `0.0121` n `20`; unknown avg `-0.1189` n `764`
- 1h: commodity avg `-0.1006` n `12`; crypto_alt avg `-0.3651` n `228`; crypto_major avg `-0.6601` n `8`; equity avg `0.0742` n `88`; fx avg `-0.0078` n `6`; index avg `0.0511` n `23`; metal avg `-0.2007` n `20`; unknown avg `-0.0313` n `764`
- 4h: commodity avg `-0.3142` n `12`; crypto_alt avg `-0.6294` n `228`; crypto_major avg `-0.6887` n `8`; equity avg `0.2477` n `88`; fx avg `-0.0575` n `6`; index avg `0.1226` n `23`; metal avg `-0.1658` n `20`; unknown avg `0.2139` n `764`
- 24h: commodity avg `-0.1375` n `12`; crypto_alt avg `-0.9015` n `228`; crypto_major avg `-1.4896` n `8`; equity avg `0.3304` n `88`; fx avg `-0.0984` n `6`; index avg `0.1405` n `23`; metal avg `-0.1574` n `20`; unknown avg `15.0678` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1899`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1816`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
