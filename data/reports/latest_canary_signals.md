# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T03:52:25.470469+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.0336` n `228`; crypto_major avg `0.0428` n `8`; equity avg `0.0612` n `78`; fx avg `-0.0188` n `6`; index avg `-0.0065` n `23`; metal avg `0.0067` n `18`; unknown avg `1.8169` n `687`
- 1h: commodity avg `0.0326` n `12`; crypto_alt avg `0.1303` n `228`; crypto_major avg `0.202` n `8`; equity avg `0.0899` n `78`; fx avg `-0.0108` n `6`; index avg `-0.016` n `23`; metal avg `-0.0293` n `18`; unknown avg `1.8233` n `687`
- 4h: commodity avg `0.0722` n `12`; crypto_alt avg `-0.2487` n `228`; crypto_major avg `0.0454` n `8`; equity avg `0.15` n `78`; fx avg `-0.0054` n `6`; index avg `0.0026` n `23`; metal avg `-0.0508` n `18`; unknown avg `-0.4455` n `679`
- 24h: commodity avg `0.455` n `12`; crypto_alt avg `-3.7663` n `228`; crypto_major avg `-4.4264` n `8`; equity avg `1.0503` n `78`; fx avg `-0.0944` n `6`; index avg `0.2905` n `23`; metal avg `-4.1577` n `18`; unknown avg `-0.3707` n `556`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0435`, n `668`, weak_sample_signal
