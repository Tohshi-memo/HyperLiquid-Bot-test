# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T15:12:55.721478+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0216` n `12`; crypto_alt avg `0.0162` n `230`; crypto_major avg `0.026` n `8`; equity avg `0.1553` n `114`; fx avg `-0.004` n `6`; index avg `0.0176` n `25`; metal avg `0.0078` n `20`; unknown avg `-0.0172` n `792`
- 1h: commodity avg `-0.0374` n `12`; crypto_alt avg `0.1417` n `230`; crypto_major avg `0.3405` n `8`; equity avg `0.6283` n `114`; fx avg `-0.0134` n `6`; index avg `0.0842` n `25`; metal avg `0.1396` n `20`; unknown avg `-0.0177` n `792`
- 4h: commodity avg `-0.0144` n `12`; crypto_alt avg `-0.0262` n `230`; crypto_major avg `0.0221` n `8`; equity avg `0.3435` n `114`; fx avg `0.014` n `6`; index avg `0.0748` n `25`; metal avg `0.1075` n `20`; unknown avg `0.0231` n `792`
- 24h: commodity avg `-0.0783` n `12`; crypto_alt avg `-0.0607` n `230`; crypto_major avg `0.9335` n `8`; equity avg `1.6812` n `114`; fx avg `0.005` n `6`; index avg `0.2336` n `25`; metal avg `0.3204` n `20`; unknown avg `0.0738` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1638`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
