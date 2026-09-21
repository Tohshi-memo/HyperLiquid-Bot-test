# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T18:52:30.583415+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0465` n `12`; crypto_alt avg `0.3651` n `234`; crypto_major avg `0.4429` n `8`; equity avg `0.122` n `140`; fx avg `0.0034` n `6`; index avg `0.0278` n `26`; metal avg `0.0178` n `20`; unknown avg `0.1727` n `942`
- 1h: commodity avg `-0.0015` n `12`; crypto_alt avg `0.6532` n `234`; crypto_major avg `0.7943` n `8`; equity avg `0.2781` n `140`; fx avg `0.0122` n `6`; index avg `0.0531` n `26`; metal avg `0.0892` n `20`; unknown avg `3.9762` n `940`
- 4h: commodity avg `0.0286` n `12`; crypto_alt avg `-0.7761` n `234`; crypto_major avg `0.3793` n `8`; equity avg `0.7637` n `140`; fx avg `-0.0013` n `6`; index avg `0.1869` n `26`; metal avg `0.0417` n `20`; unknown avg `-0.0255` n `928`
- 24h: commodity avg `-0.9709` n `12`; crypto_alt avg `4.4195` n `234`; crypto_major avg `5.8251` n `8`; equity avg `3.057` n `140`; fx avg `-0.0781` n `6`; index avg `0.6484` n `26`; metal avg `0.0773` n `20`; unknown avg `3.9477` n `747`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1835`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1638`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
