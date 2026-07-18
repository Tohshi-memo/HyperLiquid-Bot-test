# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T13:37:23.718722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.019` n `12`; crypto_alt avg `0.0281` n `230`; crypto_major avg `0.1214` n `8`; equity avg `0.043` n `96`; fx avg `-0.0036` n `6`; index avg `-0.0003` n `25`; metal avg `0.0032` n `20`; unknown avg `-0.0197` n `770`
- 1h: commodity avg `0.0102` n `12`; crypto_alt avg `-0.2565` n `230`; crypto_major avg `-0.1524` n `8`; equity avg `-0.0183` n `96`; fx avg `-0.0012` n `6`; index avg `0.0035` n `25`; metal avg `-0.004` n `20`; unknown avg `-0.0334` n `770`
- 4h: commodity avg `0.1054` n `12`; crypto_alt avg `-0.0623` n `230`; crypto_major avg `0.0051` n `8`; equity avg `-0.1132` n `96`; fx avg `-0.0032` n `6`; index avg `0.0034` n `25`; metal avg `-0.0177` n `20`; unknown avg `-0.0905` n `769`
- 24h: commodity avg `0.4726` n `12`; crypto_alt avg `0.3464` n `230`; crypto_major avg `1.271` n `8`; equity avg `2.0533` n `96`; fx avg `0.0164` n `6`; index avg `0.3679` n `25`; metal avg `0.4238` n `20`; unknown avg `0.0877` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
