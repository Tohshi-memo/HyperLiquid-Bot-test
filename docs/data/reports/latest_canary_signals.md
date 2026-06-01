# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T21:37:21.074746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.85` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0274` n `12`; crypto_alt avg `0.2187` n `228`; crypto_major avg `0.0857` n `8`; equity avg `-0.0615` n `69`; fx avg `-0.0039` n `6`; index avg `-0.0523` n `23`; metal avg `0.004` n `18`; unknown avg `0.1123` n `422`
- 1h: commodity avg `-0.0182` n `12`; crypto_alt avg `-0.4109` n `228`; crypto_major avg `-0.4335` n `8`; equity avg `-0.1336` n `69`; fx avg `-0.0019` n `6`; index avg `-0.1588` n `23`; metal avg `-0.0283` n `18`; unknown avg `-0.2055` n `422`
- 4h: commodity avg `0.2294` n `12`; crypto_alt avg `-0.0888` n `228`; crypto_major avg `0.0174` n `8`; equity avg `-0.7005` n `69`; fx avg `0.0139` n `6`; index avg `-0.1048` n `23`; metal avg `-0.1062` n `18`; unknown avg `-0.0778` n `422`
- 24h: commodity avg `0.5088` n `12`; crypto_alt avg `0.5368` n `228`; crypto_major avg `-1.1177` n `8`; equity avg `-0.2815` n `69`; fx avg `0.0584` n `6`; index avg `0.1169` n `23`; metal avg `-0.0945` n `18`; unknown avg `2.3023` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
