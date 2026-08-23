# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T03:22:34.166982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.128` n `230`; crypto_major avg `-0.0555` n `8`; equity avg `0.0039` n `121`; fx avg `0.0047` n `6`; index avg `-0.0004` n `25`; metal avg `-0.0021` n `20`; unknown avg `-0.0343` n `794`
- 1h: commodity avg `-0.0278` n `12`; crypto_alt avg `-0.4576` n `230`; crypto_major avg `-0.107` n `8`; equity avg `-0.0269` n `121`; fx avg `0.0052` n `6`; index avg `-0.001` n `25`; metal avg `0.0045` n `20`; unknown avg `-0.0242` n `794`
- 4h: commodity avg `-0.0575` n `12`; crypto_alt avg `-1.3728` n `230`; crypto_major avg `0.1044` n `8`; equity avg `0.1783` n `121`; fx avg `0.0266` n `6`; index avg `0.0234` n `25`; metal avg `0.025` n `20`; unknown avg `1.878` n `794`
- 24h: commodity avg `0.0574` n `12`; crypto_alt avg `-6.8424` n `230`; crypto_major avg `-3.4542` n `8`; equity avg `-0.294` n `121`; fx avg `0.1108` n `6`; index avg `-0.0463` n `25`; metal avg `-0.0296` n `20`; unknown avg `3.1583` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
