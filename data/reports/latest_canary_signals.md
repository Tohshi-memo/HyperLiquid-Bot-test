# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T10:22:27.403636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1364` n `12`; crypto_alt avg `0.144` n `229`; crypto_major avg `0.1586` n `8`; equity avg `0.2171` n `91`; fx avg `-0.0016` n `6`; index avg `0.0511` n `25`; metal avg `0.1103` n `20`; unknown avg `0.0595` n `763`
- 1h: commodity avg `-0.2138` n `12`; crypto_alt avg `0.076` n `229`; crypto_major avg `0.2357` n `8`; equity avg `0.3921` n `91`; fx avg `-0.0388` n `6`; index avg `0.05` n `25`; metal avg `0.0114` n `20`; unknown avg `0.0839` n `763`
- 4h: commodity avg `0.4126` n `12`; crypto_alt avg `-1.097` n `229`; crypto_major avg `-0.5868` n `8`; equity avg `-1.7751` n `91`; fx avg `0.0285` n `6`; index avg `-0.3913` n `25`; metal avg `-1.1071` n `20`; unknown avg `-0.3496` n `763`
- 24h: commodity avg `1.3007` n `12`; crypto_alt avg `-4.2092` n `229`; crypto_major avg `-3.3412` n `8`; equity avg `-3.259` n `91`; fx avg `-0.1274` n `6`; index avg `-0.7285` n `25`; metal avg `-1.2322` n `20`; unknown avg `-0.8735` n `733`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
