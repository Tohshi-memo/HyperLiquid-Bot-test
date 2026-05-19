# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T03:37:19.512886+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0966` n `12`; crypto_alt avg `0.1823` n `228`; crypto_major avg `0.1894` n `8`; equity avg `0.2294` n `66`; fx avg `-0.0059` n `6`; index avg `0.104` n `23`; metal avg `-0.0735` n `18`; unknown avg `-0.0617` n `383`
- 1h: commodity avg `-0.0957` n `12`; crypto_alt avg `0.2991` n `228`; crypto_major avg `0.1994` n `8`; equity avg `0.4152` n `66`; fx avg `0.017` n `6`; index avg `0.2222` n `23`; metal avg `-0.0556` n `18`; unknown avg `-0.287` n `383`
- 4h: commodity avg `0.1767` n `12`; crypto_alt avg `-0.0194` n `228`; crypto_major avg `-0.1352` n `8`; equity avg `-0.4236` n `66`; fx avg `0.1583` n `6`; index avg `-0.3004` n `23`; metal avg `-1.3097` n `18`; unknown avg `-0.6058` n `383`
- 24h: commodity avg `0.1718` n `12`; crypto_alt avg `0.9767` n `228`; crypto_major avg `0.4471` n `8`; equity avg `-0.4945` n `66`; fx avg `0.2486` n `6`; index avg `-0.194` n `23`; metal avg `0.8554` n `18`; unknown avg `0.3939` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1911`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1619`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
