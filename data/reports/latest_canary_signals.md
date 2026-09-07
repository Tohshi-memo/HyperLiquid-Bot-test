# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T19:37:26.612687+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.013` n `12`; crypto_alt avg `0.2828` n `232`; crypto_major avg `0.218` n `8`; equity avg `0.0352` n `134`; fx avg `-0.0003` n `6`; index avg `0.0044` n `26`; metal avg `-0.0019` n `20`; unknown avg `0.1882` n `796`
- 1h: commodity avg `-0.0062` n `12`; crypto_alt avg `0.5567` n `232`; crypto_major avg `0.4397` n `8`; equity avg `0.0719` n `134`; fx avg `-0.0041` n `6`; index avg `0.0131` n `26`; metal avg `0.0124` n `20`; unknown avg `0.8523` n `794`
- 4h: commodity avg `-0.0872` n `12`; crypto_alt avg `0.9108` n `232`; crypto_major avg `0.7788` n `8`; equity avg `0.2679` n `134`; fx avg `-0.0245` n `6`; index avg `0.0597` n `26`; metal avg `0.0168` n `20`; unknown avg `0.2645` n `768`
- 24h: commodity avg `0.1692` n `12`; crypto_alt avg `0.6215` n `232`; crypto_major avg `-0.5492` n `8`; equity avg `0.4499` n `134`; fx avg `-0.1312` n `6`; index avg `0.0941` n `26`; metal avg `-0.0053` n `20`; unknown avg `0.559` n `661`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
