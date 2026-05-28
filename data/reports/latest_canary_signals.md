# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T08:52:19.321291+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0295` n `12`; crypto_alt avg `-0.0652` n `228`; crypto_major avg `0.012` n `8`; equity avg `-0.0312` n `67`; fx avg `0.0157` n `6`; index avg `0.0099` n `23`; metal avg `-0.0371` n `18`; unknown avg `-0.0401` n `419`
- 1h: commodity avg `-0.2655` n `12`; crypto_alt avg `-0.3059` n `228`; crypto_major avg `-0.3432` n `8`; equity avg `0.0808` n `67`; fx avg `0.0042` n `6`; index avg `0.071` n `23`; metal avg `-0.047` n `18`; unknown avg `-0.2167` n `419`
- 4h: commodity avg `-0.5036` n `12`; crypto_alt avg `-0.2252` n `228`; crypto_major avg `0.0066` n `8`; equity avg `1.2135` n `67`; fx avg `0.047` n `6`; index avg `0.5355` n `23`; metal avg `0.8494` n `18`; unknown avg `-0.1159` n `409`
- 24h: commodity avg `0.8594` n `12`; crypto_alt avg `-4.8982` n `228`; crypto_major avg `-3.7711` n `8`; equity avg `-1.4552` n `67`; fx avg `-0.0862` n `6`; index avg `-1.063` n `23`; metal avg `-1.6484` n `18`; unknown avg `-1.9592` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.177`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1716`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
