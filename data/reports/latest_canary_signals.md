# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T13:07:25.714650+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0154` n `12`; crypto_alt avg `-0.1181` n `230`; crypto_major avg `-0.2003` n `8`; equity avg `-0.0029` n `96`; fx avg `-0.0025` n `6`; index avg `0.0089` n `25`; metal avg `-0.0085` n `20`; unknown avg `-0.0179` n `770`
- 1h: commodity avg `0.0086` n `12`; crypto_alt avg `-0.313` n `230`; crypto_major avg `-0.2048` n `8`; equity avg `-0.0951` n `96`; fx avg `-0.0013` n `6`; index avg `-0.0079` n `25`; metal avg `-0.0063` n `20`; unknown avg `0.0095` n `770`
- 4h: commodity avg `0.1091` n `12`; crypto_alt avg `-0.0826` n `230`; crypto_major avg `-0.0257` n `8`; equity avg `-0.1364` n `96`; fx avg `-0.0099` n `6`; index avg `-0.0241` n `25`; metal avg `-0.0157` n `20`; unknown avg `-0.0605` n `769`
- 24h: commodity avg `0.4703` n `12`; crypto_alt avg `0.37` n `230`; crypto_major avg `1.0864` n `8`; equity avg `1.3587` n `96`; fx avg `0.0211` n `6`; index avg `0.2616` n `25`; metal avg `0.4055` n `20`; unknown avg `0.126` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
