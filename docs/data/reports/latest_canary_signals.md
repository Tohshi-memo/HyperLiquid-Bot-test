# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T23:37:24.425958+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0091` n `12`; crypto_alt avg `0.1081` n `230`; crypto_major avg `-0.0169` n `8`; equity avg `0.0031` n `102`; fx avg `-0.0011` n `6`; index avg `-0.0006` n `25`; metal avg `-0.0074` n `20`; unknown avg `-0.0344` n `781`
- 1h: commodity avg `0.0652` n `12`; crypto_alt avg `0.1197` n `230`; crypto_major avg `-0.0241` n `8`; equity avg `-0.0251` n `102`; fx avg `-0.0219` n `6`; index avg `-0.0224` n `25`; metal avg `-0.0075` n `20`; unknown avg `0.056` n `781`
- 4h: commodity avg `0.6205` n `12`; crypto_alt avg `0.0877` n `230`; crypto_major avg `-0.0868` n `8`; equity avg `-0.7715` n `102`; fx avg `-0.113` n `6`; index avg `-0.1128` n `25`; metal avg `-0.0647` n `20`; unknown avg `2.3459` n `780`
- 24h: commodity avg `0.8091` n `12`; crypto_alt avg `-0.8312` n `230`; crypto_major avg `-2.6012` n `8`; equity avg `-1.8095` n `102`; fx avg `0.0642` n `6`; index avg `-0.0061` n `25`; metal avg `-0.4125` n `20`; unknown avg `2.5193` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
