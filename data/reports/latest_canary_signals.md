# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T00:22:33.296471+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1905` n `12`; crypto_alt avg `-0.0753` n `228`; crypto_major avg `-0.2665` n `8`; equity avg `0.0037` n `74`; fx avg `-0.0118` n `6`; index avg `-0.0801` n `23`; metal avg `-0.0828` n `18`; unknown avg `0.0142` n `556`
- 1h: commodity avg `0.0068` n `12`; crypto_alt avg `0.3697` n `228`; crypto_major avg `0.0433` n `8`; equity avg `0.4034` n `74`; fx avg `0.019` n `6`; index avg `-0.0121` n `23`; metal avg `-0.0026` n `18`; unknown avg `0.1319` n `556`
- 4h: commodity avg `-0.154` n `12`; crypto_alt avg `0.2249` n `228`; crypto_major avg `0.1179` n `8`; equity avg `0.8251` n `74`; fx avg `0.0607` n `6`; index avg `0.2497` n `23`; metal avg `0.1557` n `18`; unknown avg `-0.286` n `556`
- 24h: commodity avg `-2.7118` n `12`; crypto_alt avg `3.782` n `228`; crypto_major avg `3.7258` n `8`; equity avg `4.8404` n `74`; fx avg `0.0697` n `6`; index avg `2.6683` n `23`; metal avg `3.8862` n `18`; unknown avg `2.6439` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
