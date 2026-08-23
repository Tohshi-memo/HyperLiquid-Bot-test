# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T23:22:32.693842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `-0.0767` n `231`; crypto_major avg `0.1785` n `8`; equity avg `0.148` n `122`; fx avg `0.0087` n `6`; index avg `0.0234` n `25`; metal avg `0.0274` n `20`; unknown avg `0.0627` n `793`
- 1h: commodity avg `-0.0693` n `12`; crypto_alt avg `-0.2609` n `231`; crypto_major avg `0.0626` n `8`; equity avg `0.2377` n `122`; fx avg `-0.0077` n `6`; index avg `0.047` n `25`; metal avg `-0.0479` n `20`; unknown avg `0.1182` n `793`
- 4h: commodity avg `-0.1355` n `12`; crypto_alt avg `-0.029` n `231`; crypto_major avg `0.6899` n `8`; equity avg `0.1128` n `122`; fx avg `-0.0794` n `6`; index avg `-0.0015` n `25`; metal avg `-0.0148` n `20`; unknown avg `0.9733` n `793`
- 24h: commodity avg `-0.2743` n `12`; crypto_alt avg `3.3797` n `231`; crypto_major avg `1.9413` n `8`; equity avg `0.8809` n `122`; fx avg `-0.111` n `6`; index avg `0.1217` n `25`; metal avg `0.0654` n `20`; unknown avg `5.8957` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
