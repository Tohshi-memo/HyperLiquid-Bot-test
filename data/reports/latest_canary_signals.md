# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T07:52:31.617554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1137` n `12`; crypto_alt avg `-0.0782` n `228`; crypto_major avg `-0.0489` n `8`; equity avg `-0.0356` n `74`; fx avg `0.0053` n `6`; index avg `-0.0333` n `23`; metal avg `-0.0524` n `18`; unknown avg `-0.0278` n `556`
- 1h: commodity avg `-0.3061` n `12`; crypto_alt avg `-0.1179` n `228`; crypto_major avg `-0.1154` n `8`; equity avg `0.2421` n `74`; fx avg `-0.0121` n `6`; index avg `0.0399` n `23`; metal avg `0.1955` n `18`; unknown avg `-0.0028` n `548`
- 4h: commodity avg `-0.9048` n `12`; crypto_alt avg `0.719` n `228`; crypto_major avg `0.4371` n `8`; equity avg `0.637` n `74`; fx avg `0.0555` n `6`; index avg `0.243` n `23`; metal avg `0.7065` n `18`; unknown avg `0.0991` n `530`
- 24h: commodity avg `0.4879` n `12`; crypto_alt avg `0.5354` n `228`; crypto_major avg `0.4615` n `8`; equity avg `-0.0332` n `74`; fx avg `0.0195` n `6`; index avg `-0.4127` n `23`; metal avg `-0.3235` n `18`; unknown avg `3.7275` n `527`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
