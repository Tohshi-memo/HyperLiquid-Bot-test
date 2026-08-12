# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T14:47:16.061420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.18` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.8883` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0114` n `12`; crypto_alt avg `-0.0101` n `230`; crypto_major avg `0.0923` n `8`; equity avg `0.1276` n `113`; fx avg `-0.0083` n `6`; index avg `0.0001` n `25`; metal avg `0.0327` n `20`; unknown avg `-0.0501` n `786`
- 1h: commodity avg `0.0844` n `12`; crypto_alt avg `-0.5505` n `230`; crypto_major avg `-0.3081` n `8`; equity avg `0.1714` n `113`; fx avg `-0.0023` n `6`; index avg `0.0044` n `25`; metal avg `0.0006` n `20`; unknown avg `-0.0309` n `786`
- 4h: commodity avg `-0.047` n `12`; crypto_alt avg `-0.5187` n `230`; crypto_major avg `-0.699` n `8`; equity avg `1.1893` n `113`; fx avg `-0.0029` n `6`; index avg `0.1701` n `25`; metal avg `0.0404` n `20`; unknown avg `0.0063` n `786`
- 24h: commodity avg `0.2339` n `12`; crypto_alt avg `-0.8154` n `230`; crypto_major avg `0.7473` n `8`; equity avg `2.8327` n `113`; fx avg `0.0406` n `6`; index avg `0.2973` n `25`; metal avg `0.2807` n `20`; unknown avg `-0.0841` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2295`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2078`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1998`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1973`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
