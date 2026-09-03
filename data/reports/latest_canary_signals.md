# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T09:22:30.556525+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0182` n `12`; crypto_alt avg `0.0868` n `232`; crypto_major avg `-0.0331` n `8`; equity avg `-0.1459` n `133`; fx avg `-0.021` n `6`; index avg `-0.0107` n `26`; metal avg `-0.0337` n `20`; unknown avg `0.019` n `792`
- 1h: commodity avg `0.1644` n `12`; crypto_alt avg `0.048` n `232`; crypto_major avg `-0.0166` n `8`; equity avg `-0.2241` n `133`; fx avg `-0.0302` n `6`; index avg `-0.0276` n `26`; metal avg `-0.0106` n `20`; unknown avg `-0.0932` n `790`
- 4h: commodity avg `0.1402` n `12`; crypto_alt avg `0.8249` n `232`; crypto_major avg `0.7457` n `8`; equity avg `0.367` n `133`; fx avg `-0.1282` n `6`; index avg `0.0954` n `26`; metal avg `0.1633` n `20`; unknown avg `16.2774` n `754`
- 24h: commodity avg `0.2701` n `12`; crypto_alt avg `1.4234` n `232`; crypto_major avg `1.5125` n `8`; equity avg `1.6014` n `133`; fx avg `-0.3874` n `6`; index avg `0.1973` n `26`; metal avg `0.9004` n `20`; unknown avg `-0.1517` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0454`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0394`, n `668`, weak_sample_signal
