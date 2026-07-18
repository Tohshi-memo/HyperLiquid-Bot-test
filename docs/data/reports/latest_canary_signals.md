# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T04:52:29.748842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0137` n `12`; crypto_alt avg `0.0293` n `230`; crypto_major avg `-0.0162` n `8`; equity avg `-0.0181` n `96`; fx avg `0.0033` n `6`; index avg `-0.0007` n `25`; metal avg `0.0003` n `20`; unknown avg `0.0134` n `769`
- 1h: commodity avg `-0.033` n `12`; crypto_alt avg `-0.2388` n `230`; crypto_major avg `-0.1049` n `8`; equity avg `-0.0869` n `96`; fx avg `0.0082` n `6`; index avg `0.0181` n `25`; metal avg `0.0018` n `20`; unknown avg `0.4855` n `769`
- 4h: commodity avg `-0.0472` n `12`; crypto_alt avg `-0.363` n `230`; crypto_major avg `-0.104` n `8`; equity avg `0.0113` n `96`; fx avg `-0.0033` n `6`; index avg `0.0574` n `25`; metal avg `-0.0115` n `20`; unknown avg `-0.3212` n `769`
- 24h: commodity avg `0.6703` n `12`; crypto_alt avg `-0.7673` n `230`; crypto_major avg `-0.2977` n `8`; equity avg `0.7593` n `96`; fx avg `0.0597` n `6`; index avg `0.1606` n `25`; metal avg `0.2327` n `20`; unknown avg `0.2052` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
