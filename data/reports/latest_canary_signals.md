# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T15:07:29.520613+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2449` n `12`; crypto_alt avg `-0.4357` n `228`; crypto_major avg `-0.4226` n `8`; equity avg `-0.16` n `74`; fx avg `-0.0022` n `6`; index avg `-0.1598` n `23`; metal avg `0.0067` n `18`; unknown avg `-0.0162` n `556`
- 1h: commodity avg `-0.0755` n `12`; crypto_alt avg `-0.3289` n `228`; crypto_major avg `-0.3488` n `8`; equity avg `-0.7716` n `74`; fx avg `-0.0334` n `6`; index avg `-0.4301` n `23`; metal avg `-0.0314` n `18`; unknown avg `0.1756` n `556`
- 4h: commodity avg `0.1374` n `12`; crypto_alt avg `-0.285` n `228`; crypto_major avg `-0.4232` n `8`; equity avg `-0.3031` n `74`; fx avg `-0.0671` n `6`; index avg `-0.1221` n `23`; metal avg `0.1974` n `18`; unknown avg `0.6382` n `556`
- 24h: commodity avg `-0.4367` n `12`; crypto_alt avg `0.2905` n `228`; crypto_major avg `0.0747` n `8`; equity avg `-0.6167` n `74`; fx avg `-0.0426` n `6`; index avg `-0.3809` n `23`; metal avg `-0.5424` n `18`; unknown avg `2.5637` n `528`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
