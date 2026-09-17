# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T16:37:28.600860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.071` n `12`; crypto_alt avg `-0.096` n `234`; crypto_major avg `-0.3254` n `8`; equity avg `-0.0327` n `138`; fx avg `0.0104` n `6`; index avg `-0.0056` n `26`; metal avg `-0.0285` n `20`; unknown avg `-0.0278` n `913`
- 1h: commodity avg `0.0626` n `12`; crypto_alt avg `0.3711` n `234`; crypto_major avg `-0.1674` n `8`; equity avg `0.2226` n `138`; fx avg `0.0189` n `6`; index avg `0.016` n `26`; metal avg `0.0062` n `20`; unknown avg `0.2039` n `911`
- 4h: commodity avg `0.3486` n `12`; crypto_alt avg `0.5571` n `234`; crypto_major avg `-0.0718` n `8`; equity avg `0.2356` n `138`; fx avg `-0.0179` n `6`; index avg `0.0021` n `26`; metal avg `-0.0071` n `20`; unknown avg `1.0324` n `891`
- 24h: commodity avg `-0.1367` n `12`; crypto_alt avg `5.0498` n `234`; crypto_major avg `2.4634` n `8`; equity avg `1.8281` n `138`; fx avg `0.0326` n `6`; index avg `0.2527` n `26`; metal avg `0.192` n `20`; unknown avg `0.5024` n `711`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
