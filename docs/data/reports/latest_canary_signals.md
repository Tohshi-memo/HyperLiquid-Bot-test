# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T23:37:28.220914+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `13`; crypto_alt avg `-0.0221` n `239`; crypto_major avg `-0.0516` n `8`; equity avg `0.0681` n `168`; fx avg `0.0189` n `6`; index avg `0.0081` n `27`; metal avg `-0.0098` n `20`; unknown avg `1.1889` n `1261`
- 1h: commodity avg `0.0568` n `13`; crypto_alt avg `-0.3271` n `239`; crypto_major avg `-0.3348` n `8`; equity avg `-0.2074` n `168`; fx avg `0.0191` n `6`; index avg `-0.0066` n `27`; metal avg `-0.064` n `20`; unknown avg `53.7106` n `1229`
- 4h: commodity avg `0.0206` n `13`; crypto_alt avg `-0.6036` n `239`; crypto_major avg `-0.6709` n `8`; equity avg `-0.2145` n `168`; fx avg `0.0247` n `6`; index avg `-0.0049` n `27`; metal avg `-0.035` n `20`; unknown avg `61.5918` n `1143`
- 24h: commodity avg `0.1369` n `13`; crypto_alt avg `1.0181` n `239`; crypto_major avg `0.4122` n `8`; equity avg `0.635` n `168`; fx avg `0.0049` n `6`; index avg `0.0656` n `27`; metal avg `-0.0583` n `20`; unknown avg `209.162` n `993`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
