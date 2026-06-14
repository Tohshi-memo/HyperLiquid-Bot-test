# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T10:37:25.526668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1003` n `12`; crypto_alt avg `-0.069` n `228`; crypto_major avg `0.0581` n `8`; equity avg `0.0598` n `74`; fx avg `0.0035` n `6`; index avg `-0.01` n `23`; metal avg `0.0061` n `18`; unknown avg `0.0375` n `645`
- 1h: commodity avg `0.0319` n `12`; crypto_alt avg `0.1485` n `228`; crypto_major avg `0.4433` n `8`; equity avg `0.2417` n `74`; fx avg `0.0247` n `6`; index avg `0.063` n `23`; metal avg `0.0081` n `18`; unknown avg `0.3459` n `645`
- 4h: commodity avg `-0.0706` n `12`; crypto_alt avg `0.3512` n `228`; crypto_major avg `0.5033` n `8`; equity avg `0.4515` n `74`; fx avg `0.0045` n `6`; index avg `0.0916` n `23`; metal avg `0.0366` n `18`; unknown avg `0.3672` n `627`
- 24h: commodity avg `-0.6266` n `12`; crypto_alt avg `0.5154` n `228`; crypto_major avg `1.3108` n `8`; equity avg `1.0106` n `74`; fx avg `0.006` n `6`; index avg `0.3571` n `23`; metal avg `0.387` n `18`; unknown avg `-0.6084` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
