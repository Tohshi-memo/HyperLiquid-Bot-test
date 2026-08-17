# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T12:14:22.873425+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0024` n `12`; crypto_alt avg `-0.1195` n `230`; crypto_major avg `-0.0553` n `8`; equity avg `-0.0585` n `114`; fx avg `0.0013` n `6`; index avg `-0.0136` n `25`; metal avg `-0.0343` n `20`; unknown avg `-0.0156` n `792`
- 1h: commodity avg `-0.0582` n `12`; crypto_alt avg `-0.0663` n `230`; crypto_major avg `-0.1845` n `8`; equity avg `-0.2004` n `114`; fx avg `0.0058` n `6`; index avg `-0.0189` n `25`; metal avg `-0.0698` n `20`; unknown avg `0.0238` n `792`
- 4h: commodity avg `0.0561` n `12`; crypto_alt avg `-0.0219` n `230`; crypto_major avg `0.0865` n `8`; equity avg `-0.1596` n `114`; fx avg `0.0137` n `6`; index avg `-0.0177` n `25`; metal avg `-0.0674` n `20`; unknown avg `0.0192` n `792`
- 24h: commodity avg `-0.134` n `12`; crypto_alt avg `-0.001` n `230`; crypto_major avg `0.8414` n `8`; equity avg `1.0805` n `114`; fx avg `-0.0123` n `6`; index avg `0.1332` n `25`; metal avg `0.1245` n `20`; unknown avg `0.0289` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
