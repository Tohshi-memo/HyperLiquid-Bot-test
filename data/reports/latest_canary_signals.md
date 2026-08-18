# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T18:37:34.137446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0131` n `12`; crypto_alt avg `0.062` n `230`; crypto_major avg `0.047` n `8`; equity avg `0.1186` n `120`; fx avg `0.003` n `6`; index avg `0.0045` n `25`; metal avg `0.0245` n `20`; unknown avg `0.0093` n `789`
- 1h: commodity avg `0.0114` n `12`; crypto_alt avg `-0.0329` n `230`; crypto_major avg `0.1842` n `8`; equity avg `-0.0416` n `120`; fx avg `0.0168` n `6`; index avg `-0.0038` n `25`; metal avg `-0.0245` n `20`; unknown avg `-0.0627` n `789`
- 4h: commodity avg `0.2063` n `12`; crypto_alt avg `-0.111` n `230`; crypto_major avg `-0.006` n `8`; equity avg `-0.9384` n `120`; fx avg `0.0116` n `6`; index avg `-0.1358` n `25`; metal avg `-0.2352` n `20`; unknown avg `3.0265` n `789`
- 24h: commodity avg `0.3294` n `12`; crypto_alt avg `-0.5437` n `230`; crypto_major avg `0.1576` n `8`; equity avg `-4.4631` n `120`; fx avg `-0.0287` n `6`; index avg `-0.681` n `25`; metal avg `-0.5937` n `20`; unknown avg `-0.2695` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
