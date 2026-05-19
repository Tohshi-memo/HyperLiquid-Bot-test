# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T06:52:19.524540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.056` n `12`; crypto_alt avg `0.0467` n `228`; crypto_major avg `0.0421` n `8`; equity avg `0.1201` n `66`; fx avg `-0.0343` n `6`; index avg `0.0736` n `23`; metal avg `-0.0544` n `18`; unknown avg `0.1618` n `383`
- 1h: commodity avg `0.1996` n `12`; crypto_alt avg `0.2192` n `228`; crypto_major avg `0.0736` n `8`; equity avg `0.2367` n `66`; fx avg `-0.0287` n `6`; index avg `0.1238` n `23`; metal avg `0.2663` n `18`; unknown avg `0.3248` n `363`
- 4h: commodity avg `0.3324` n `12`; crypto_alt avg `0.6212` n `228`; crypto_major avg `0.3283` n `8`; equity avg `0.2706` n `66`; fx avg `0.0292` n `6`; index avg `0.1488` n `23`; metal avg `-0.0432` n `18`; unknown avg `0.5581` n `363`
- 24h: commodity avg `0.4785` n `12`; crypto_alt avg `1.6831` n `228`; crypto_major avg `0.8129` n `8`; equity avg `-0.6739` n `66`; fx avg `0.2783` n `6`; index avg `-0.2799` n `23`; metal avg `0.2523` n `18`; unknown avg `0.694` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
