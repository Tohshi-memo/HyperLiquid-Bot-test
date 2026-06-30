# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T08:52:29.398003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0319` n `12`; crypto_alt avg `0.002` n `228`; crypto_major avg `0.0365` n `8`; equity avg `-0.1627` n `88`; fx avg `-0.0006` n `6`; index avg `-0.0066` n `23`; metal avg `-0.0542` n `20`; unknown avg `0.0937` n `765`
- 1h: commodity avg `0.0915` n `12`; crypto_alt avg `-0.4223` n `228`; crypto_major avg `-0.4119` n `8`; equity avg `-0.3107` n `88`; fx avg `-0.0279` n `6`; index avg `-0.0247` n `23`; metal avg `-0.1781` n `20`; unknown avg `-0.0103` n `765`
- 4h: commodity avg `0.194` n `12`; crypto_alt avg `-0.7147` n `228`; crypto_major avg `-0.5201` n `8`; equity avg `-0.639` n `88`; fx avg `0.0467` n `6`; index avg `-0.1388` n `23`; metal avg `0.2591` n `20`; unknown avg `-0.7466` n `737`
- 24h: commodity avg `0.0712` n `12`; crypto_alt avg `-0.7747` n `228`; crypto_major avg `0.3548` n `8`; equity avg `1.1726` n `88`; fx avg `0.1624` n `6`; index avg `0.0975` n `23`; metal avg `-0.1685` n `20`; unknown avg `8.7656` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
