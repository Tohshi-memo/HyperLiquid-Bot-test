# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T16:11:03.316102+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0149` n `12`; crypto_alt avg `-0.1012` n `230`; crypto_major avg `-0.1806` n `8`; equity avg `-0.0517` n `114`; fx avg `-0.0075` n `6`; index avg `0.0006` n `25`; metal avg `0.0148` n `20`; unknown avg `0.1469` n `792`
- 1h: commodity avg `0.0885` n `12`; crypto_alt avg `0.0384` n `230`; crypto_major avg `0.0228` n `8`; equity avg `0.0492` n `114`; fx avg `0.0143` n `6`; index avg `-0.0196` n `25`; metal avg `0.0188` n `20`; unknown avg `-0.0055` n `792`
- 4h: commodity avg `0.1326` n `12`; crypto_alt avg `0.0777` n `230`; crypto_major avg `0.2298` n `8`; equity avg `0.5978` n `114`; fx avg `0.0225` n `6`; index avg `0.0743` n `25`; metal avg `0.1964` n `20`; unknown avg `0.0217` n `792`
- 24h: commodity avg `0.0057` n `12`; crypto_alt avg `-0.1786` n `230`; crypto_major avg `0.8383` n `8`; equity avg `1.6878` n `114`; fx avg `0.0052` n `6`; index avg `0.2132` n `25`; metal avg `0.3301` n `20`; unknown avg `0.0835` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1639`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
