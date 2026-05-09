# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T20:22:14.534643+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `12`; crypto_alt avg `-0.0489` n `228`; crypto_major avg `-0.0388` n `8`; equity avg `0.0193` n `65`; fx avg `0.0119` n `5`; index avg `-0.0066` n `23`; metal avg `0.0277` n `18`; unknown avg `-0.0317` n `376`
- 1h: commodity avg `0.0034` n `12`; crypto_alt avg `-0.0088` n `228`; crypto_major avg `-0.0556` n `8`; equity avg `0.1608` n `65`; fx avg `0.0121` n `5`; index avg `0.0072` n `23`; metal avg `0.0781` n `18`; unknown avg `-0.2645` n `376`
- 4h: commodity avg `0.0233` n `12`; crypto_alt avg `0.3448` n `228`; crypto_major avg `0.0649` n `8`; equity avg `0.2619` n `65`; fx avg `0.0011` n `5`; index avg `0.0241` n `23`; metal avg `0.1317` n `18`; unknown avg `0.0897` n `376`
- 24h: commodity avg `0.3079` n `12`; crypto_alt avg `0.5944` n `228`; crypto_major avg `0.3615` n `8`; equity avg `0.8216` n `65`; fx avg `-0.0436` n `5`; index avg `0.3384` n `23`; metal avg `0.0638` n `18`; unknown avg `0.1991` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
