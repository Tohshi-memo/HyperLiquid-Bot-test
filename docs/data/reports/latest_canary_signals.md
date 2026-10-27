# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T18:37:29.451778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1059` n `13`; crypto_alt avg `0.1305` n `238`; crypto_major avg `0.105` n `8`; equity avg `0.0724` n `154`; fx avg `0.0096` n `6`; index avg `-0.0027` n `27`; metal avg `0.0055` n `20`; unknown avg `1.3891` n `1238`
- 1h: commodity avg `-0.0711` n `13`; crypto_alt avg `0.2204` n `238`; crypto_major avg `0.0289` n `8`; equity avg `-0.0976` n `154`; fx avg `0.0027` n `6`; index avg `-0.0223` n `27`; metal avg `-0.0836` n `20`; unknown avg `2.3776` n `1234`
- 4h: commodity avg `-0.1053` n `13`; crypto_alt avg `0.8801` n `238`; crypto_major avg `0.7312` n `8`; equity avg `0.7992` n `154`; fx avg `-0.0202` n `6`; index avg `0.1272` n `27`; metal avg `0.0261` n `20`; unknown avg `11.4057` n `1196`
- 24h: commodity avg `-0.5011` n `13`; crypto_alt avg `1.0038` n `237`; crypto_major avg `0.9762` n `8`; equity avg `1.3397` n `154`; fx avg `-0.0561` n `6`; index avg `0.3616` n `27`; metal avg `0.0968` n `20`; unknown avg `31.8208` n `1044`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2254`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1966`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1958`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
