# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T07:37:27.022154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0456` n `12`; crypto_alt avg `-0.0403` n `232`; crypto_major avg `-0.1347` n `8`; equity avg `0.0413` n `133`; fx avg `0.0156` n `6`; index avg `0.0032` n `26`; metal avg `0.041` n `20`; unknown avg `0.0192` n `793`
- 1h: commodity avg `0.0424` n `12`; crypto_alt avg `0.4194` n `232`; crypto_major avg `0.2006` n `8`; equity avg `0.1248` n `133`; fx avg `0.0383` n `6`; index avg `0.0093` n `26`; metal avg `0.1286` n `20`; unknown avg `0.1969` n `791`
- 4h: commodity avg `-0.0792` n `12`; crypto_alt avg `-0.3372` n `232`; crypto_major avg `-0.3885` n `8`; equity avg `0.0946` n `133`; fx avg `-0.0136` n `6`; index avg `0.0489` n `26`; metal avg `0.0261` n `20`; unknown avg `0.6316` n `755`
- 24h: commodity avg `-0.0438` n `12`; crypto_alt avg `1.7822` n `232`; crypto_major avg `3.5395` n `8`; equity avg `1.7206` n `133`; fx avg `-0.0579` n `6`; index avg `0.3446` n `26`; metal avg `0.495` n `20`; unknown avg `1.7875` n `730`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
