# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T21:37:31.729182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0094` n `13`; crypto_alt avg `-0.127` n `237`; crypto_major avg `-0.0796` n `8`; equity avg `0.0105` n `151`; fx avg `-0.0016` n `6`; index avg `0.0038` n `26`; metal avg `-0.0041` n `20`; unknown avg `-0.0491` n `1196`
- 1h: commodity avg `-0.0436` n `13`; crypto_alt avg `0.0671` n `237`; crypto_major avg `0.1237` n `8`; equity avg `0.0841` n `151`; fx avg `0.007` n `6`; index avg `-0.0007` n `26`; metal avg `0.0127` n `20`; unknown avg `2.039` n `1182`
- 4h: commodity avg `-0.2999` n `13`; crypto_alt avg `0.2841` n `237`; crypto_major avg `0.3726` n `8`; equity avg `-0.0501` n `151`; fx avg `-0.0011` n `6`; index avg `0.0002` n `26`; metal avg `-0.051` n `20`; unknown avg `2.2597` n `1122`
- 24h: commodity avg `-0.3523` n `13`; crypto_alt avg `2.8708` n `237`; crypto_major avg `2.0794` n `8`; equity avg `2.9012` n `151`; fx avg `0.0274` n `6`; index avg `0.5778` n `26`; metal avg `0.1033` n `20`; unknown avg `5.5622` n `940`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1945`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
