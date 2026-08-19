# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T07:37:29.974104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0762` n `12`; crypto_alt avg `0.029` n `230`; crypto_major avg `0.0392` n `8`; equity avg `0.1316` n `120`; fx avg `-0.0039` n `6`; index avg `0.0127` n `25`; metal avg `0.0532` n `20`; unknown avg `-0.0067` n `789`
- 1h: commodity avg `-0.0679` n `12`; crypto_alt avg `0.1171` n `230`; crypto_major avg `0.1939` n `8`; equity avg `1.2539` n `120`; fx avg `0.0183` n `6`; index avg `0.1709` n `25`; metal avg `0.0585` n `20`; unknown avg `0.0198` n `789`
- 4h: commodity avg `-0.0474` n `12`; crypto_alt avg `0.0675` n `230`; crypto_major avg `0.1596` n `8`; equity avg `0.4643` n `120`; fx avg `-0.0023` n `6`; index avg `0.0913` n `25`; metal avg `-0.0134` n `20`; unknown avg `-0.069` n `757`
- 24h: commodity avg `0.3019` n `12`; crypto_alt avg `0.3165` n `230`; crypto_major avg `0.0934` n `8`; equity avg `-2.3628` n `120`; fx avg `-0.1488` n `6`; index avg `-0.3151` n `25`; metal avg `-0.5372` n `20`; unknown avg `-0.2766` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
