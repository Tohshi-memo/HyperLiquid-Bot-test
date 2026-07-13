# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T10:07:26.050192+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0805` n `12`; crypto_alt avg `0.0584` n `230`; crypto_major avg `-0.0744` n `8`; equity avg `-0.0375` n `92`; fx avg `-0.0131` n `6`; index avg `0.0074` n `25`; metal avg `0.0001` n `20`; unknown avg `0.0034` n `766`
- 1h: commodity avg `0.0946` n `12`; crypto_alt avg `-0.0699` n `230`; crypto_major avg `-0.224` n `8`; equity avg `0.0544` n `92`; fx avg `-0.041` n `6`; index avg `0.0212` n `25`; metal avg `-0.03` n `20`; unknown avg `-0.0588` n `766`
- 4h: commodity avg `-0.3469` n `12`; crypto_alt avg `0.3069` n `230`; crypto_major avg `-0.0155` n `8`; equity avg `0.3338` n `92`; fx avg `-0.1339` n `6`; index avg `0.1237` n `25`; metal avg `0.3312` n `20`; unknown avg `0.0989` n `766`
- 24h: commodity avg `-0.2542` n `12`; crypto_alt avg `-1.0286` n `230`; crypto_major avg `-1.0143` n `8`; equity avg `-1.955` n `92`; fx avg `-0.0695` n `6`; index avg `-0.3985` n `25`; metal avg `-0.1785` n `20`; unknown avg `-0.002` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1761`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
