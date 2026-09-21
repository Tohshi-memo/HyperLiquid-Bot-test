# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T01:52:31.103152+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `-0.5304` n `234`; crypto_major avg `-0.535` n `8`; equity avg `-0.1848` n `140`; fx avg `-0.0018` n `6`; index avg `-0.0053` n `26`; metal avg `-0.015` n `20`; unknown avg `2.5684` n `944`
- 1h: commodity avg `-0.1504` n `12`; crypto_alt avg `-0.9081` n `234`; crypto_major avg `-0.9334` n `8`; equity avg `-0.0454` n `140`; fx avg `0.0073` n `6`; index avg `0.0161` n `26`; metal avg `0.0871` n `20`; unknown avg `4.1395` n `941`
- 4h: commodity avg `-0.7096` n `12`; crypto_alt avg `0.1219` n `234`; crypto_major avg `0.8824` n `8`; equity avg `0.7852` n `140`; fx avg `0.0543` n `6`; index avg `0.1449` n `26`; metal avg `0.146` n `20`; unknown avg `4.3061` n `907`
- 24h: commodity avg `-0.576` n `12`; crypto_alt avg `0.887` n `234`; crypto_major avg `1.06` n `8`; equity avg `0.645` n `140`; fx avg `0.016` n `6`; index avg `0.119` n `26`; metal avg `0.0764` n `20`; unknown avg `3.6526` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
