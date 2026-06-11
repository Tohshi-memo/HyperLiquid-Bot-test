# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T08:52:30.906591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0252` n `12`; crypto_alt avg `-0.2925` n `228`; crypto_major avg `-0.2043` n `8`; equity avg `-0.1021` n `74`; fx avg `-0.0173` n `6`; index avg `-0.0255` n `23`; metal avg `-0.1892` n `18`; unknown avg `-0.0075` n `556`
- 1h: commodity avg `-0.2801` n `12`; crypto_alt avg `0.5063` n `228`; crypto_major avg `0.5084` n `8`; equity avg `0.4464` n `74`; fx avg `-0.0491` n `6`; index avg `0.2347` n `23`; metal avg `-0.1333` n `18`; unknown avg `0.2788` n `556`
- 4h: commodity avg `-0.8321` n `12`; crypto_alt avg `-0.0543` n `228`; crypto_major avg `0.4772` n `8`; equity avg `0.7573` n `74`; fx avg `-0.0118` n `6`; index avg `0.3158` n `23`; metal avg `0.1582` n `18`; unknown avg `-0.0028` n `530`
- 24h: commodity avg `0.6191` n `12`; crypto_alt avg `1.6049` n `228`; crypto_major avg `1.8053` n `8`; equity avg `1.015` n `74`; fx avg `0.0329` n `6`; index avg `0.1849` n `23`; metal avg `-0.2303` n `18`; unknown avg `3.7437` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
