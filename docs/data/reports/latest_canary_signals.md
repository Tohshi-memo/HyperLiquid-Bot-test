# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T12:37:32.871089+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0683` n `12`; crypto_alt avg `-0.245` n `229`; crypto_major avg `-0.3302` n `8`; equity avg `-0.0305` n `91`; fx avg `0.0017` n `6`; index avg `-0.0063` n `25`; metal avg `-0.0432` n `20`; unknown avg `0.1407` n `763`
- 1h: commodity avg `-0.2718` n `12`; crypto_alt avg `0.2155` n `229`; crypto_major avg `0.4327` n `8`; equity avg `0.2962` n `91`; fx avg `-0.03` n `6`; index avg `0.115` n `25`; metal avg `0.1911` n `20`; unknown avg `0.2395` n `763`
- 4h: commodity avg `-0.3182` n `12`; crypto_alt avg `0.5368` n `229`; crypto_major avg `0.5461` n `8`; equity avg `-0.1167` n `91`; fx avg `-0.1187` n `6`; index avg `0.0055` n `25`; metal avg `0.3458` n `20`; unknown avg `0.2954` n `757`
- 24h: commodity avg `0.0968` n `12`; crypto_alt avg `1.5928` n `229`; crypto_major avg `1.0582` n `8`; equity avg `-1.2757` n `90`; fx avg `-0.1847` n `6`; index avg `-0.335` n `25`; metal avg `0.2286` n `20`; unknown avg `-0.2197` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0501`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0494`, n `668`, weak_sample_signal
