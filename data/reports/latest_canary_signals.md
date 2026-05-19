# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T09:07:15.989192+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1324` n `12`; crypto_alt avg `-0.1807` n `228`; crypto_major avg `-0.0437` n `8`; equity avg `-0.1742` n `66`; fx avg `-0.0465` n `6`; index avg `-0.0154` n `23`; metal avg `-0.249` n `18`; unknown avg `-0.1192` n `383`
- 1h: commodity avg `0.0108` n `12`; crypto_alt avg `-0.1782` n `228`; crypto_major avg `-0.0641` n `8`; equity avg `-0.3207` n `66`; fx avg `-0.0542` n `6`; index avg `-0.1539` n `23`; metal avg `-0.3491` n `18`; unknown avg `-0.1507` n `383`
- 4h: commodity avg `0.3506` n `12`; crypto_alt avg `-0.2857` n `228`; crypto_major avg `0.1533` n `8`; equity avg `0.1407` n `66`; fx avg `-0.0586` n `6`; index avg `0.0723` n `23`; metal avg `-0.3981` n `18`; unknown avg `-0.2972` n `363`
- 24h: commodity avg `0.6313` n `12`; crypto_alt avg `1.4706` n `228`; crypto_major avg `0.9926` n `8`; equity avg `-1.6257` n `66`; fx avg `0.2521` n `6`; index avg `-0.6257` n `23`; metal avg `-0.4486` n `18`; unknown avg `0.7281` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
