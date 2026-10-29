# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T14:52:31.651717+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0905` n `13`; crypto_alt avg `-0.3473` n `238`; crypto_major avg `-0.3609` n `8`; equity avg `-0.3534` n `156`; fx avg `0.0257` n `6`; index avg `-0.0637` n `27`; metal avg `-0.0362` n `20`; unknown avg `38.2004` n `1236`
- 1h: commodity avg `-0.0091` n `13`; crypto_alt avg `0.589` n `238`; crypto_major avg `0.6718` n `8`; equity avg `0.2772` n `156`; fx avg `0.1017` n `6`; index avg `0.0337` n `27`; metal avg `0.1098` n `20`; unknown avg `23.6707` n `1140`
- 4h: commodity avg `-0.458` n `13`; crypto_alt avg `1.01` n `238`; crypto_major avg `1.3358` n `8`; equity avg `0.0905` n `156`; fx avg `0.0437` n `6`; index avg `-0.122` n `27`; metal avg `-0.0951` n `20`; unknown avg `24.0504` n `1134`
- 24h: commodity avg `-0.908` n `13`; crypto_alt avg `0.5495` n `238`; crypto_major avg `1.9977` n `8`; equity avg `-0.3965` n `155`; fx avg `0.0241` n `6`; index avg `-0.1136` n `27`; metal avg `-0.3946` n `20`; unknown avg `39.7348` n `946`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
