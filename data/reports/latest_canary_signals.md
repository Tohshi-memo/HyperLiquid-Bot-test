# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T09:37:38.537455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0832` n `12`; crypto_alt avg `0.2841` n `228`; crypto_major avg `0.2138` n `8`; equity avg `0.0738` n `74`; fx avg `-0.0118` n `6`; index avg `-0.0042` n `23`; metal avg `-0.0419` n `18`; unknown avg `0.6424` n `556`
- 1h: commodity avg `0.2107` n `12`; crypto_alt avg `-0.322` n `228`; crypto_major avg `-0.2958` n `8`; equity avg `-0.2583` n `74`; fx avg `-0.0162` n `6`; index avg `-0.042` n `23`; metal avg `-0.4884` n `18`; unknown avg `4.7948` n `556`
- 4h: commodity avg `-0.5243` n `12`; crypto_alt avg `0.3044` n `228`; crypto_major avg `0.5188` n `8`; equity avg `0.6953` n `74`; fx avg `-0.0053` n `6`; index avg `0.3423` n `23`; metal avg `-0.3268` n `18`; unknown avg `4.9946` n `530`
- 24h: commodity avg `0.6457` n `12`; crypto_alt avg `1.7899` n `228`; crypto_major avg `1.6854` n `8`; equity avg `0.9246` n `74`; fx avg `0.0029` n `6`; index avg `0.0794` n `23`; metal avg `-0.5978` n `18`; unknown avg `8.8854` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
