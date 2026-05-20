# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T16:39:32.695742+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1602` n `12`; crypto_alt avg `0.0419` n `228`; crypto_major avg `0.0646` n `8`; equity avg `-0.0202` n `66`; fx avg `-0.0016` n `6`; index avg `-0.0564` n `23`; metal avg `-0.0097` n `18`; unknown avg `1.2556` n `384`
- 1h: commodity avg `-0.0958` n `12`; crypto_alt avg `-0.042` n `228`; crypto_major avg `-0.119` n `8`; equity avg `-0.1905` n `66`; fx avg `0.0134` n `6`; index avg `0.0441` n `23`; metal avg `-0.1831` n `18`; unknown avg `0.9536` n `384`
- 4h: commodity avg `-1.1687` n `12`; crypto_alt avg `1.115` n `228`; crypto_major avg `0.6057` n `8`; equity avg `0.4288` n `66`; fx avg `0.0099` n `6`; index avg `0.6533` n `23`; metal avg `0.4297` n `18`; unknown avg `1.311` n `384`
- 24h: commodity avg `-2.205` n `12`; crypto_alt avg `2.4146` n `228`; crypto_major avg `1.4993` n `8`; equity avg `1.4663` n `66`; fx avg `0.0236` n `6`; index avg `1.0152` n `23`; metal avg `0.8828` n `18`; unknown avg `2.3062` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.046`, n `668`, weak_sample_signal
