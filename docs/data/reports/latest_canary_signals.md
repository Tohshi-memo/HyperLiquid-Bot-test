# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T12:52:17.089484+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.42` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.2004` n `12`; crypto_alt avg `0.1046` n `228`; crypto_major avg `0.1346` n `8`; equity avg `-0.08` n `66`; fx avg `0.0129` n `6`; index avg `-0.0968` n `23`; metal avg `-0.0098` n `18`; unknown avg `-0.0963` n `386`
- 1h: commodity avg `0.1766` n `12`; crypto_alt avg `0.2992` n `228`; crypto_major avg `0.202` n `8`; equity avg `-0.1373` n `66`; fx avg `-0.0164` n `6`; index avg `-0.1451` n `23`; metal avg `-0.0675` n `18`; unknown avg `0.036` n `386`
- 4h: commodity avg `0.7317` n `12`; crypto_alt avg `-0.7996` n `228`; crypto_major avg `-0.7727` n `8`; equity avg `-0.4567` n `66`; fx avg `0.0075` n `6`; index avg `-0.341` n `23`; metal avg `-0.4717` n `18`; unknown avg `1.0741` n `386`
- 24h: commodity avg `-0.7505` n `12`; crypto_alt avg `1.5766` n `228`; crypto_major avg `2.0441` n `8`; equity avg `0.867` n `66`; fx avg `0.0504` n `6`; index avg `0.7454` n `23`; metal avg `-0.2252` n `18`; unknown avg `6.1042` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.052`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0465`, n `668`, weak_sample_signal
