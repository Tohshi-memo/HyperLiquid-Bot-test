# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T23:52:33.536002+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0607` n `12`; crypto_alt avg `0.4354` n `234`; crypto_major avg `0.2375` n `8`; equity avg `0.0181` n `141`; fx avg `-0.0143` n `6`; index avg `0.0161` n `26`; metal avg `0.0281` n `20`; unknown avg `2.9485` n `962`
- 1h: commodity avg `-0.0289` n `12`; crypto_alt avg `0.7822` n `234`; crypto_major avg `0.5368` n `8`; equity avg `0.058` n `141`; fx avg `-0.0219` n `6`; index avg `0.0431` n `26`; metal avg `0.0378` n `20`; unknown avg `6.4171` n `960`
- 4h: commodity avg `-0.3112` n `12`; crypto_alt avg `0.2` n `234`; crypto_major avg `-0.2476` n `8`; equity avg `-0.3504` n `141`; fx avg `-0.0325` n `6`; index avg `-0.0624` n `26`; metal avg `-0.1579` n `20`; unknown avg `3.3911` n `886`
- 24h: commodity avg `-0.4602` n `12`; crypto_alt avg `0.8371` n `234`; crypto_major avg `0.037` n `8`; equity avg `-0.014` n `141`; fx avg `-0.0326` n `6`; index avg `-0.0198` n `26`; metal avg `-0.1771` n `20`; unknown avg `4.8396` n `827`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
