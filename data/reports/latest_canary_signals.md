# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T04:07:27.098290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0372` n `12`; crypto_alt avg `0.0088` n `230`; crypto_major avg `0.0747` n `8`; equity avg `0.0036` n `96`; fx avg `0.0115` n `6`; index avg `0.0137` n `25`; metal avg `-0.0043` n `20`; unknown avg `0.6374` n `769`
- 1h: commodity avg `-0.0815` n `12`; crypto_alt avg `-0.0403` n `230`; crypto_major avg `0.0033` n `8`; equity avg `-0.0083` n `96`; fx avg `0.012` n `6`; index avg `0.0235` n `25`; metal avg `-0.0044` n `20`; unknown avg `0.4429` n `769`
- 4h: commodity avg `-0.0994` n `12`; crypto_alt avg `-0.1126` n `230`; crypto_major avg `0.1013` n `8`; equity avg `0.1824` n `96`; fx avg `0.0043` n `6`; index avg `0.1068` n `25`; metal avg `-0.0198` n `20`; unknown avg `-0.2575` n `769`
- 24h: commodity avg `0.6904` n `12`; crypto_alt avg `-0.3941` n `230`; crypto_major avg `-0.0482` n `8`; equity avg `0.7621` n `96`; fx avg `0.0473` n `6`; index avg `0.087` n `25`; metal avg `0.1932` n `20`; unknown avg `0.2228` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
