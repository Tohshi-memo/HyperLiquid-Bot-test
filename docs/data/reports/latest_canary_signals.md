# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T14:37:25.718919+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0573` n `12`; crypto_alt avg `0.5394` n `231`; crypto_major avg `0.4147` n `8`; equity avg `0.4621` n `122`; fx avg `-0.0131` n `6`; index avg `0.0121` n `25`; metal avg `0.0893` n `20`; unknown avg `0.1451` n `795`
- 1h: commodity avg `0.1281` n `12`; crypto_alt avg `0.2212` n `231`; crypto_major avg `0.2735` n `8`; equity avg `0.036` n `122`; fx avg `-0.0159` n `6`; index avg `-0.086` n `25`; metal avg `0.1808` n `20`; unknown avg `-0.0448` n `795`
- 4h: commodity avg `0.0083` n `12`; crypto_alt avg `-0.2986` n `231`; crypto_major avg `-0.3188` n `8`; equity avg `0.0673` n `122`; fx avg `0.0174` n `6`; index avg `-0.0956` n `25`; metal avg `0.0644` n `20`; unknown avg `-0.0586` n `795`
- 24h: commodity avg `-0.702` n `12`; crypto_alt avg `-1.3801` n `231`; crypto_major avg `-0.9695` n `8`; equity avg `1.8024` n `122`; fx avg `0.0232` n `6`; index avg `0.2061` n `25`; metal avg `-0.4101` n `20`; unknown avg `-1.0149` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
