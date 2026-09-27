# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T21:22:31.941239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0205` n `12`; crypto_alt avg `0.2076` n `234`; crypto_major avg `0.0845` n `8`; equity avg `0.0166` n `141`; fx avg `0.0053` n `6`; index avg `0.0079` n `26`; metal avg `-0.0005` n `20`; unknown avg `0.8642` n `930`
- 1h: commodity avg `0.0256` n `12`; crypto_alt avg `-0.0657` n `234`; crypto_major avg `0.0089` n `8`; equity avg `-0.0069` n `141`; fx avg `-0.0501` n `6`; index avg `0.0017` n `26`; metal avg `-0.0053` n `20`; unknown avg `1.3786` n `926`
- 4h: commodity avg `0.0574` n `12`; crypto_alt avg `0.4579` n `234`; crypto_major avg `0.2902` n `8`; equity avg `0.1181` n `141`; fx avg `-0.0488` n `6`; index avg `0.0282` n `26`; metal avg `-0.0023` n `20`; unknown avg `2.5558` n `894`
- 24h: commodity avg `-0.124` n `12`; crypto_alt avg `1.2634` n `234`; crypto_major avg `0.6087` n `8`; equity avg `0.4355` n `141`; fx avg `-0.0589` n `6`; index avg `0.054` n `26`; metal avg `-0.0147` n `20`; unknown avg `8.3172` n `837`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
