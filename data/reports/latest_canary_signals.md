# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T08:52:27.005571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0112` n `12`; crypto_alt avg `0.0589` n `228`; crypto_major avg `0.0962` n `8`; equity avg `-0.0155` n `86`; fx avg `0.0111` n `6`; index avg `-0.0007` n `23`; metal avg `-0.062` n `20`; unknown avg `-0.0617` n `764`
- 1h: commodity avg `-0.037` n `12`; crypto_alt avg `0.2458` n `228`; crypto_major avg `0.2372` n `8`; equity avg `0.0959` n `86`; fx avg `-0.0068` n `6`; index avg `0.035` n `23`; metal avg `-0.1281` n `20`; unknown avg `-0.0128` n `764`
- 4h: commodity avg `-0.0734` n `12`; crypto_alt avg `0.2566` n `228`; crypto_major avg `0.245` n `8`; equity avg `0.3848` n `86`; fx avg `0.0468` n `6`; index avg `0.1477` n `23`; metal avg `0.0852` n `20`; unknown avg `0.0037` n `740`
- 24h: commodity avg `-0.5436` n `12`; crypto_alt avg `0.5573` n `228`; crypto_major avg `0.3971` n `8`; equity avg `5.1411` n `86`; fx avg `-0.0265` n `6`; index avg `0.1316` n `23`; metal avg `-0.3084` n `20`; unknown avg `-0.011` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
