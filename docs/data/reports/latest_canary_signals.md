# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T03:52:25.697280+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.102` n `12`; crypto_alt avg `0.0126` n `228`; crypto_major avg `-0.0171` n `8`; equity avg `0.0243` n `74`; fx avg `0.0039` n `6`; index avg `-0.0118` n `23`; metal avg `-0.0855` n `18`; unknown avg `0.2806` n `557`
- 1h: commodity avg `-0.0914` n `12`; crypto_alt avg `-0.0526` n `228`; crypto_major avg `-0.2053` n `8`; equity avg `-0.0199` n `74`; fx avg `0.0132` n `6`; index avg `-0.0461` n `23`; metal avg `0.1167` n `18`; unknown avg `-0.0881` n `557`
- 4h: commodity avg `0.2521` n `12`; crypto_alt avg `0.342` n `228`; crypto_major avg `0.088` n `8`; equity avg `0.132` n `74`; fx avg `0.0265` n `6`; index avg `-0.2309` n `23`; metal avg `0.0426` n `18`; unknown avg `-0.3109` n `556`
- 24h: commodity avg `-2.4913` n `12`; crypto_alt avg `2.6797` n `228`; crypto_major avg `2.6429` n `8`; equity avg `3.9258` n `74`; fx avg `0.0237` n `6`; index avg `2.0019` n `23`; metal avg `3.4751` n `18`; unknown avg `1.8926` n `530`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
