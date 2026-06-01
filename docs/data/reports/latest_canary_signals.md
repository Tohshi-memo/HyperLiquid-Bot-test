# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T10:22:19.991655+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0784` n `12`; crypto_alt avg `0.0411` n `228`; crypto_major avg `-0.0093` n `8`; equity avg `0.064` n `69`; fx avg `0.0045` n `6`; index avg `0.0537` n `23`; metal avg `0.0287` n `18`; unknown avg `-0.0045` n `422`
- 1h: commodity avg `-0.1496` n `12`; crypto_alt avg `-0.2269` n `228`; crypto_major avg `-0.0613` n `8`; equity avg `-0.0992` n `69`; fx avg `0.009` n `6`; index avg `-0.0181` n `23`; metal avg `-0.0515` n `18`; unknown avg `0.2459` n `422`
- 4h: commodity avg `0.061` n `12`; crypto_alt avg `-0.5944` n `228`; crypto_major avg `-0.3685` n `8`; equity avg `-0.305` n `69`; fx avg `0.0444` n `6`; index avg `-0.0917` n `23`; metal avg `0.092` n `18`; unknown avg `0.3545` n `422`
- 24h: commodity avg `1.067` n `12`; crypto_alt avg `-0.0593` n `228`; crypto_major avg `-0.5593` n `8`; equity avg `-0.1457` n `69`; fx avg `-0.0039` n `6`; index avg `0.4719` n `23`; metal avg `0.2367` n `18`; unknown avg `2.1711` n `411`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2876`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2123`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
