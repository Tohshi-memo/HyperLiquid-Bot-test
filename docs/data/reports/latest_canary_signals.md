# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T20:22:26.014689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.006` n `12`; crypto_alt avg `-0.1909` n `228`; crypto_major avg `-0.3144` n `8`; equity avg `-0.0157` n `78`; fx avg `-0.0094` n `6`; index avg `-0.0021` n `23`; metal avg `-0.0016` n `18`; unknown avg `0.0371` n `687`
- 1h: commodity avg `-0.0273` n `12`; crypto_alt avg `-0.0604` n `228`; crypto_major avg `-0.2717` n `8`; equity avg `-0.0273` n `78`; fx avg `-0.0031` n `6`; index avg `-0.0079` n `23`; metal avg `0.0759` n `18`; unknown avg `-0.2368` n `687`
- 4h: commodity avg `-0.1708` n `12`; crypto_alt avg `-0.7583` n `228`; crypto_major avg `-0.4919` n `8`; equity avg `-0.1971` n `78`; fx avg `0.0073` n `6`; index avg `-0.0428` n `23`; metal avg `0.2798` n `18`; unknown avg `-0.0682` n `687`
- 24h: commodity avg `0.2684` n `12`; crypto_alt avg `-3.9183` n `228`; crypto_major avg `-4.8313` n `8`; equity avg `0.6642` n `78`; fx avg `-0.1017` n `6`; index avg `0.2239` n `23`; metal avg `-4.161` n `18`; unknown avg `-0.4545` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0524`, n `668`, weak_sample_signal
