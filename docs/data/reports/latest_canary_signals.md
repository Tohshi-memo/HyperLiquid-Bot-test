# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T15:07:31.079818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0686` n `12`; crypto_alt avg `0.2147` n `230`; crypto_major avg `0.1775` n `8`; equity avg `0.0206` n `121`; fx avg `-0.0045` n `6`; index avg `0.0246` n `25`; metal avg `0.0289` n `20`; unknown avg `-0.0568` n `793`
- 1h: commodity avg `-0.0214` n `12`; crypto_alt avg `0.7067` n `230`; crypto_major avg `0.6811` n `8`; equity avg `-0.3372` n `121`; fx avg `-0.0181` n `6`; index avg `0.01` n `25`; metal avg `-0.0643` n `20`; unknown avg `-0.1128` n `793`
- 4h: commodity avg `-0.1605` n `12`; crypto_alt avg `1.602` n `230`; crypto_major avg `0.4833` n `8`; equity avg `-0.5709` n `121`; fx avg `-0.0317` n `6`; index avg `-0.061` n `25`; metal avg `-0.0961` n `20`; unknown avg `0.171` n `793`
- 24h: commodity avg `0.189` n `12`; crypto_alt avg `8.1065` n `230`; crypto_major avg `6.2377` n `8`; equity avg `0.685` n `121`; fx avg `-0.0863` n `6`; index avg `0.01` n `25`; metal avg `0.4618` n `20`; unknown avg `2.529` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2372`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1955`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1939`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
