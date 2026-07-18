# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T11:52:27.892643+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `12`; crypto_alt avg `0.0132` n `230`; crypto_major avg `-0.0016` n `8`; equity avg `-0.0025` n `96`; fx avg `0.0` n `6`; index avg `-0.0072` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.0024` n `770`
- 1h: commodity avg `0.0139` n `12`; crypto_alt avg `0.0466` n `230`; crypto_major avg `-0.0145` n `8`; equity avg `-0.0178` n `96`; fx avg `-0.0024` n `6`; index avg `0.0106` n `25`; metal avg `-0.0` n `20`; unknown avg `-0.0156` n `770`
- 4h: commodity avg `0.1535` n `12`; crypto_alt avg `-0.1109` n `230`; crypto_major avg `-0.0917` n `8`; equity avg `-0.1261` n `96`; fx avg `-0.0013` n `6`; index avg `0.0656` n `25`; metal avg `-0.0014` n `20`; unknown avg `-0.0214` n `769`
- 24h: commodity avg `0.6919` n `12`; crypto_alt avg `-0.5096` n `230`; crypto_major avg `0.0303` n `8`; equity avg `0.6133` n `96`; fx avg `0.0298` n `6`; index avg `0.1656` n `25`; metal avg `0.2676` n `20`; unknown avg `0.0567` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
