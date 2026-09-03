# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T05:07:25.485408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0128` n `12`; crypto_alt avg `0.0598` n `232`; crypto_major avg `0.0331` n `8`; equity avg `-0.2272` n `133`; fx avg `0.0331` n `6`; index avg `-0.0512` n `26`; metal avg `-0.0654` n `20`; unknown avg `-0.0747` n `790`
- 1h: commodity avg `-0.0887` n `12`; crypto_alt avg `0.3251` n `232`; crypto_major avg `0.017` n `8`; equity avg `-0.3052` n `133`; fx avg `0.0307` n `6`; index avg `-0.0637` n `26`; metal avg `-0.0348` n `20`; unknown avg `-0.233` n `790`
- 4h: commodity avg `-0.028` n `12`; crypto_alt avg `1.1114` n `232`; crypto_major avg `0.8561` n `8`; equity avg `-0.0093` n `133`; fx avg `-0.0532` n `6`; index avg `-0.0228` n `26`; metal avg `0.164` n `20`; unknown avg `0.1094` n `790`
- 24h: commodity avg `0.1015` n `12`; crypto_alt avg `0.7686` n `232`; crypto_major avg `0.6238` n `8`; equity avg `1.4411` n `133`; fx avg `-0.3231` n `6`; index avg `0.1679` n `26`; metal avg `0.853` n `20`; unknown avg `-0.498` n `751`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0462`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0454`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0451`, n `668`, weak_sample_signal
