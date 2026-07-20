# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T05:07:24.321648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0331` n `12`; crypto_alt avg `-0.2496` n `230`; crypto_major avg `-0.2543` n `8`; equity avg `-0.2453` n `98`; fx avg `0.0055` n `6`; index avg `-0.0839` n `25`; metal avg `-0.0304` n `20`; unknown avg `-0.0304` n `769`
- 1h: commodity avg `-0.0402` n `12`; crypto_alt avg `-0.3518` n `230`; crypto_major avg `-0.3628` n `8`; equity avg `-0.014` n `98`; fx avg `-0.0079` n `6`; index avg `0.0251` n `25`; metal avg `-0.0305` n `20`; unknown avg `-0.1127` n `769`
- 4h: commodity avg `-0.0246` n `12`; crypto_alt avg `-0.4795` n `230`; crypto_major avg `-0.368` n `8`; equity avg `-0.2124` n `98`; fx avg `-0.0318` n `6`; index avg `-0.0383` n `25`; metal avg `0.041` n `20`; unknown avg `-0.4445` n `769`
- 24h: commodity avg `-0.0784` n `12`; crypto_alt avg `-0.4933` n `230`; crypto_major avg `-0.3366` n `8`; equity avg `0.223` n `97`; fx avg `-0.0191` n `6`; index avg `0.0546` n `25`; metal avg `0.068` n `20`; unknown avg `0.0061` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1135`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1023`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0973`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0955`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.088`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0846`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0788`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
