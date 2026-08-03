# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T23:07:44.287385+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1036` n `12`; crypto_alt avg `-0.0447` n `230`; crypto_major avg `-0.0876` n `8`; equity avg `-0.0359` n `104`; fx avg `-0.0044` n `6`; index avg `-0.0174` n `25`; metal avg `0.0117` n `20`; unknown avg `-0.0156` n `783`
- 1h: commodity avg `0.0522` n `12`; crypto_alt avg `-0.0571` n `230`; crypto_major avg `-0.0286` n `8`; equity avg `0.0795` n `104`; fx avg `-0.0078` n `6`; index avg `0.0052` n `25`; metal avg `0.0255` n `20`; unknown avg `-0.0717` n `783`
- 4h: commodity avg `-0.0255` n `12`; crypto_alt avg `-0.2973` n `230`; crypto_major avg `-0.496` n `8`; equity avg `0.4877` n `104`; fx avg `0.0524` n `6`; index avg `0.07` n `25`; metal avg `0.0587` n `20`; unknown avg `0.2073` n `783`
- 24h: commodity avg `-0.0529` n `12`; crypto_alt avg `0.2948` n `230`; crypto_major avg `0.0312` n `8`; equity avg `2.0396` n `104`; fx avg `-0.2589` n `6`; index avg `0.074` n `25`; metal avg `-0.2488` n `20`; unknown avg `0.026` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
