# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T06:07:33.945243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.045` n `12`; crypto_alt avg `-0.3408` n `228`; crypto_major avg `-0.3458` n `8`; equity avg `-0.3583` n `86`; fx avg `0.0355` n `6`; index avg `-0.0787` n `23`; metal avg `-0.0803` n `20`; unknown avg `-0.0539` n `684`
- 1h: commodity avg `-0.1912` n `12`; crypto_alt avg `-0.6407` n `228`; crypto_major avg `-0.6927` n `8`; equity avg `-0.8998` n `86`; fx avg `0.03` n `6`; index avg `-0.1831` n `23`; metal avg `-0.193` n `20`; unknown avg `-0.234` n `676`
- 4h: commodity avg `-0.1501` n `12`; crypto_alt avg `-0.9183` n `228`; crypto_major avg `-1.183` n `8`; equity avg `-1.7205` n `86`; fx avg `0.0161` n `6`; index avg `-0.3673` n `23`; metal avg `-0.4746` n `20`; unknown avg `0.2802` n `676`
- 24h: commodity avg `-0.562` n `12`; crypto_alt avg `-1.6114` n `228`; crypto_major avg `-1.7243` n `8`; equity avg `-3.8312` n `85`; fx avg `0.0199` n `6`; index avg `-0.6689` n `23`; metal avg `-1.3663` n `18`; unknown avg `0.7713` n `647`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
