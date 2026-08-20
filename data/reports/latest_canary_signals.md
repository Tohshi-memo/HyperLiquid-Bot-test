# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T06:52:28.438723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0381` n `12`; crypto_alt avg `0.1067` n `230`; crypto_major avg `0.1693` n `8`; equity avg `0.1697` n `121`; fx avg `0.0107` n `6`; index avg `0.015` n `25`; metal avg `-0.0402` n `20`; unknown avg `0.0988` n `792`
- 1h: commodity avg `0.0082` n `12`; crypto_alt avg `0.5309` n `230`; crypto_major avg `0.7246` n `8`; equity avg `0.3838` n `121`; fx avg `-0.0307` n `6`; index avg `0.069` n `25`; metal avg `0.0686` n `20`; unknown avg `0.292` n `776`
- 4h: commodity avg `0.0323` n `12`; crypto_alt avg `0.4782` n `230`; crypto_major avg `0.8325` n `8`; equity avg `0.3501` n `121`; fx avg `0.0015` n `6`; index avg `0.0594` n `25`; metal avg `-0.018` n `20`; unknown avg `0.2376` n `776`
- 24h: commodity avg `-0.0255` n `12`; crypto_alt avg `5.8238` n `230`; crypto_major avg `10.5588` n `8`; equity avg `1.4156` n `120`; fx avg `0.0514` n `6`; index avg `0.2645` n `25`; metal avg `1.0261` n `20`; unknown avg `1.9506` n `773`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1969`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
