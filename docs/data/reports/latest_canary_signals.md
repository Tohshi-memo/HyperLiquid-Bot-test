# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T01:37:23.715397+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0628` n `12`; crypto_alt avg `0.0198` n `230`; crypto_major avg `-0.0452` n `8`; equity avg `-0.0715` n `113`; fx avg `-0.0163` n `6`; index avg `-0.0215` n `25`; metal avg `-0.0079` n `20`; unknown avg `0.0268` n `787`
- 1h: commodity avg `-0.0198` n `12`; crypto_alt avg `-0.0371` n `230`; crypto_major avg `0.0317` n `8`; equity avg `-0.4104` n `113`; fx avg `-0.0261` n `6`; index avg `-0.1057` n `25`; metal avg `-0.12` n `20`; unknown avg `-0.1706` n `787`
- 4h: commodity avg `-0.0254` n `12`; crypto_alt avg `0.0823` n `230`; crypto_major avg `-0.0074` n `8`; equity avg `-0.3749` n `113`; fx avg `-0.0406` n `6`; index avg `-0.0774` n `25`; metal avg `-0.1931` n `20`; unknown avg `0.7729` n `787`
- 24h: commodity avg `-0.3392` n `12`; crypto_alt avg `0.246` n `230`; crypto_major avg `0.4465` n `8`; equity avg `0.9597` n `113`; fx avg `0.0335` n `6`; index avg `0.214` n `25`; metal avg `-0.7721` n `20`; unknown avg `1.1377` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2433`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.207`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1969`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1856`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1632`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
