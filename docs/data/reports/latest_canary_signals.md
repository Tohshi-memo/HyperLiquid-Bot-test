# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T23:22:28.193320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `12`; crypto_alt avg `0.1955` n `228`; crypto_major avg `0.0441` n `8`; equity avg `-0.0913` n `86`; fx avg `-0.0118` n `6`; index avg `-0.0116` n `23`; metal avg `0.0056` n `20`; unknown avg `0.2159` n `716`
- 1h: commodity avg `-0.0084` n `12`; crypto_alt avg `-0.5257` n `228`; crypto_major avg `-0.3742` n `8`; equity avg `-0.2847` n `86`; fx avg `0.0262` n `6`; index avg `-0.0362` n `23`; metal avg `-0.0399` n `20`; unknown avg `-0.0256` n `716`
- 4h: commodity avg `-0.0438` n `12`; crypto_alt avg `-0.8791` n `228`; crypto_major avg `-0.6903` n `8`; equity avg `-0.1493` n `86`; fx avg `0.0018` n `6`; index avg `-0.0019` n `23`; metal avg `0.0008` n `20`; unknown avg `-0.0957` n `708`
- 24h: commodity avg `-0.8798` n `12`; crypto_alt avg `-0.481` n `228`; crypto_major avg `-0.1526` n `8`; equity avg `-0.4596` n `85`; fx avg `0.1045` n `6`; index avg `0.1809` n `23`; metal avg `0.2838` n `18`; unknown avg `0.4316` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
