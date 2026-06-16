# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T00:52:32.592828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.22` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0053` n `12`; crypto_alt avg `-0.1196` n `228`; crypto_major avg `-0.0148` n `8`; equity avg `-0.1209` n `77`; fx avg `0.0052` n `6`; index avg `-0.0652` n `23`; metal avg `-0.0439` n `18`; unknown avg `0.0065` n `687`
- 1h: commodity avg `-0.0865` n `12`; crypto_alt avg `0.1871` n `228`; crypto_major avg `0.0296` n `8`; equity avg `-0.2977` n `77`; fx avg `0.0088` n `6`; index avg `-0.1237` n `23`; metal avg `-0.184` n `18`; unknown avg `-0.2136` n `687`
- 4h: commodity avg `0.0754` n `12`; crypto_alt avg `-0.2936` n `228`; crypto_major avg `-0.8125` n `8`; equity avg `-0.3531` n `77`; fx avg `-0.0055` n `6`; index avg `-0.0598` n `23`; metal avg `-0.1673` n `18`; unknown avg `0.1237` n `679`
- 24h: commodity avg `0.6037` n `12`; crypto_alt avg `1.3762` n `228`; crypto_major avg `2.3376` n `8`; equity avg `1.1739` n `76`; fx avg `0.0053` n `6`; index avg `0.506` n `23`; metal avg `-0.0475` n `18`; unknown avg `1.8636` n `519`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0438`, n `668`, weak_sample_signal
