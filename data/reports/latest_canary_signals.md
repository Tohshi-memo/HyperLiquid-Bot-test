# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T20:07:31.705362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `12`; crypto_alt avg `-0.0834` n `230`; crypto_major avg `-0.1699` n `8`; equity avg `-0.7355` n `108`; fx avg `0.0123` n `6`; index avg `-0.0917` n `25`; metal avg `-0.0132` n `20`; unknown avg `0.0555` n `782`
- 1h: commodity avg `-0.0435` n `12`; crypto_alt avg `-0.163` n `230`; crypto_major avg `-0.1631` n `8`; equity avg `-1.0456` n `108`; fx avg `0.0214` n `6`; index avg `-0.139` n `25`; metal avg `-0.0994` n `20`; unknown avg `-0.0553` n `782`
- 4h: commodity avg `-0.1138` n `12`; crypto_alt avg `0.1352` n `230`; crypto_major avg `0.3806` n `8`; equity avg `-0.8869` n `108`; fx avg `0.0087` n `6`; index avg `-0.0895` n `25`; metal avg `0.1251` n `20`; unknown avg `-0.158` n `782`
- 24h: commodity avg `-0.1097` n `12`; crypto_alt avg `0.533` n `230`; crypto_major avg `0.7436` n `8`; equity avg `-1.3195` n `108`; fx avg `-0.0322` n `6`; index avg `-0.223` n `25`; metal avg `0.7818` n `20`; unknown avg `0.7635` n `749`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
