# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T21:37:31.345339+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0288` n `12`; crypto_alt avg `0.0166` n `230`; crypto_major avg `0.0485` n `8`; equity avg `0.0631` n `94`; fx avg `-0.0134` n `6`; index avg `0.0085` n `25`; metal avg `0.009` n `20`; unknown avg `0.0623` n `768`
- 1h: commodity avg `0.041` n `12`; crypto_alt avg `0.1242` n `230`; crypto_major avg `0.0922` n `8`; equity avg `0.0941` n `94`; fx avg `-0.0132` n `6`; index avg `0.0416` n `25`; metal avg `0.0277` n `20`; unknown avg `0.0678` n `768`
- 4h: commodity avg `0.1974` n `12`; crypto_alt avg `-0.0823` n `230`; crypto_major avg `-0.0527` n `8`; equity avg `-0.2349` n `94`; fx avg `-0.0155` n `6`; index avg `-0.0478` n `25`; metal avg `-0.0702` n `20`; unknown avg `-0.2841` n `768`
- 24h: commodity avg `-0.2342` n `12`; crypto_alt avg `-0.8637` n `230`; crypto_major avg `-1.8846` n `8`; equity avg `-3.6713` n `94`; fx avg `-0.1836` n `6`; index avg `-0.4889` n `25`; metal avg `-0.8254` n `20`; unknown avg `-0.3671` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
