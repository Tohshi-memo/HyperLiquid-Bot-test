# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T01:49:34.300719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0382` n `12`; crypto_alt avg `-0.1716` n `228`; crypto_major avg `-0.1999` n `8`; equity avg `-0.1703` n `86`; fx avg `-0.0033` n `6`; index avg `-0.004` n `23`; metal avg `-0.0914` n `20`; unknown avg `-0.0747` n `764`
- 1h: commodity avg `0.016` n `12`; crypto_alt avg `-0.0997` n `228`; crypto_major avg `0.1339` n `8`; equity avg `-0.2365` n `86`; fx avg `-0.0113` n `6`; index avg `-0.0193` n `23`; metal avg `-0.0546` n `20`; unknown avg `-0.5063` n `764`
- 4h: commodity avg `-0.0581` n `12`; crypto_alt avg `0.2133` n `228`; crypto_major avg `0.6958` n `8`; equity avg `0.3223` n `86`; fx avg `0.0191` n `6`; index avg `0.0956` n `23`; metal avg `-0.1958` n `20`; unknown avg `-0.195` n `756`
- 24h: commodity avg `-0.447` n `12`; crypto_alt avg `-1.5045` n `228`; crypto_major avg `-2.0067` n `8`; equity avg `-1.4218` n `86`; fx avg `-0.1467` n `6`; index avg `-0.4622` n `23`; metal avg `-0.8798` n `20`; unknown avg `0.374` n `588`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
