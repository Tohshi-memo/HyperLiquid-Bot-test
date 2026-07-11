# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T07:37:27.955955+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0117` n `12`; crypto_alt avg `-0.0289` n `230`; crypto_major avg `-0.0481` n `8`; equity avg `-0.0433` n `92`; fx avg `0.001` n `6`; index avg `-0.0072` n `25`; metal avg `-0.0108` n `20`; unknown avg `0.0884` n `765`
- 1h: commodity avg `0.0245` n `12`; crypto_alt avg `-0.187` n `230`; crypto_major avg `-0.1373` n `8`; equity avg `0.0779` n `92`; fx avg `-0.0104` n `6`; index avg `0.0189` n `25`; metal avg `-0.0113` n `20`; unknown avg `0.0081` n `763`
- 4h: commodity avg `-0.0036` n `12`; crypto_alt avg `-0.3307` n `229`; crypto_major avg `-0.1008` n `8`; equity avg `0.0792` n `92`; fx avg `0.0163` n `6`; index avg `0.0133` n `25`; metal avg `-0.0319` n `20`; unknown avg `-0.0015` n `731`
- 24h: commodity avg `-0.0955` n `12`; crypto_alt avg `0.365` n `229`; crypto_major avg `-0.0826` n `8`; equity avg `0.1324` n `92`; fx avg `-0.0848` n `6`; index avg `0.1825` n `25`; metal avg `0.0319` n `20`; unknown avg `2.9187` n `730`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
