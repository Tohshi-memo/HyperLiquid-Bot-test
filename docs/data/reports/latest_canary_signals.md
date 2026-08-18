# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T10:43:07.735025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0795` n `12`; crypto_alt avg `0.0317` n `230`; crypto_major avg `0.0812` n `8`; equity avg `0.0697` n `114`; fx avg `0.0131` n `6`; index avg `0.0075` n `25`; metal avg `0.041` n `20`; unknown avg `0.2661` n `795`
- 1h: commodity avg `-0.0411` n `12`; crypto_alt avg `0.0027` n `230`; crypto_major avg `0.1006` n `8`; equity avg `-0.0664` n `114`; fx avg `-0.0152` n `6`; index avg `-0.0028` n `25`; metal avg `0.062` n `20`; unknown avg `0.3424` n `795`
- 4h: commodity avg `-0.1896` n `12`; crypto_alt avg `0.0268` n `230`; crypto_major avg `-0.2599` n `8`; equity avg `-1.147` n `114`; fx avg `-0.0286` n `6`; index avg `-0.125` n `25`; metal avg `-0.0721` n `20`; unknown avg `-0.0073` n `793`
- 24h: commodity avg `0.4697` n `12`; crypto_alt avg `-0.792` n `230`; crypto_major avg `-0.0525` n `8`; equity avg `-2.8374` n `114`; fx avg `-0.0488` n `6`; index avg `-0.5539` n `25`; metal avg `-0.2229` n `20`; unknown avg `0.0001` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
