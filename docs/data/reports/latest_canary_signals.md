# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T04:51:03.645093+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.12` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `1.6045` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5354` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0129` n `12`; crypto_alt avg `0.3093` n `228`; crypto_major avg `0.2961` n `8`; equity avg `0.1306` n `88`; fx avg `-0.0426` n `6`; index avg `0.0362` n `23`; metal avg `0.0742` n `20`; unknown avg `1.3267` n `765`
- 1h: commodity avg `-0.0276` n `12`; crypto_alt avg `0.4721` n `228`; crypto_major avg `0.2391` n `8`; equity avg `0.0439` n `88`; fx avg `-0.0691` n `6`; index avg `0.0014` n `23`; metal avg `0.0238` n `20`; unknown avg `0.4945` n `765`
- 4h: commodity avg `-0.0606` n `12`; crypto_alt avg `1.6145` n `228`; crypto_major avg `1.3782` n `8`; equity avg `-0.1572` n `88`; fx avg `-0.0674` n `6`; index avg `-0.1261` n `23`; metal avg `-0.2263` n `20`; unknown avg `2.4557` n `763`
- 24h: commodity avg `0.0963` n `12`; crypto_alt avg `0.0881` n `228`; crypto_major avg `0.3547` n `8`; equity avg `0.4545` n `88`; fx avg `0.1016` n `6`; index avg `-0.04` n `23`; metal avg `-0.2481` n `20`; unknown avg `-0.8288` n `733`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
