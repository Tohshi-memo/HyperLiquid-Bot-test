# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T22:22:27.271426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.82` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `-0.0819` n `228`; crypto_major avg `-0.0523` n `8`; equity avg `0.0114` n `88`; fx avg `-0.0114` n `6`; index avg `0.0102` n `23`; metal avg `-0.0238` n `20`; unknown avg `-0.2` n `765`
- 1h: commodity avg `-0.0537` n `12`; crypto_alt avg `0.371` n `228`; crypto_major avg `0.2479` n `8`; equity avg `0.1119` n `88`; fx avg `0.0095` n `6`; index avg `0.0261` n `23`; metal avg `0.0662` n `20`; unknown avg `2.4645` n `765`
- 4h: commodity avg `0.0857` n `12`; crypto_alt avg `-0.2986` n `228`; crypto_major avg `-0.0901` n `8`; equity avg `0.3838` n `88`; fx avg `-0.0043` n `6`; index avg `-0.0275` n `23`; metal avg `-0.2163` n `20`; unknown avg `3.1783` n `763`
- 24h: commodity avg `0.1195` n `12`; crypto_alt avg `-2.1829` n `228`; crypto_major avg `-2.327` n `8`; equity avg `1.1976` n `88`; fx avg `0.1157` n `6`; index avg `0.2648` n `23`; metal avg `-0.0145` n `20`; unknown avg `9.8463` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0498`, n `668`, weak_sample_signal
