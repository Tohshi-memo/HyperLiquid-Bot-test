# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T23:07:13.809388+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.015` n `12`; crypto_alt avg `0.3307` n `228`; crypto_major avg `0.2453` n `8`; equity avg `0.2493` n `66`; fx avg `-0.0029` n `6`; index avg `0.0525` n `23`; metal avg `0.267` n `18`; unknown avg `0.0231` n `383`
- 1h: commodity avg `0.0326` n `12`; crypto_alt avg `0.0157` n `228`; crypto_major avg `0.03` n `8`; equity avg `0.3209` n `66`; fx avg `-0.0069` n `6`; index avg `0.0592` n `23`; metal avg `0.4975` n `18`; unknown avg `-0.3403` n `383`
- 4h: commodity avg `-0.143` n `12`; crypto_alt avg `1.657` n `228`; crypto_major avg `1.3074` n `8`; equity avg `1.272` n `66`; fx avg `-0.0487` n `6`; index avg `0.5937` n `23`; metal avg `0.7565` n `18`; unknown avg `-0.0795` n `383`
- 24h: commodity avg `0.7419` n `12`; crypto_alt avg `-0.1872` n `228`; crypto_major avg `-0.7664` n `8`; equity avg `-0.3576` n `66`; fx avg `0.1681` n `6`; index avg `-0.0871` n `23`; metal avg `1.062` n `18`; unknown avg `-0.1867` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
