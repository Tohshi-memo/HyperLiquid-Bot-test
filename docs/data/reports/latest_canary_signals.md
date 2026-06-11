# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T20:52:42.385225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.2499` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0917` n `12`; crypto_alt avg `0.1969` n `228`; crypto_major avg `0.1169` n `8`; equity avg `0.0497` n `74`; fx avg `0.002` n `6`; index avg `-0.0301` n `23`; metal avg `-0.1039` n `18`; unknown avg `-0.2939` n `556`
- 1h: commodity avg `0.0805` n `12`; crypto_alt avg `-0.13` n `228`; crypto_major avg `-0.5454` n `8`; equity avg `-0.0949` n `74`; fx avg `0.0062` n `6`; index avg `-0.0043` n `23`; metal avg `-0.1708` n `18`; unknown avg `-0.155` n `556`
- 4h: commodity avg `-1.5567` n `12`; crypto_alt avg `1.5184` n `228`; crypto_major avg `1.6932` n `8`; equity avg `2.5772` n `74`; fx avg `0.0655` n `6`; index avg `1.4147` n `23`; metal avg `2.8767` n `18`; unknown avg `0.7107` n `556`
- 24h: commodity avg `-2.1754` n `12`; crypto_alt avg `3.9675` n `228`; crypto_major avg `3.6101` n `8`; equity avg `3.9612` n `74`; fx avg `0.0336` n `6`; index avg `2.3761` n `23`; metal avg `3.5072` n `18`; unknown avg `2.0853` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
