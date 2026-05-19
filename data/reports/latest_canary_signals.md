# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T23:22:14.587826+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0595` n `12`; crypto_alt avg `0.2753` n `228`; crypto_major avg `0.2464` n `8`; equity avg `0.1571` n `66`; fx avg `-0.0051` n `6`; index avg `0.0565` n `23`; metal avg `0.0916` n `18`; unknown avg `0.0473` n `383`
- 1h: commodity avg `0.0323` n `12`; crypto_alt avg `0.1459` n `228`; crypto_major avg `0.2468` n `8`; equity avg `0.0269` n `66`; fx avg `-0.0067` n `6`; index avg `0.0507` n `23`; metal avg `0.2514` n `18`; unknown avg `-0.1717` n `383`
- 4h: commodity avg `-0.107` n `12`; crypto_alt avg `-0.1795` n `228`; crypto_major avg `0.0023` n `8`; equity avg `-0.1093` n `66`; fx avg `-0.0104` n `6`; index avg `-0.1957` n `23`; metal avg `0.1034` n `18`; unknown avg `-0.2327` n `383`
- 24h: commodity avg `1.1687` n `12`; crypto_alt avg `-1.14` n `228`; crypto_major avg `-0.6229` n `8`; equity avg `-0.4045` n `66`; fx avg `0.0682` n `6`; index avg `-0.7531` n `23`; metal avg `-3.0388` n `18`; unknown avg `0.9359` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
