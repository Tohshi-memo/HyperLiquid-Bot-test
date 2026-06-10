# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T19:07:33.483512+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0544` n `12`; crypto_alt avg `0.2717` n `228`; crypto_major avg `0.2042` n `8`; equity avg `0.06` n `74`; fx avg `-0.0096` n `6`; index avg `0.0622` n `23`; metal avg `-0.1203` n `18`; unknown avg `0.1267` n `550`
- 1h: commodity avg `-0.1823` n `12`; crypto_alt avg `-0.0076` n `228`; crypto_major avg `-0.2446` n `8`; equity avg `-0.625` n `74`; fx avg `-0.0142` n `6`; index avg `-0.3788` n `23`; metal avg `-0.4752` n `18`; unknown avg `0.4481` n `550`
- 4h: commodity avg `0.267` n `12`; crypto_alt avg `-1.0851` n `228`; crypto_major avg `-1.3388` n `8`; equity avg `-0.876` n `74`; fx avg `-0.0221` n `6`; index avg `-0.7201` n `23`; metal avg `-0.5483` n `18`; unknown avg `0.541` n `548`
- 24h: commodity avg `1.2532` n `12`; crypto_alt avg `-1.1702` n `228`; crypto_major avg `-2.0739` n `8`; equity avg `-1.2547` n `74`; fx avg `-0.0428` n `6`; index avg `-0.8962` n `23`; metal avg `-2.045` n `18`; unknown avg `-0.0493` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
