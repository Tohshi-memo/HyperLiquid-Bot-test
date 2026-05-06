# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T21:51:54.211858+00:00`
- Correlation status: `ready`
- Asset price records: `491`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.92` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0248` n `12`; crypto_alt avg `0.1385` n `228`; crypto_major avg `0.0361` n `8`; equity avg `-0.144` n `65`; fx avg `0.0152` n `4`; index avg `-0.033` n `23`; metal avg `-0.0181` n `18`; unknown avg `-0.0565` n `356`
- 1h: commodity avg `0.0994` n `12`; crypto_alt avg `0.872` n `228`; crypto_major avg `0.4132` n `8`; equity avg `-0.3973` n `65`; fx avg `-0.013` n `4`; index avg `-0.0507` n `23`; metal avg `0.0777` n `18`; unknown avg `0.1121` n `356`
- 4h: commodity avg `0.2557` n `12`; crypto_alt avg `0.7407` n `228`; crypto_major avg `0.3012` n `8`; equity avg `0.0204` n `65`; fx avg `-0.044` n `4`; index avg `0.2091` n `23`; metal avg `0.3559` n `18`; unknown avg `0.1381` n `356`
- 24h: commodity avg `-2.2857` n `7`; crypto_alt avg `2.514` n `223`; crypto_major avg `0.532` n `7`; equity avg `1.9321` n `47`; fx avg `-0.5756` n `4`; index avg `1.384` n `6`; metal avg `3.3843` n `7`; unknown avg `3.7325` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1321`, n `487`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1184`, n `487`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1022`, n `483`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0998`, n `483`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0923`, n `483`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0874`, n `483`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.079`, n `483`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0742`, n `487`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0643`, n `487`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.062`, n `483`, weak_sample_signal
