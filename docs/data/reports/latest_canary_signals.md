# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T18:37:29.311968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0203` n `12`; crypto_alt avg `-0.027` n `230`; crypto_major avg `-0.0217` n `8`; equity avg `-0.0084` n `96`; fx avg `-0.0209` n `6`; index avg `-0.0115` n `25`; metal avg `0.0139` n `20`; unknown avg `0.0546` n `770`
- 1h: commodity avg `0.1198` n `12`; crypto_alt avg `-0.0001` n `230`; crypto_major avg `0.1156` n `8`; equity avg `0.0087` n `96`; fx avg `-0.0375` n `6`; index avg `-0.021` n `25`; metal avg `-0.0142` n `20`; unknown avg `0.0931` n `770`
- 4h: commodity avg `0.2031` n `12`; crypto_alt avg `0.2381` n `230`; crypto_major avg `0.3259` n `8`; equity avg `-0.0352` n `96`; fx avg `-0.0935` n `6`; index avg `-0.0352` n `25`; metal avg `-0.0303` n `20`; unknown avg `0.0512` n `770`
- 24h: commodity avg `0.3824` n `12`; crypto_alt avg `-0.6973` n `230`; crypto_major avg `0.2938` n `8`; equity avg `-0.8033` n `96`; fx avg `-0.155` n `6`; index avg `-0.0704` n `25`; metal avg `-0.0272` n `20`; unknown avg `-0.1096` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
