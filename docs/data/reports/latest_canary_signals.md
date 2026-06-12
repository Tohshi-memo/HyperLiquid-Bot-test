# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T16:22:35.361761+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0455` n `12`; crypto_alt avg `0.1387` n `228`; crypto_major avg `0.2575` n `8`; equity avg `0.4723` n `74`; fx avg `-0.0178` n `6`; index avg `0.1445` n `23`; metal avg `0.3607` n `18`; unknown avg `-0.0786` n `643`
- 1h: commodity avg `0.2885` n `12`; crypto_alt avg `-0.8749` n `228`; crypto_major avg `-0.912` n `8`; equity avg `-0.8215` n `74`; fx avg `0.0003` n `6`; index avg `-0.2898` n `23`; metal avg `0.1506` n `18`; unknown avg `0.1501` n `643`
- 4h: commodity avg `0.1269` n `12`; crypto_alt avg `-0.6642` n `228`; crypto_major avg `0.1556` n `8`; equity avg `-0.6451` n `74`; fx avg `-0.011` n `6`; index avg `0.1798` n `23`; metal avg `0.4135` n `18`; unknown avg `25.9879` n `643`
- 24h: commodity avg `-2.2559` n `12`; crypto_alt avg `1.5063` n `228`; crypto_major avg `2.5629` n `8`; equity avg `1.9322` n `74`; fx avg `0.0873` n `6`; index avg `1.6542` n `23`; metal avg `2.8623` n `18`; unknown avg `40.7004` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
