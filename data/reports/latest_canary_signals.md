# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T01:37:23.759656+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0175` n `12`; crypto_alt avg `-0.0098` n `232`; crypto_major avg `-0.0172` n `8`; equity avg `-0.0236` n `134`; fx avg `0.0344` n `6`; index avg `0.0126` n `26`; metal avg `0.1276` n `20`; unknown avg `141.3413` n `794`
- 1h: commodity avg `0.0123` n `12`; crypto_alt avg `-0.9214` n `232`; crypto_major avg `-0.5633` n `8`; equity avg `-0.1052` n `134`; fx avg `0.0264` n `6`; index avg `0.0186` n `26`; metal avg `0.0067` n `20`; unknown avg `-0.319` n `790`
- 4h: commodity avg `-0.0276` n `12`; crypto_alt avg `-0.6095` n `232`; crypto_major avg `-0.5577` n `8`; equity avg `-0.0167` n `134`; fx avg `-0.0723` n `6`; index avg `0.0079` n `26`; metal avg `-0.0653` n `20`; unknown avg `0.6214` n `783`
- 24h: commodity avg `-0.0526` n `12`; crypto_alt avg `-0.0153` n `232`; crypto_major avg `-0.1173` n `8`; equity avg `0.1926` n `134`; fx avg `-0.036` n `6`; index avg `0.0293` n `26`; metal avg `-0.0938` n `20`; unknown avg `150.8229` n `676`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
