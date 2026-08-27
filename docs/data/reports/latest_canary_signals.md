# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T04:22:25.717182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0187` n `12`; crypto_alt avg `0.0137` n `231`; crypto_major avg `-0.0005` n `8`; equity avg `0.0052` n `126`; fx avg `0.0138` n `6`; index avg `0.007` n `25`; metal avg `-0.01` n `20`; unknown avg `0.5836` n `793`
- 1h: commodity avg `0.0238` n `12`; crypto_alt avg `-0.2032` n `231`; crypto_major avg `-0.1957` n `8`; equity avg `-0.1293` n `126`; fx avg `-0.0111` n `6`; index avg `-0.0158` n `25`; metal avg `-0.1069` n `20`; unknown avg `-0.1192` n `793`
- 4h: commodity avg `0.063` n `12`; crypto_alt avg `-0.7085` n `231`; crypto_major avg `-0.4626` n `8`; equity avg `-0.04` n `126`; fx avg `-0.0104` n `6`; index avg `-0.0488` n `25`; metal avg `0.0307` n `20`; unknown avg `0.0776` n `793`
- 24h: commodity avg `0.4909` n `12`; crypto_alt avg `0.1167` n `231`; crypto_major avg `0.2878` n `8`; equity avg `1.0994` n `126`; fx avg `-0.0825` n `6`; index avg `0.1531` n `25`; metal avg `-0.2499` n `20`; unknown avg `0.2261` n `777`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
