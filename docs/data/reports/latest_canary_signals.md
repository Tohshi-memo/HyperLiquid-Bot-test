# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T16:52:17.595811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2027` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `-0.0451` n `228`; crypto_major avg `0.0048` n `8`; equity avg `-0.0138` n `69`; fx avg `0.001` n `6`; index avg `0.0022` n `23`; metal avg `0.0364` n `18`; unknown avg `-0.0384` n `421`
- 1h: commodity avg `-0.0708` n `12`; crypto_alt avg `-0.6445` n `228`; crypto_major avg `-0.6042` n `8`; equity avg `-0.0949` n `69`; fx avg `0.0023` n `6`; index avg `0.0482` n `23`; metal avg `0.0246` n `18`; unknown avg `0.3055` n `421`
- 4h: commodity avg `0.0554` n `12`; crypto_alt avg `-1.632` n `228`; crypto_major avg `-1.0362` n `8`; equity avg `-0.0728` n `69`; fx avg `-0.0156` n `6`; index avg `0.1665` n `23`; metal avg `-0.0418` n `18`; unknown avg `-0.1459` n `421`
- 24h: commodity avg `0.5047` n `12`; crypto_alt avg `-1.6946` n `228`; crypto_major avg `-0.5982` n `8`; equity avg `0.8865` n `69`; fx avg `-0.0223` n `6`; index avg `0.0093` n `23`; metal avg `-0.1039` n `18`; unknown avg `-0.0041` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
