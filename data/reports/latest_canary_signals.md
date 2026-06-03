# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T23:52:24.525465+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.18` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.856` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0151` n `12`; crypto_alt avg `-0.0796` n `228`; crypto_major avg `-0.086` n `8`; equity avg `0.0335` n `73`; fx avg `-0.0034` n `6`; index avg `0.0407` n `23`; metal avg `0.1407` n `18`; unknown avg `-0.1728` n `419`
- 1h: commodity avg `-0.0417` n `12`; crypto_alt avg `-0.6785` n `228`; crypto_major avg `-0.645` n `8`; equity avg `-0.3791` n `73`; fx avg `0.0187` n `6`; index avg `0.0138` n `23`; metal avg `0.4192` n `18`; unknown avg `-0.5929` n `419`
- 4h: commodity avg `-0.1579` n `12`; crypto_alt avg `-0.2942` n `228`; crypto_major avg `-0.1256` n `8`; equity avg `-1.9816` n `73`; fx avg `-0.037` n `6`; index avg `-0.5599` n `23`; metal avg `0.1966` n `18`; unknown avg `0.1489` n `419`
- 24h: commodity avg `0.2677` n `12`; crypto_alt avg `2.1943` n `228`; crypto_major avg `-0.9889` n `8`; equity avg `-3.647` n `72`; fx avg `0.0711` n `6`; index avg `-0.9496` n `23`; metal avg `-1.5803` n `18`; unknown avg `0.8134` n `409`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
