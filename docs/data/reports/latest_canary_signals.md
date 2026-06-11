# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T10:07:28.720356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0257` n `12`; crypto_alt avg `0.0943` n `228`; crypto_major avg `-0.0149` n `8`; equity avg `0.0783` n `74`; fx avg `-0.0101` n `6`; index avg `0.06` n `23`; metal avg `-0.0283` n `18`; unknown avg `0.1594` n `556`
- 1h: commodity avg `-0.0472` n `12`; crypto_alt avg `0.2296` n `228`; crypto_major avg `0.1023` n `8`; equity avg `0.0617` n `74`; fx avg `-0.0203` n `6`; index avg `0.032` n `23`; metal avg `0.0337` n `18`; unknown avg `0.6926` n `556`
- 4h: commodity avg `-0.6872` n `12`; crypto_alt avg `0.7836` n `228`; crypto_major avg `0.6746` n `8`; equity avg `1.0376` n `74`; fx avg `-0.0301` n `6`; index avg `0.5249` n `23`; metal avg `0.2597` n `18`; unknown avg `4.9646` n `546`
- 24h: commodity avg `0.3693` n `12`; crypto_alt avg `1.9364` n `228`; crypto_major avg `1.9122` n `8`; equity avg `1.165` n `74`; fx avg `-0.0156` n `6`; index avg `0.2192` n `23`; metal avg `-0.272` n `18`; unknown avg `8.8756` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
