# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T20:07:31.796809+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0715` n `12`; crypto_alt avg `-0.1385` n `230`; crypto_major avg `-0.2484` n `8`; equity avg `-0.4278` n `96`; fx avg `-0.0148` n `6`; index avg `-0.0861` n `25`; metal avg `-0.0121` n `20`; unknown avg `0.1174` n `769`
- 1h: commodity avg `0.0819` n `12`; crypto_alt avg `-0.4427` n `230`; crypto_major avg `-0.1976` n `8`; equity avg `-0.4889` n `96`; fx avg `-0.004` n `6`; index avg `-0.076` n `25`; metal avg `0.0397` n `20`; unknown avg `-0.0251` n `769`
- 4h: commodity avg `0.1546` n `12`; crypto_alt avg `-0.0552` n `230`; crypto_major avg `0.3666` n `8`; equity avg `-0.612` n `96`; fx avg `0.0108` n `6`; index avg `-0.115` n `25`; metal avg `0.0094` n `20`; unknown avg `0.4898` n `769`
- 24h: commodity avg `0.7465` n `12`; crypto_alt avg `-1.2196` n `230`; crypto_major avg `-1.2663` n `8`; equity avg `-1.5322` n `94`; fx avg `0.0957` n `6`; index avg `-0.2774` n `25`; metal avg `-0.0028` n `20`; unknown avg `-0.0462` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
