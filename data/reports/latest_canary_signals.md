# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T11:22:37.846598+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0293` n `13`; crypto_alt avg `-0.2147` n `239`; crypto_major avg `-0.1582` n `8`; equity avg `-0.1309` n `168`; fx avg `0.0066` n `6`; index avg `-0.0165` n `27`; metal avg `0.0045` n `20`; unknown avg `0.1204` n `1235`
- 1h: commodity avg `-0.0598` n `13`; crypto_alt avg `-0.3069` n `239`; crypto_major avg `-0.0673` n `8`; equity avg `0.0895` n `168`; fx avg `0.0111` n `6`; index avg `-0.0138` n `27`; metal avg `-0.0009` n `20`; unknown avg `0.1932` n `1197`
- 4h: commodity avg `0.2164` n `13`; crypto_alt avg `-0.8752` n `239`; crypto_major avg `-0.8659` n `8`; equity avg `-0.7288` n `168`; fx avg `0.0263` n `6`; index avg `-0.1061` n `27`; metal avg `0.069` n `20`; unknown avg `0.5888` n `1177`
- 24h: commodity avg `0.3519` n `13`; crypto_alt avg `-1.8231` n `239`; crypto_major avg `-2.5039` n `8`; equity avg `-4.1467` n `167`; fx avg `0.0156` n `6`; index avg `-0.3697` n `27`; metal avg `-0.9063` n `20`; unknown avg `428.0732` n `1067`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
