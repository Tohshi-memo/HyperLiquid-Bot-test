# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T07:22:30.265197+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0339` n `12`; crypto_alt avg `0.2104` n `228`; crypto_major avg `0.2907` n `8`; equity avg `0.0523` n `88`; fx avg `-0.0072` n `6`; index avg `0.0032` n `23`; metal avg `0.1084` n `20`; unknown avg `0.0164` n `765`
- 1h: commodity avg `0.036` n `12`; crypto_alt avg `-0.3633` n `228`; crypto_major avg `-0.1722` n `8`; equity avg `-0.1178` n `88`; fx avg `-0.013` n `6`; index avg `-0.0284` n `23`; metal avg `0.001` n `20`; unknown avg `-0.042` n `763`
- 4h: commodity avg `-0.0946` n `12`; crypto_alt avg `-0.0549` n `228`; crypto_major avg `-0.2875` n `8`; equity avg `-0.2391` n `88`; fx avg `-0.0458` n `6`; index avg `-0.0248` n `23`; metal avg `-0.1949` n `20`; unknown avg `0.2508` n `743`
- 24h: commodity avg `-0.0725` n `12`; crypto_alt avg `-0.9561` n `228`; crypto_major avg `-0.6242` n `8`; equity avg `0.2667` n `88`; fx avg `0.0897` n `6`; index avg `-0.0577` n `23`; metal avg `-0.8579` n `20`; unknown avg `-0.2862` n `743`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
