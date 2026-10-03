# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T09:07:31.119963+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0072` n `13`; crypto_alt avg `-0.0655` n `235`; crypto_major avg `0.0222` n `8`; equity avg `0.0115` n `143`; fx avg `0.0015` n `6`; index avg `0.0028` n `26`; metal avg `0.0035` n `20`; unknown avg `0.3069` n `984`
- 1h: commodity avg `0.0171` n `13`; crypto_alt avg `-0.126` n `235`; crypto_major avg `-0.0864` n `8`; equity avg `0.0203` n `143`; fx avg `0.004` n `6`; index avg `0.001` n `26`; metal avg `0.0059` n `20`; unknown avg `1.3125` n `966`
- 4h: commodity avg `-0.0068` n `13`; crypto_alt avg `-0.5419` n `235`; crypto_major avg `-0.0793` n `8`; equity avg `0.0089` n `143`; fx avg `-0.004` n `6`; index avg `0.0008` n `26`; metal avg `0.006` n `20`; unknown avg `0.3773` n `944`
- 24h: commodity avg `0.716` n `13`; crypto_alt avg `-2.6036` n `235`; crypto_major avg `-2.459` n `8`; equity avg `-0.0205` n `142`; fx avg `0.0387` n `6`; index avg `0.1212` n `26`; metal avg `-0.309` n `20`; unknown avg `0.1225` n `872`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1841`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
