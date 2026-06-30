# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T14:37:30.934919+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0518` n `12`; crypto_alt avg `-0.1729` n `228`; crypto_major avg `-0.2909` n `8`; equity avg `-0.0302` n `88`; fx avg `0.0038` n `6`; index avg `0.0022` n `23`; metal avg `-0.0376` n `20`; unknown avg `0.1934` n `765`
- 1h: commodity avg `0.0482` n `12`; crypto_alt avg `1.1684` n `228`; crypto_major avg `0.9731` n `8`; equity avg `0.684` n `88`; fx avg `0.0311` n `6`; index avg `0.1153` n `23`; metal avg `0.4441` n `20`; unknown avg `0.4304` n `765`
- 4h: commodity avg `0.176` n `12`; crypto_alt avg `-0.4112` n `228`; crypto_major avg `-0.4975` n `8`; equity avg `0.5967` n `88`; fx avg `0.0147` n `6`; index avg `0.2176` n `23`; metal avg `0.2264` n `20`; unknown avg `0.123` n `765`
- 24h: commodity avg `0.4126` n `12`; crypto_alt avg `-0.9679` n `228`; crypto_major avg `-0.2726` n `8`; equity avg `2.8884` n `88`; fx avg `0.1101` n `6`; index avg `0.5077` n `23`; metal avg `0.5268` n `20`; unknown avg `8.38` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
