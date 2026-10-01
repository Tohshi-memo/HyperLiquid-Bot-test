# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T09:52:30.525808+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `13`; crypto_alt avg `-0.1979` n `234`; crypto_major avg `-0.1109` n `8`; equity avg `-0.0245` n `142`; fx avg `-0.0062` n `6`; index avg `-0.004` n `26`; metal avg `-0.0015` n `20`; unknown avg `1.2999` n `975`
- 1h: commodity avg `-0.1271` n `13`; crypto_alt avg `-0.089` n `234`; crypto_major avg `0.2171` n `8`; equity avg `0.1866` n `142`; fx avg `0.0275` n `6`; index avg `0.0641` n `26`; metal avg `0.0655` n `20`; unknown avg `5.2437` n `973`
- 4h: commodity avg `0.3793` n `13`; crypto_alt avg `-1.0263` n `234`; crypto_major avg `-0.7752` n `8`; equity avg `-0.6249` n `142`; fx avg `-0.0353` n `6`; index avg `-0.1659` n `26`; metal avg `-0.3807` n `20`; unknown avg `6.9866` n `930`
- 24h: commodity avg `-0.0716` n `13`; crypto_alt avg `-0.4951` n `234`; crypto_major avg `0.1941` n `8`; equity avg `0.3966` n `142`; fx avg `0.0816` n `6`; index avg `0.1278` n `26`; metal avg `-0.3183` n `20`; unknown avg `774.3143` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1672`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
