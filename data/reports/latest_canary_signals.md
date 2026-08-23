# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T21:22:23.742118+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `0.4513` n `231`; crypto_major avg `0.4795` n `8`; equity avg `0.0603` n `122`; fx avg `-0.0313` n `6`; index avg `0.003` n `25`; metal avg `0.0039` n `20`; unknown avg `0.179` n `793`
- 1h: commodity avg `-0.012` n `12`; crypto_alt avg `0.91` n `231`; crypto_major avg `0.9133` n `8`; equity avg `0.0755` n `122`; fx avg `-0.0481` n `6`; index avg `0.0026` n `25`; metal avg `0.0303` n `20`; unknown avg `1.547` n `793`
- 4h: commodity avg `-0.0862` n `12`; crypto_alt avg `0.8543` n `231`; crypto_major avg `0.7763` n `8`; equity avg `0.2635` n `122`; fx avg `-0.1077` n `6`; index avg `0.0402` n `25`; metal avg `0.0604` n `20`; unknown avg `3.5857` n `793`
- 24h: commodity avg `-0.1297` n `12`; crypto_alt avg `3.9642` n `231`; crypto_major avg `1.7081` n `8`; equity avg `0.8442` n `122`; fx avg `-0.1221` n `6`; index avg `0.1313` n `25`; metal avg `0.1217` n `20`; unknown avg `9.0371` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
