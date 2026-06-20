# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T16:37:25.043798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0245` n `12`; crypto_alt avg `-0.2592` n `228`; crypto_major avg `-0.2645` n `8`; equity avg `-0.0561` n `78`; fx avg `-0.0194` n `6`; index avg `-0.0188` n `23`; metal avg `-0.0218` n `18`; unknown avg `0.0872` n `701`
- 1h: commodity avg `-0.0086` n `12`; crypto_alt avg `-0.3988` n `228`; crypto_major avg `-0.4267` n `8`; equity avg `-0.0647` n `78`; fx avg `0.0053` n `6`; index avg `-0.0265` n `23`; metal avg `-0.0483` n `18`; unknown avg `0.0897` n `701`
- 4h: commodity avg `0.2173` n `12`; crypto_alt avg `0.0972` n `228`; crypto_major avg `-0.1624` n `8`; equity avg `-0.0085` n `78`; fx avg `0.0142` n `6`; index avg `-0.0198` n `23`; metal avg `-0.0179` n `18`; unknown avg `0.4234` n `701`
- 24h: commodity avg `0.2595` n `12`; crypto_alt avg `0.1064` n `228`; crypto_major avg `0.8645` n `8`; equity avg `0.2928` n `78`; fx avg `0.0699` n `6`; index avg `-0.0013` n `23`; metal avg `0.3088` n `18`; unknown avg `-0.1886` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
