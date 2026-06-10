# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T14:22:31.022573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1964` n `12`; crypto_alt avg `-0.3382` n `228`; crypto_major avg `-0.3262` n `8`; equity avg `-0.0196` n `74`; fx avg `-0.0241` n `6`; index avg `0.1838` n `23`; metal avg `-0.1492` n `18`; unknown avg `-0.0438` n `547`
- 1h: commodity avg `-0.0339` n `12`; crypto_alt avg `0.6031` n `228`; crypto_major avg `0.8523` n `8`; equity avg `1.6062` n `74`; fx avg `-0.0147` n `6`; index avg `0.9097` n `23`; metal avg `0.808` n `18`; unknown avg `1.4216` n `547`
- 4h: commodity avg `0.8566` n `12`; crypto_alt avg `1.3438` n `228`; crypto_major avg `1.656` n `8`; equity avg `2.1991` n `74`; fx avg `-0.0397` n `6`; index avg `0.992` n `23`; metal avg `0.847` n `18`; unknown avg `1.5172` n `547`
- 24h: commodity avg `1.0153` n `12`; crypto_alt avg `0.6345` n `228`; crypto_major avg `-0.6307` n `8`; equity avg `-1.0216` n `74`; fx avg `-0.0796` n `6`; index avg `-0.661` n `23`; metal avg `-2.1574` n `18`; unknown avg `1.4831` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
