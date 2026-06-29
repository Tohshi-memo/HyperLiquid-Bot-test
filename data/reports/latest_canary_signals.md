# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T17:37:30.887114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.97` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `2.0178` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `1.935` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.062` n `12`; crypto_alt avg `0.1672` n `228`; crypto_major avg `0.04` n `8`; equity avg `0.069` n `88`; fx avg `-0.0034` n `6`; index avg `0.0177` n `23`; metal avg `-0.0337` n `20`; unknown avg `0.316` n `765`
- 1h: commodity avg `-0.0058` n `12`; crypto_alt avg `1.3277` n `228`; crypto_major avg `1.946` n `8`; equity avg `0.6009` n `88`; fx avg `-0.0115` n `6`; index avg `0.0577` n `23`; metal avg `0.011` n `20`; unknown avg `1.4503` n `765`
- 4h: commodity avg `0.1275` n `12`; crypto_alt avg `1.3671` n `228`; crypto_major avg `1.7577` n `8`; equity avg `0.9401` n `88`; fx avg `0.0102` n `6`; index avg `0.1085` n `23`; metal avg `-0.2601` n `20`; unknown avg `0.7317` n `764`
- 24h: commodity avg `-0.5059` n `12`; crypto_alt avg `2.0667` n `228`; crypto_major avg `2.7655` n `8`; equity avg `1.3712` n `88`; fx avg `0.1289` n `6`; index avg `0.1359` n `23`; metal avg `-0.6856` n `20`; unknown avg `3.4946` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
