# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T10:07:30.120986+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0239` n `12`; crypto_alt avg `0.2213` n `229`; crypto_major avg `0.2589` n `8`; equity avg `0.0276` n `88`; fx avg `0.0034` n `6`; index avg `-0.0086` n `25`; metal avg `-0.0093` n `20`; unknown avg `0.1077` n `765`
- 1h: commodity avg `0.0699` n `12`; crypto_alt avg `0.127` n `229`; crypto_major avg `-0.0802` n `8`; equity avg `-0.0762` n `88`; fx avg `-0.0095` n `6`; index avg `-0.0091` n `25`; metal avg `-0.1027` n `20`; unknown avg `0.1092` n `765`
- 4h: commodity avg `-0.1096` n `12`; crypto_alt avg `0.0678` n `229`; crypto_major avg `-0.2216` n `8`; equity avg `0.0341` n `88`; fx avg `0.0212` n `6`; index avg `0.0389` n `25`; metal avg `0.0288` n `20`; unknown avg `-0.0383` n `763`
- 24h: commodity avg `-0.111` n `12`; crypto_alt avg `0.3796` n `229`; crypto_major avg `0.8416` n `8`; equity avg `-0.5568` n `88`; fx avg `0.0768` n `6`; index avg `-0.008` n `25`; metal avg `-0.2851` n `20`; unknown avg `1.2761` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
