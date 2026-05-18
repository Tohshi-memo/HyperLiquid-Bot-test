# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T18:52:21.949632+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0194` n `12`; crypto_alt avg `-0.0778` n `228`; crypto_major avg `-0.1224` n `8`; equity avg `-0.0972` n `66`; fx avg `0.0023` n `6`; index avg `-0.0623` n `23`; metal avg `-0.0282` n `18`; unknown avg `-0.1234` n `383`
- 1h: commodity avg `0.3581` n `12`; crypto_alt avg `-0.7702` n `228`; crypto_major avg `-0.6086` n `8`; equity avg `-0.7105` n `66`; fx avg `-0.0757` n `6`; index avg `-0.3056` n `23`; metal avg `-0.3068` n `18`; unknown avg `-0.1837` n `383`
- 4h: commodity avg `0.9212` n `12`; crypto_alt avg `-0.4503` n `228`; crypto_major avg `-0.3507` n `8`; equity avg `-1.0553` n `66`; fx avg `0.1036` n `6`; index avg `-0.6023` n `23`; metal avg `-0.1069` n `18`; unknown avg `-0.4344` n `383`
- 24h: commodity avg `1.42` n `12`; crypto_alt avg `-2.8467` n `228`; crypto_major avg `-2.551` n `8`; equity avg `-1.6201` n `66`; fx avg `0.1366` n `6`; index avg `-0.7947` n `23`; metal avg `0.3404` n `18`; unknown avg `-0.571` n `362`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1686`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
