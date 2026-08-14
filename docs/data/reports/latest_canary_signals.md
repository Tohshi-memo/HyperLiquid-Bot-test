# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T12:02:05.810226+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0823` n `12`; crypto_alt avg `-0.0645` n `230`; crypto_major avg `-0.0961` n `8`; equity avg `-0.0952` n `113`; fx avg `-0.0058` n `6`; index avg `-0.0036` n `25`; metal avg `0.0279` n `20`; unknown avg `0.0264` n `787`
- 1h: commodity avg `0.0339` n `12`; crypto_alt avg `0.0475` n `230`; crypto_major avg `-0.0115` n `8`; equity avg `-0.0684` n `113`; fx avg `0.0102` n `6`; index avg `-0.005` n `25`; metal avg `0.1496` n `20`; unknown avg `-0.0348` n `787`
- 4h: commodity avg `-0.2169` n `12`; crypto_alt avg `-0.0849` n `230`; crypto_major avg `-0.237` n `8`; equity avg `0.2766` n `113`; fx avg `0.0163` n `6`; index avg `0.0571` n `25`; metal avg `0.1877` n `20`; unknown avg `2.8831` n `787`
- 24h: commodity avg `-0.0008` n `12`; crypto_alt avg `-0.7039` n `230`; crypto_major avg `-0.6646` n `8`; equity avg `1.9603` n `113`; fx avg `-0.0291` n `6`; index avg `0.3679` n `25`; metal avg `-0.115` n `20`; unknown avg `0.9245` n `755`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1867`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1755`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1692`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1672`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.154`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
