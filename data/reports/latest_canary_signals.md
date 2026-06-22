# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T00:52:30.066792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.056` n `12`; crypto_alt avg `0.0569` n `228`; crypto_major avg `-0.1651` n `8`; equity avg `0.1373` n `78`; fx avg `0.0111` n `6`; index avg `0.0465` n `23`; metal avg `0.2161` n `18`; unknown avg `-0.125` n `702`
- 1h: commodity avg `-0.0146` n `12`; crypto_alt avg `1.0446` n `228`; crypto_major avg `0.7548` n `8`; equity avg `0.204` n `78`; fx avg `0.0179` n `6`; index avg `0.166` n `23`; metal avg `0.625` n `18`; unknown avg `0.4977` n `702`
- 4h: commodity avg `-0.1146` n `12`; crypto_alt avg `-0.1137` n `228`; crypto_major avg `-0.1896` n `8`; equity avg `-0.5699` n `78`; fx avg `0.049` n `6`; index avg `-0.0076` n `23`; metal avg `0.4362` n `18`; unknown avg `-0.0694` n `702`
- 24h: commodity avg `0.0835` n `12`; crypto_alt avg `0.0265` n `228`; crypto_major avg `-0.9494` n `8`; equity avg `-0.5499` n `78`; fx avg `-0.0825` n `6`; index avg `-0.0016` n `23`; metal avg `0.3179` n `18`; unknown avg `1.3278` n `645`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
