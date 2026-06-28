# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T05:37:29.685946+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0338` n `12`; crypto_alt avg `-0.0765` n `228`; crypto_major avg `-0.0842` n `8`; equity avg `-0.0078` n `88`; fx avg `-0.0177` n `6`; index avg `0.0147` n `23`; metal avg `-0.0176` n `20`; unknown avg `-0.2317` n `764`
- 1h: commodity avg `0.0387` n `12`; crypto_alt avg `-0.3131` n `228`; crypto_major avg `-0.2296` n `8`; equity avg `-0.0264` n `88`; fx avg `-0.0172` n `6`; index avg `-0.0026` n `23`; metal avg `-0.0579` n `20`; unknown avg `0.1034` n `764`
- 4h: commodity avg `-0.2017` n `12`; crypto_alt avg `0.061` n `228`; crypto_major avg `-0.4123` n `8`; equity avg `-0.0268` n `88`; fx avg `-0.0247` n `6`; index avg `0.0119` n `23`; metal avg `-0.0231` n `20`; unknown avg `14.8363` n `714`
- 24h: commodity avg `0.2418` n `12`; crypto_alt avg `-0.5977` n `228`; crypto_major avg `-1.3683` n `8`; equity avg `0.023` n `88`; fx avg `-0.0304` n `6`; index avg `-0.1032` n `23`; metal avg `-0.0705` n `20`; unknown avg `16.378` n `666`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.22`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1878`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
