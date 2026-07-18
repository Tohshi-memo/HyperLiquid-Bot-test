# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T08:07:29.720022+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `12`; crypto_alt avg `-0.0304` n `230`; crypto_major avg `-0.053` n `8`; equity avg `-0.0365` n `96`; fx avg `0.0099` n `6`; index avg `0.0212` n `25`; metal avg `0.0036` n `20`; unknown avg `0.0301` n `769`
- 1h: commodity avg `-0.0336` n `12`; crypto_alt avg `0.0004` n `230`; crypto_major avg `0.1015` n `8`; equity avg `0.0373` n `96`; fx avg `0.0112` n `6`; index avg `0.019` n `25`; metal avg `0.022` n `20`; unknown avg `-0.1008` n `769`
- 4h: commodity avg `0.0446` n `12`; crypto_alt avg `-0.4287` n `230`; crypto_major avg `-0.2137` n `8`; equity avg `-0.148` n `96`; fx avg `0.0005` n `6`; index avg `-0.014` n `25`; metal avg `0.0208` n `20`; unknown avg `-0.1013` n `737`
- 24h: commodity avg `0.8416` n `12`; crypto_alt avg `-0.0671` n `230`; crypto_major avg `0.5932` n `8`; equity avg `1.2678` n `96`; fx avg `0.0321` n `6`; index avg `0.1614` n `25`; metal avg `0.2086` n `20`; unknown avg `0.263` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
