# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T02:22:24.310186+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0679` n `13`; crypto_alt avg `0.1846` n `239`; crypto_major avg `0.0779` n `8`; equity avg `0.1939` n `164`; fx avg `-0.0205` n `6`; index avg `0.0195` n `27`; metal avg `0.0314` n `20`; unknown avg `0.8036` n `1263`
- 1h: commodity avg `-0.0054` n `13`; crypto_alt avg `0.0813` n `239`; crypto_major avg `-0.2366` n `8`; equity avg `-0.3296` n `164`; fx avg `-0.0388` n `6`; index avg `-0.04` n `27`; metal avg `-0.0304` n `20`; unknown avg `2.7753` n `1261`
- 4h: commodity avg `0.1033` n `13`; crypto_alt avg `0.8234` n `239`; crypto_major avg `0.4446` n `8`; equity avg `1.0486` n `164`; fx avg `-0.0462` n `6`; index avg `0.1099` n `27`; metal avg `0.1637` n `20`; unknown avg `6.3198` n `1257`
- 24h: commodity avg `0.0666` n `13`; crypto_alt avg `-0.2843` n `239`; crypto_major avg `-1.4756` n `8`; equity avg `0.098` n `164`; fx avg `-0.1186` n `6`; index avg `0.1276` n `27`; metal avg `-0.537` n `20`; unknown avg `92.0014` n `1129`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
