# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T02:30:24.938658+00:00`
- Correlation status: `ready`
- Asset price records: `33`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `7`; crypto_alt avg `-0.0334` n `223`; crypto_major avg `-0.1194` n `7`; equity avg `0.031` n `42`; fx avg `-0.0059` n `4`; index avg `0.0064` n `9`; metal avg `-0.0003` n `7`; unknown avg `-0.0281` n `311`
- 1h: commodity avg `0.0021` n `7`; crypto_alt avg `-0.1737` n `223`; crypto_major avg `-0.136` n `7`; equity avg `0.0202` n `42`; fx avg `-0.017` n `4`; index avg `-0.0172` n `9`; metal avg `0.0107` n `7`; unknown avg `-0.0028` n `311`
- 4h: commodity avg `0.0433` n `7`; crypto_alt avg `-0.1895` n `223`; crypto_major avg `-0.1652` n `7`; equity avg `0.1501` n `42`; fx avg `0.0467` n `4`; index avg `-0.0867` n `9`; metal avg `-0.0022` n `7`; unknown avg `-0.0742` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.671`, n `29`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6469`, n `29`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5615`, n `25`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.556`, n `25`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5316`, n `29`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.5174`, n `25`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5067`, n `29`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4915`, n `29`, moderate_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.4832`, n `29`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4786`, n `25`, moderate_sample_signal
