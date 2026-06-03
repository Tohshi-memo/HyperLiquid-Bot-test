# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T22:37:28.895130+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.2` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.5876` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1059` n `12`; crypto_alt avg `-0.0876` n `228`; crypto_major avg `0.0186` n `8`; equity avg `-0.1184` n `73`; fx avg `0.0096` n `6`; index avg `-0.0076` n `23`; metal avg `0.167` n `18`; unknown avg `-0.0973` n `419`
- 1h: commodity avg `-0.4166` n `12`; crypto_alt avg `-0.0675` n `228`; crypto_major avg `-0.0573` n `8`; equity avg `0.2129` n `73`; fx avg `0.01` n `6`; index avg `0.0292` n `23`; metal avg `-0.08` n `18`; unknown avg `0.03` n `419`
- 4h: commodity avg `-0.1996` n `12`; crypto_alt avg `0.1126` n `228`; crypto_major avg `-0.084` n `8`; equity avg `-1.6716` n `73`; fx avg `0.0046` n `6`; index avg `-0.5171` n `23`; metal avg `-0.2129` n `18`; unknown avg `-0.0413` n `419`
- 24h: commodity avg `0.5872` n `12`; crypto_alt avg `1.3616` n `228`; crypto_major avg `-0.8916` n `8`; equity avg `-3.6702` n `72`; fx avg `0.0556` n `6`; index avg `-0.9133` n `23`; metal avg `-2.2493` n `18`; unknown avg `1.3322` n `409`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
