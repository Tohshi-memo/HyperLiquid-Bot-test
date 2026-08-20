# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T07:37:24.612774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.013` n `12`; crypto_alt avg `-0.076` n `230`; crypto_major avg `-0.0993` n `8`; equity avg `-0.0668` n `121`; fx avg `0.0041` n `6`; index avg `-0.0057` n `25`; metal avg `-0.011` n `20`; unknown avg `-0.0068` n `792`
- 1h: commodity avg `0.1316` n `12`; crypto_alt avg `-0.0061` n `230`; crypto_major avg `0.0123` n `8`; equity avg `-0.1111` n `121`; fx avg `0.0495` n `6`; index avg `-0.0255` n `25`; metal avg `-0.1153` n `20`; unknown avg `0.1564` n `792`
- 4h: commodity avg `0.148` n `12`; crypto_alt avg `0.6757` n `230`; crypto_major avg `1.1008` n `8`; equity avg `0.1394` n `121`; fx avg `0.0211` n `6`; index avg `0.0325` n `25`; metal avg `-0.1143` n `20`; unknown avg `0.3407` n `776`
- 24h: commodity avg `0.1329` n `12`; crypto_alt avg `5.6622` n `230`; crypto_major avg `10.2841` n `8`; equity avg `0.5322` n `120`; fx avg `0.0835` n `6`; index avg `0.1776` n `25`; metal avg `0.8883` n `20`; unknown avg `2.0126` n `773`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1985`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
