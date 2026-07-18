# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T10:37:24.299941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0463` n `12`; crypto_alt avg `0.0451` n `230`; crypto_major avg `0.0265` n `8`; equity avg `-0.0109` n `96`; fx avg `-0.008` n `6`; index avg `0.0061` n `25`; metal avg `0.004` n `20`; unknown avg `-0.002` n `769`
- 1h: commodity avg `0.1251` n `12`; crypto_alt avg `0.2313` n `230`; crypto_major avg `0.1372` n `8`; equity avg `-0.0118` n `96`; fx avg `-0.0012` n `6`; index avg `0.0318` n `25`; metal avg `0.005` n `20`; unknown avg `-0.0311` n `769`
- 4h: commodity avg `0.1699` n `12`; crypto_alt avg `-0.1827` n `230`; crypto_major avg `-0.0035` n `8`; equity avg `-0.0551` n `96`; fx avg `0.0074` n `6`; index avg `0.0475` n `25`; metal avg `0.0309` n `20`; unknown avg `-0.1472` n `769`
- 24h: commodity avg `0.7733` n `12`; crypto_alt avg `-0.62` n `230`; crypto_major avg `0.0518` n `8`; equity avg `0.297` n `96`; fx avg `0.028` n `6`; index avg `0.1214` n `25`; metal avg `0.2128` n `20`; unknown avg `0.2034` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
