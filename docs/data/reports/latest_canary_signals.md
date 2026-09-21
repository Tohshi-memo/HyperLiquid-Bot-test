# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T17:52:30.690862+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0248` n `12`; crypto_alt avg `-0.4821` n `234`; crypto_major avg `-0.4386` n `8`; equity avg `0.1464` n `140`; fx avg `0.0027` n `6`; index avg `0.0248` n `26`; metal avg `0.0406` n `20`; unknown avg `0.0085` n `942`
- 1h: commodity avg `0.2078` n `12`; crypto_alt avg `-0.9767` n `234`; crypto_major avg `-0.2902` n `8`; equity avg `0.0704` n `140`; fx avg `0.0018` n `6`; index avg `0.0205` n `26`; metal avg `-0.0208` n `20`; unknown avg `0.4098` n `940`
- 4h: commodity avg `-0.1651` n `12`; crypto_alt avg `-1.104` n `234`; crypto_major avg `-0.0236` n `8`; equity avg `0.7518` n `140`; fx avg `-0.0113` n `6`; index avg `0.2098` n `26`; metal avg `-0.1698` n `20`; unknown avg `1.319` n `870`
- 24h: commodity avg `-0.9844` n `12`; crypto_alt avg `3.1965` n `234`; crypto_major avg `4.7332` n `8`; equity avg `2.7048` n `140`; fx avg `-0.0895` n `6`; index avg `0.5944` n `26`; metal avg `-0.0465` n `20`; unknown avg `6.8002` n `739`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1855`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
