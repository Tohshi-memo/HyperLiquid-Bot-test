# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T10:22:25.414807+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.056` n `12`; crypto_alt avg `-0.0234` n `230`; crypto_major avg `-0.0006` n `8`; equity avg `0.1567` n `96`; fx avg `0.0156` n `6`; index avg `0.0313` n `25`; metal avg `-0.0119` n `20`; unknown avg `-0.0081` n `769`
- 1h: commodity avg `0.065` n `12`; crypto_alt avg `0.2753` n `230`; crypto_major avg `0.2889` n `8`; equity avg `0.9415` n `96`; fx avg `-0.0073` n `6`; index avg `0.1151` n `25`; metal avg `-0.021` n `20`; unknown avg `0.0679` n `769`
- 4h: commodity avg `0.3841` n `12`; crypto_alt avg `0.1697` n `230`; crypto_major avg `0.3912` n `8`; equity avg `0.3727` n `96`; fx avg `0.0209` n `6`; index avg `0.0131` n `25`; metal avg `-0.0502` n `20`; unknown avg `0.2039` n `768`
- 24h: commodity avg `0.0717` n `12`; crypto_alt avg `-1.3556` n `230`; crypto_major avg `-2.5555` n `8`; equity avg `-4.4992` n `94`; fx avg `-0.0134` n `6`; index avg `-0.6359` n `25`; metal avg `-0.6775` n `20`; unknown avg `-0.4461` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
