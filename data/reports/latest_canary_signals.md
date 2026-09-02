# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T06:07:30.176715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0205` n `12`; crypto_alt avg `-0.1408` n `232`; crypto_major avg `-0.1144` n `8`; equity avg `-0.0583` n `132`; fx avg `-0.0384` n `6`; index avg `-0.0416` n `26`; metal avg `-0.0285` n `20`; unknown avg `0.2868` n `774`
- 1h: commodity avg `-0.007` n `12`; crypto_alt avg `0.335` n `232`; crypto_major avg `0.3302` n `8`; equity avg `0.2229` n `132`; fx avg `-0.0634` n `6`; index avg `0.0064` n `26`; metal avg `0.1219` n `20`; unknown avg `0.3152` n `774`
- 4h: commodity avg `-0.0636` n `12`; crypto_alt avg `1.3484` n `232`; crypto_major avg `0.9356` n `8`; equity avg `0.2461` n `132`; fx avg `-0.1289` n `6`; index avg `-0.0297` n `26`; metal avg `0.1969` n `20`; unknown avg `0.0659` n `774`
- 24h: commodity avg `0.8032` n `12`; crypto_alt avg `-0.6899` n `232`; crypto_major avg `-1.8343` n `8`; equity avg `-2.6733` n `130`; fx avg `-0.1787` n `6`; index avg `-0.5223` n `26`; metal avg `-0.9896` n `20`; unknown avg `-0.3579` n `754`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0458`, n `668`, weak_sample_signal
