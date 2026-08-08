# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T00:37:50.618026+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `-0.0251` n `230`; crypto_major avg `-0.0275` n `8`; equity avg `0.0151` n `112`; fx avg `-0.002` n `6`; index avg `0.0115` n `25`; metal avg `-0.0029` n `20`; unknown avg `-0.0961` n `783`
- 1h: commodity avg `-0.0447` n `12`; crypto_alt avg `0.0332` n `230`; crypto_major avg `-0.0249` n `8`; equity avg `0.0957` n `112`; fx avg `-0.0014` n `6`; index avg `0.0014` n `25`; metal avg `0.0415` n `20`; unknown avg `-0.1487` n `783`
- 4h: commodity avg `-0.108` n `12`; crypto_alt avg `-0.0964` n `230`; crypto_major avg `-0.2132` n `8`; equity avg `0.1628` n `112`; fx avg `0.0253` n `6`; index avg `-0.015` n `25`; metal avg `0.1552` n `20`; unknown avg `-0.2617` n `782`
- 24h: commodity avg `-0.2645` n `12`; crypto_alt avg `-0.5879` n `230`; crypto_major avg `-0.1292` n `8`; equity avg `1.9939` n `112`; fx avg `-0.1144` n `6`; index avg `0.1266` n `25`; metal avg `0.548` n `20`; unknown avg `0.0049` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
