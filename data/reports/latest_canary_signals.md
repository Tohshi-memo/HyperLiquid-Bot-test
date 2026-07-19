# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T01:37:24.865155+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0285` n `12`; crypto_alt avg `-0.0715` n `230`; crypto_major avg `-0.0743` n `8`; equity avg `0.0793` n `96`; fx avg `-0.0058` n `6`; index avg `0.0034` n `25`; metal avg `0.0071` n `20`; unknown avg `0.1667` n `770`
- 1h: commodity avg `0.0103` n `12`; crypto_alt avg `-0.0552` n `230`; crypto_major avg `0.0062` n `8`; equity avg `0.0762` n `96`; fx avg `-0.0066` n `6`; index avg `0.0065` n `25`; metal avg `0.011` n `20`; unknown avg `-0.3373` n `770`
- 4h: commodity avg `0.1534` n `12`; crypto_alt avg `0.0713` n `230`; crypto_major avg `0.1238` n `8`; equity avg `0.1785` n `96`; fx avg `0.0351` n `6`; index avg `0.0009` n `25`; metal avg `0.0246` n `20`; unknown avg `-0.553` n `770`
- 24h: commodity avg `0.375` n `12`; crypto_alt avg `-0.2441` n `230`; crypto_major avg `0.6549` n `8`; equity avg `-0.2515` n `96`; fx avg `-0.0429` n `6`; index avg `0.0101` n `25`; metal avg `-0.0564` n `20`; unknown avg `0.0472` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
