# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T21:37:27.472128+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0186` n `12`; crypto_alt avg `0.1628` n `229`; crypto_major avg `0.1317` n `8`; equity avg `0.0069` n `92`; fx avg `-0.0005` n `6`; index avg `-0.0009` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.102` n `765`
- 1h: commodity avg `-0.0097` n `12`; crypto_alt avg `0.3365` n `229`; crypto_major avg `0.1379` n `8`; equity avg `0.0331` n `92`; fx avg `0.0122` n `6`; index avg `-0.0021` n `25`; metal avg `0.0265` n `20`; unknown avg `-0.253` n `765`
- 4h: commodity avg `0.0365` n `12`; crypto_alt avg `0.2217` n `229`; crypto_major avg `0.1594` n `8`; equity avg `-0.1559` n `92`; fx avg `-0.0147` n `6`; index avg `0.0012` n `25`; metal avg `0.0716` n `20`; unknown avg `-0.442` n `765`
- 24h: commodity avg `-0.2936` n `12`; crypto_alt avg `0.9871` n `229`; crypto_major avg `0.8958` n `8`; equity avg `-0.632` n `92`; fx avg `-0.1778` n `6`; index avg `0.0432` n `25`; metal avg `0.1516` n `20`; unknown avg `-0.2682` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
