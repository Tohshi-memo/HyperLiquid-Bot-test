# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T08:52:30.163974+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `12`; crypto_alt avg `-0.0736` n `230`; crypto_major avg `-0.0195` n `8`; equity avg `0.0239` n `102`; fx avg `0.0055` n `6`; index avg `0.0144` n `25`; metal avg `-0.0333` n `20`; unknown avg `0.0012` n `780`
- 1h: commodity avg `0.049` n `12`; crypto_alt avg `-0.2162` n `230`; crypto_major avg `-0.0407` n `8`; equity avg `0.2772` n `102`; fx avg `-0.0156` n `6`; index avg `-0.0053` n `25`; metal avg `-0.1006` n `20`; unknown avg `0.008` n `779`
- 4h: commodity avg `0.1` n `12`; crypto_alt avg `0.2184` n `230`; crypto_major avg `-0.2352` n `8`; equity avg `0.1012` n `102`; fx avg `-0.1242` n `6`; index avg `0.0078` n `25`; metal avg `-0.1487` n `20`; unknown avg `-0.0282` n `747`
- 24h: commodity avg `-0.3785` n `12`; crypto_alt avg `-0.1497` n `230`; crypto_major avg `0.1947` n `8`; equity avg `8.705` n `102`; fx avg `-0.2153` n `6`; index avg `1.253` n `25`; metal avg `0.2983` n `20`; unknown avg `0.0212` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
