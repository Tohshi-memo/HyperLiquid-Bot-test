# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T11:22:34.737545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.37` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.549` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0876` n `12`; crypto_alt avg `0.4927` n `228`; crypto_major avg `0.5011` n `8`; equity avg `0.1089` n `74`; fx avg `0.0013` n `6`; index avg `0.0398` n `23`; metal avg `0.0029` n `18`; unknown avg `0.0626` n `689`
- 1h: commodity avg `-0.0101` n `12`; crypto_alt avg `1.1796` n `228`; crypto_major avg `1.3152` n `8`; equity avg `0.1453` n `74`; fx avg `-0.0131` n `6`; index avg `0.0778` n `23`; metal avg `0.1864` n `18`; unknown avg `0.0517` n `689`
- 4h: commodity avg `0.0649` n `12`; crypto_alt avg `1.2` n `228`; crypto_major avg `1.5782` n `8`; equity avg `0.0292` n `74`; fx avg `0.0059` n `6`; index avg `0.1034` n `23`; metal avg `0.6125` n `18`; unknown avg `1.0985` n `689`
- 24h: commodity avg `-1.106` n `12`; crypto_alt avg `4.6673` n `228`; crypto_major avg `4.7011` n `8`; equity avg `1.5726` n `74`; fx avg `0.0569` n `6`; index avg `0.9926` n `23`; metal avg `2.5215` n `18`; unknown avg `1.2247` n `529`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
