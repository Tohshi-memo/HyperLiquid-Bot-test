# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T00:16:11.178821+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0452` n `12`; crypto_alt avg `0.2073` n `228`; crypto_major avg `0.0715` n `8`; equity avg `-0.0017` n `77`; fx avg `-0.0062` n `6`; index avg `0.0562` n `23`; metal avg `-0.0261` n `18`; unknown avg `458.9214` n `687`
- 1h: commodity avg `-0.0677` n `12`; crypto_alt avg `0.839` n `228`; crypto_major avg `0.4803` n `8`; equity avg `0.0079` n `77`; fx avg `-0.0104` n `6`; index avg `0.1121` n `23`; metal avg `-0.0913` n `18`; unknown avg `1.1466` n `687`
- 4h: commodity avg `-0.1494` n `12`; crypto_alt avg `-0.2848` n `228`; crypto_major avg `-0.8569` n `8`; equity avg `-0.2039` n `77`; fx avg `0.012` n `6`; index avg `-0.0231` n `23`; metal avg `-0.1664` n `18`; unknown avg `0.2489` n `679`
- 24h: commodity avg `0.7279` n `12`; crypto_alt avg `1.26` n `228`; crypto_major avg `2.1821` n `8`; equity avg `1.2511` n `76`; fx avg `0.0541` n `6`; index avg `0.6738` n `23`; metal avg `-0.1446` n `18`; unknown avg `1.4581` n `519`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.044`, n `668`, weak_sample_signal
