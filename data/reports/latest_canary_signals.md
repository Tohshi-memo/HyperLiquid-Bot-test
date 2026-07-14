# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T09:22:32.080473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0879` n `12`; crypto_alt avg `-0.0031` n `230`; crypto_major avg `0.0029` n `8`; equity avg `0.0483` n `92`; fx avg `0.0019` n `6`; index avg `-0.0085` n `25`; metal avg `0.0028` n `20`; unknown avg `-0.0266` n `766`
- 1h: commodity avg `0.1205` n `12`; crypto_alt avg `0.0004` n `230`; crypto_major avg `0.1457` n `8`; equity avg `0.0613` n `92`; fx avg `0.0326` n `6`; index avg `-0.0053` n `25`; metal avg `0.0345` n `20`; unknown avg `0.0397` n `766`
- 4h: commodity avg `0.183` n `12`; crypto_alt avg `-0.0787` n `230`; crypto_major avg `-0.1262` n `8`; equity avg `0.3097` n `92`; fx avg `0.0866` n `6`; index avg `-0.0017` n `25`; metal avg `0.0076` n `20`; unknown avg `-0.0318` n `750`
- 24h: commodity avg `1.6419` n `12`; crypto_alt avg `-0.813` n `230`; crypto_major avg `-0.6819` n `8`; equity avg `-0.5593` n `92`; fx avg `-0.0417` n `6`; index avg `-0.1487` n `25`; metal avg `-0.1856` n `20`; unknown avg `-0.2685` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
