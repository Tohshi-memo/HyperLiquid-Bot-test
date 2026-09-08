# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T11:07:27.589577+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0365` n `12`; crypto_alt avg `-0.2893` n `232`; crypto_major avg `-0.2952` n `8`; equity avg `0.0391` n `134`; fx avg `0.021` n `6`; index avg `-0.013` n `26`; metal avg `-0.0623` n `20`; unknown avg `0.326` n `795`
- 1h: commodity avg `0.0219` n `12`; crypto_alt avg `-0.5581` n `232`; crypto_major avg `-0.4643` n `8`; equity avg `0.0095` n `134`; fx avg `0.0235` n `6`; index avg `-0.0125` n `26`; metal avg `-0.093` n `20`; unknown avg `0.6922` n `795`
- 4h: commodity avg `0.0374` n `12`; crypto_alt avg `0.4563` n `232`; crypto_major avg `0.1928` n `8`; equity avg `-0.0171` n `134`; fx avg `-0.0219` n `6`; index avg `-0.0303` n `26`; metal avg `-0.13` n `20`; unknown avg `-0.042` n `787`
- 24h: commodity avg `0.2403` n `12`; crypto_alt avg `0.4582` n `232`; crypto_major avg `-0.8319` n `8`; equity avg `-0.0954` n `134`; fx avg `-0.1261` n `6`; index avg `-0.0388` n `26`; metal avg `0.0734` n `20`; unknown avg `7462.1666` n `670`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
