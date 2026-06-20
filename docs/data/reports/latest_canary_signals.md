# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T01:22:26.715662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0213` n `12`; crypto_alt avg `0.0699` n `228`; crypto_major avg `0.0864` n `8`; equity avg `-0.0021` n `78`; fx avg `0.0003` n `6`; index avg `-0.0039` n `23`; metal avg `-0.014` n `18`; unknown avg `-0.4492` n `687`
- 1h: commodity avg `-0.0437` n `12`; crypto_alt avg `-0.1411` n `228`; crypto_major avg `-0.0738` n `8`; equity avg `-0.0506` n `78`; fx avg `0.0` n `6`; index avg `-0.0086` n `23`; metal avg `-0.0259` n `18`; unknown avg `-0.5512` n `687`
- 4h: commodity avg `-0.1021` n `12`; crypto_alt avg `0.1693` n `228`; crypto_major avg `0.0918` n `8`; equity avg `0.1638` n `78`; fx avg `0.0586` n `6`; index avg `0.0482` n `23`; metal avg `-0.0305` n `18`; unknown avg `-0.7809` n `679`
- 24h: commodity avg `0.245` n `12`; crypto_alt avg `-3.4208` n `228`; crypto_major avg `-4.4198` n `8`; equity avg `0.8951` n `78`; fx avg `-0.0849` n `6`; index avg `0.2678` n `23`; metal avg `-4.1292` n `18`; unknown avg `-0.8758` n `564`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
