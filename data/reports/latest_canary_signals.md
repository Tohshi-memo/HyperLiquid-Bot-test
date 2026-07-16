# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T21:41:30.667419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0184` n `12`; crypto_alt avg `0.0873` n `230`; crypto_major avg `0.0755` n `8`; equity avg `0.0501` n `94`; fx avg `-0.0073` n `6`; index avg `0.0129` n `25`; metal avg `0.013` n `20`; unknown avg `0.0407` n `768`
- 1h: commodity avg `0.0515` n `12`; crypto_alt avg `0.1957` n `230`; crypto_major avg `0.1192` n `8`; equity avg `0.0809` n `94`; fx avg `-0.007` n `6`; index avg `0.0461` n `25`; metal avg `0.0318` n `20`; unknown avg `0.0451` n `768`
- 4h: commodity avg `0.2078` n `12`; crypto_alt avg `-0.0095` n `230`; crypto_major avg `-0.0257` n `8`; equity avg `-0.2481` n `94`; fx avg `-0.0094` n `6`; index avg `-0.0434` n `25`; metal avg `-0.0662` n `20`; unknown avg `-0.2928` n `768`
- 24h: commodity avg `-0.2238` n `12`; crypto_alt avg `-0.7911` n `230`; crypto_major avg `-1.8582` n `8`; equity avg `-3.6839` n `94`; fx avg `-0.1775` n `6`; index avg `-0.4846` n `25`; metal avg `-0.8214` n `20`; unknown avg `-0.3602` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
