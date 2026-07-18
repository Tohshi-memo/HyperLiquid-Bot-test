# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T12:09:08.090116+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `12`; crypto_alt avg `0.1758` n `230`; crypto_major avg `0.1724` n `8`; equity avg `0.0261` n `96`; fx avg `-0.001` n `6`; index avg `-0.0083` n `25`; metal avg `-0.0081` n `20`; unknown avg `0.0398` n `770`
- 1h: commodity avg `-0.0193` n `12`; crypto_alt avg `0.2188` n `230`; crypto_major avg `0.1445` n `8`; equity avg `0.0195` n `96`; fx avg `0.0005` n `6`; index avg `-0.005` n `25`; metal avg `-0.0116` n `20`; unknown avg `0.0235` n `770`
- 4h: commodity avg `0.1403` n `12`; crypto_alt avg `0.0952` n `230`; crypto_major avg `0.1331` n `8`; equity avg `-0.0635` n `96`; fx avg `-0.0122` n `6`; index avg `0.036` n `25`; metal avg `-0.013` n `20`; unknown avg `-0.0237` n `769`
- 24h: commodity avg `0.6447` n `12`; crypto_alt avg `-0.2734` n `230`; crypto_major avg `0.3579` n `8`; equity avg `0.9003` n `96`; fx avg `0.0319` n `6`; index avg `0.188` n `25`; metal avg `0.3323` n `20`; unknown avg `0.0734` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
