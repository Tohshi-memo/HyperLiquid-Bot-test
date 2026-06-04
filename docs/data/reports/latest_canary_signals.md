# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T21:22:27.792711+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0397` n `12`; crypto_alt avg `-0.8543` n `228`; crypto_major avg `-0.7768` n `8`; equity avg `-0.0292` n `74`; fx avg `-0.0018` n `6`; index avg `-0.0142` n `23`; metal avg `-0.0362` n `18`; unknown avg `-0.174` n `424`
- 1h: commodity avg `0.1466` n `12`; crypto_alt avg `-0.5301` n `228`; crypto_major avg `-0.2593` n `8`; equity avg `0.0235` n `74`; fx avg `0.0282` n `6`; index avg `-0.0646` n `23`; metal avg `-0.0827` n `18`; unknown avg `-0.0525` n `424`
- 4h: commodity avg `0.3383` n `12`; crypto_alt avg `-1.1845` n `228`; crypto_major avg `-0.4548` n `8`; equity avg `-0.6246` n `74`; fx avg `-0.0169` n `6`; index avg `-0.1434` n `23`; metal avg `-0.0631` n `18`; unknown avg `-0.3941` n `424`
- 24h: commodity avg `-0.7819` n `12`; crypto_alt avg `-5.6123` n `228`; crypto_major avg `-3.9853` n `8`; equity avg `-0.4408` n `73`; fx avg `0.0691` n `6`; index avg `0.0762` n `23`; metal avg `0.8048` n `18`; unknown avg `-0.2385` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
