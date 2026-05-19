# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T22:37:17.310397+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `12`; crypto_alt avg `-0.0518` n `228`; crypto_major avg `-0.0378` n `8`; equity avg `-0.0801` n `66`; fx avg `-0.0026` n `6`; index avg `0.0021` n `23`; metal avg `0.1083` n `18`; unknown avg `-0.0015` n `383`
- 1h: commodity avg `0.0775` n `12`; crypto_alt avg `-0.6604` n `228`; crypto_major avg `-0.3579` n `8`; equity avg `-0.1198` n `66`; fx avg `-0.0051` n `6`; index avg `-0.0481` n `23`; metal avg `0.0637` n `18`; unknown avg `0.0954` n `383`
- 4h: commodity avg `-0.1013` n `12`; crypto_alt avg `-0.5132` n `228`; crypto_major avg `-0.3796` n `8`; equity avg `-0.5956` n `66`; fx avg `-0.0088` n `6`; index avg `-0.3618` n `23`; metal avg `-0.189` n `18`; unknown avg `-0.0973` n `383`
- 24h: commodity avg `1.1138` n `12`; crypto_alt avg `-1.184` n `228`; crypto_major avg `-0.8878` n `8`; equity avg `-0.3272` n `66`; fx avg `0.0609` n `6`; index avg `-0.7759` n `23`; metal avg `-2.9299` n `18`; unknown avg `0.8576` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
