# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T14:37:16.574362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2584` n `12`; crypto_alt avg `-0.0565` n `228`; crypto_major avg `-0.0337` n `8`; equity avg `0.2739` n `66`; fx avg `0.0089` n `6`; index avg `0.1177` n `23`; metal avg `0.048` n `18`; unknown avg `-0.0647` n `383`
- 1h: commodity avg `-0.3896` n `12`; crypto_alt avg `-0.7066` n `228`; crypto_major avg `-0.7925` n `8`; equity avg `-1.3018` n `66`; fx avg `-0.0007` n `6`; index avg `-0.8523` n `23`; metal avg `0.0884` n `18`; unknown avg `-0.1138` n `383`
- 4h: commodity avg `0.0385` n `12`; crypto_alt avg `-0.6618` n `228`; crypto_major avg `-0.7038` n `8`; equity avg `-0.9386` n `66`; fx avg `-0.0466` n `6`; index avg `-0.7589` n `23`; metal avg `-1.4561` n `18`; unknown avg `-0.4517` n `383`
- 24h: commodity avg `0.7815` n `12`; crypto_alt avg `0.6389` n `228`; crypto_major avg `0.4095` n `8`; equity avg `-1.2557` n `66`; fx avg `0.1928` n `6`; index avg `-1.2604` n `23`; metal avg `-1.8144` n `18`; unknown avg `-0.2574` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.2366`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
