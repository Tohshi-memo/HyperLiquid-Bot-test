# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T22:22:20.846535+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.223` n `12`; crypto_alt avg `-0.1105` n `228`; crypto_major avg `-0.0693` n `8`; equity avg `0.0814` n `65`; fx avg `-0.0019` n `5`; index avg `0.0635` n `23`; metal avg `0.008` n `18`; unknown avg `-0.0023` n `375`
- 1h: commodity avg `-0.278` n `12`; crypto_alt avg `0.4604` n `228`; crypto_major avg `0.2454` n `8`; equity avg `0.2481` n `65`; fx avg `-0.0061` n `5`; index avg `0.1589` n `23`; metal avg `-0.0198` n `18`; unknown avg `0.0409` n `375`
- 4h: commodity avg `-0.3856` n `12`; crypto_alt avg `0.5487` n `228`; crypto_major avg `0.2148` n `8`; equity avg `0.8839` n `65`; fx avg `0.0117` n `5`; index avg `0.0415` n `23`; metal avg `-0.2654` n `18`; unknown avg `-0.304` n `375`
- 24h: commodity avg `-0.6828` n `12`; crypto_alt avg `3.7521` n `228`; crypto_major avg `1.7816` n `8`; equity avg `4.4683` n `65`; fx avg `0.2027` n `5`; index avg `1.64` n `23`; metal avg `1.0322` n `18`; unknown avg `0.8489` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
