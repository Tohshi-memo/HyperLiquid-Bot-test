# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T02:22:31.346102+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0108` n `12`; crypto_alt avg `0.1731` n `230`; crypto_major avg `0.1934` n `8`; equity avg `0.055` n `96`; fx avg `-0.0058` n `6`; index avg `0.0017` n `25`; metal avg `-0.022` n `20`; unknown avg `-0.0992` n `769`
- 1h: commodity avg `0.0645` n `12`; crypto_alt avg `-0.0283` n `230`; crypto_major avg `0.1573` n `8`; equity avg `0.0316` n `96`; fx avg `-0.0314` n `6`; index avg `0.0278` n `25`; metal avg `-0.0283` n `20`; unknown avg `-0.2438` n `769`
- 4h: commodity avg `0.0342` n `12`; crypto_alt avg `0.1678` n `230`; crypto_major avg `0.2202` n `8`; equity avg `0.2169` n `96`; fx avg `0.0013` n `6`; index avg `0.0457` n `25`; metal avg `0.0348` n `20`; unknown avg `-0.3546` n `769`
- 24h: commodity avg `0.7171` n `12`; crypto_alt avg `-0.0164` n `230`; crypto_major avg `-0.0067` n `8`; equity avg `0.5526` n `94`; fx avg `0.0624` n `6`; index avg `-0.0074` n `25`; metal avg `0.1507` n `20`; unknown avg `0.233` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
