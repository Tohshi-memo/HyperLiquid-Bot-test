# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T04:22:29.230056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0114` n `12`; crypto_alt avg `-0.0384` n `234`; crypto_major avg `0.4048` n `8`; equity avg `0.096` n `140`; fx avg `-0.0108` n `6`; index avg `0.0157` n `26`; metal avg `0.0181` n `20`; unknown avg `-0.0727` n `945`
- 1h: commodity avg `-0.1034` n `12`; crypto_alt avg `-0.0406` n `234`; crypto_major avg `0.5496` n `8`; equity avg `0.2185` n `140`; fx avg `-0.0079` n `6`; index avg `0.0373` n `26`; metal avg `0.0571` n `20`; unknown avg `1.7966` n `937`
- 4h: commodity avg `-0.1961` n `12`; crypto_alt avg `0.2911` n `234`; crypto_major avg `0.9409` n `8`; equity avg `-0.1794` n `140`; fx avg `-0.0098` n `6`; index avg `-0.0473` n `26`; metal avg `-0.2188` n `20`; unknown avg `6.0541` n `937`
- 24h: commodity avg `-0.1915` n `12`; crypto_alt avg `3.6746` n `234`; crypto_major avg `2.2361` n `8`; equity avg `0.8735` n `140`; fx avg `-0.2066` n `6`; index avg `0.0727` n `26`; metal avg `0.1736` n `20`; unknown avg `1.606` n `836`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
