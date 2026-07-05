# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T06:52:27.740430+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0165` n `12`; crypto_alt avg `0.0718` n `229`; crypto_major avg `0.0325` n `8`; equity avg `0.0049` n `88`; fx avg `0.0016` n `6`; index avg `-0.0075` n `25`; metal avg `-0.0055` n `20`; unknown avg `0.0002` n `765`
- 1h: commodity avg `0.0088` n `12`; crypto_alt avg `0.0288` n `229`; crypto_major avg `0.0762` n `8`; equity avg `-0.0181` n `88`; fx avg `0.0097` n `6`; index avg `0.0015` n `25`; metal avg `0.0023` n `20`; unknown avg `-0.0524` n `731`
- 4h: commodity avg `-0.0108` n `12`; crypto_alt avg `0.0247` n `229`; crypto_major avg `0.2754` n `8`; equity avg `0.1268` n `88`; fx avg `0.0074` n `6`; index avg `0.0231` n `25`; metal avg `0.0115` n `20`; unknown avg `0.0004` n `731`
- 24h: commodity avg `0.0678` n `12`; crypto_alt avg `-0.7879` n `229`; crypto_major avg `-0.753` n `8`; equity avg `0.1592` n `88`; fx avg `0.0159` n `6`; index avg `0.0396` n `25`; metal avg `0.0657` n `20`; unknown avg `-1.1992` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
