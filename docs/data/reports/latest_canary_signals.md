# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T00:52:30.643868+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1642` n `12`; crypto_alt avg `-0.0641` n `228`; crypto_major avg `-0.0552` n `8`; equity avg `0.0111` n `74`; fx avg `-0.0051` n `6`; index avg `-0.0` n `23`; metal avg `-0.2039` n `18`; unknown avg `-0.0271` n `556`
- 1h: commodity avg `0.1463` n `12`; crypto_alt avg `0.502` n `228`; crypto_major avg `0.2097` n `8`; equity avg `0.5162` n `74`; fx avg `-0.0196` n `6`; index avg `-0.0945` n `23`; metal avg `-0.0764` n `18`; unknown avg `0.0305` n `556`
- 4h: commodity avg `-0.2121` n `12`; crypto_alt avg `0.4729` n `228`; crypto_major avg `0.5443` n `8`; equity avg `1.0936` n `74`; fx avg `0.0086` n `6`; index avg `0.3343` n `23`; metal avg `0.1629` n `18`; unknown avg `0.2955` n `556`
- 24h: commodity avg `-2.6883` n `12`; crypto_alt avg `3.8728` n `228`; crypto_major avg `3.9559` n `8`; equity avg `4.8456` n `74`; fx avg `0.02` n `6`; index avg `2.568` n `23`; metal avg `3.4776` n `18`; unknown avg `2.8537` n `530`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
