# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T12:22:30.276849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0026` n `12`; crypto_alt avg `-0.0013` n `233`; crypto_major avg `-0.0313` n `8`; equity avg `-0.1062` n `134`; fx avg `0.0257` n `6`; index avg `-0.0019` n `26`; metal avg `-0.0986` n `20`; unknown avg `0.1711` n `797`
- 1h: commodity avg `0.3318` n `12`; crypto_alt avg `-0.3589` n `233`; crypto_major avg `-0.2668` n `8`; equity avg `-0.4773` n `134`; fx avg `0.016` n `6`; index avg `-0.0833` n `26`; metal avg `-0.1586` n `20`; unknown avg `0.0316` n `795`
- 4h: commodity avg `0.4416` n `12`; crypto_alt avg `-0.4334` n `233`; crypto_major avg `-0.4561` n `8`; equity avg `-0.83` n `134`; fx avg `0.0465` n `6`; index avg `-0.1709` n `26`; metal avg `-0.7235` n `20`; unknown avg `0.3579` n `789`
- 24h: commodity avg `0.3251` n `12`; crypto_alt avg `-4.7005` n `233`; crypto_major avg `-3.407` n `8`; equity avg `-1.4028` n `134`; fx avg `0.1194` n `6`; index avg `-0.1212` n `26`; metal avg `-0.4709` n `20`; unknown avg `-0.8947` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
