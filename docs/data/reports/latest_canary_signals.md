# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T16:52:18.616343+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0275` n `12`; crypto_alt avg `0.0252` n `228`; crypto_major avg `-0.0389` n `8`; equity avg `0.0085` n `65`; fx avg `0.0` n `5`; index avg `-0.0378` n `23`; metal avg `0.0006` n `18`; unknown avg `0.2115` n `376`
- 1h: commodity avg `0.04` n `12`; crypto_alt avg `0.209` n `228`; crypto_major avg `0.0389` n `8`; equity avg `0.0505` n `65`; fx avg `-0.0068` n `5`; index avg `-0.0182` n `23`; metal avg `0.0085` n `18`; unknown avg `-0.1734` n `376`
- 4h: commodity avg `0.3304` n `12`; crypto_alt avg `-0.6805` n `228`; crypto_major avg `-0.3905` n `8`; equity avg `0.0203` n `65`; fx avg `-0.0138` n `5`; index avg `0.0371` n `23`; metal avg `-0.0633` n `18`; unknown avg `-0.1957` n `376`
- 24h: commodity avg `-0.2489` n `12`; crypto_alt avg `1.1647` n `228`; crypto_major avg `1.3086` n `8`; equity avg `1.8192` n `65`; fx avg `0.0057` n `5`; index avg `0.5535` n `23`; metal avg `0.0762` n `18`; unknown avg `0.3141` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
