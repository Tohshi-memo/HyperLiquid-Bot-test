# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T07:07:34.288290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0235` n `12`; crypto_alt avg `-0.1207` n `228`; crypto_major avg `-0.0339` n `8`; equity avg `-0.0025` n `74`; fx avg `0.0032` n `6`; index avg `0.0008` n `23`; metal avg `-0.0129` n `18`; unknown avg `-0.0265` n `645`
- 1h: commodity avg `-0.0614` n `12`; crypto_alt avg `-0.5593` n `228`; crypto_major avg `-0.3207` n `8`; equity avg `0.0329` n `74`; fx avg `-0.0109` n `6`; index avg `0.011` n `23`; metal avg `-0.0065` n `18`; unknown avg `3.0457` n `641`
- 4h: commodity avg `-0.1033` n `12`; crypto_alt avg `-0.5276` n `228`; crypto_major avg `-0.5262` n `8`; equity avg `0.0106` n `74`; fx avg `-0.0072` n `6`; index avg `-0.0192` n `23`; metal avg `-0.0029` n `18`; unknown avg `1.9396` n `625`
- 24h: commodity avg `-0.7433` n `12`; crypto_alt avg `0.835` n `228`; crypto_major avg `1.1079` n `8`; equity avg `0.7317` n `74`; fx avg `-0.0165` n `6`; index avg `0.2347` n `23`; metal avg `0.2931` n `18`; unknown avg `-0.39` n `599`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
