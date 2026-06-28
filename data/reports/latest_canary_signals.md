# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T22:37:27.668132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0051` n `12`; crypto_alt avg `-0.0249` n `228`; crypto_major avg `-0.0641` n `8`; equity avg `0.0687` n `88`; fx avg `0.0028` n `6`; index avg `0.0176` n `23`; metal avg `-0.0274` n `20`; unknown avg `-0.0042` n `764`
- 1h: commodity avg `-0.1148` n `12`; crypto_alt avg `-0.2382` n `228`; crypto_major avg `-0.4977` n `8`; equity avg `0.095` n `88`; fx avg `-0.0085` n `6`; index avg `0.0457` n `23`; metal avg `-0.2401` n `20`; unknown avg `0.0633` n `764`
- 4h: commodity avg `-0.3283` n `12`; crypto_alt avg `-0.5031` n `228`; crypto_major avg `-0.5263` n `8`; equity avg `0.2687` n `88`; fx avg `-0.0582` n `6`; index avg `0.1172` n `23`; metal avg `-0.2051` n `20`; unknown avg `0.3008` n `764`
- 24h: commodity avg `-0.1516` n `12`; crypto_alt avg `-0.7753` n `228`; crypto_major avg `-1.3285` n `8`; equity avg `0.3515` n `88`; fx avg `-0.0991` n `6`; index avg `0.1351` n `23`; metal avg `-0.1968` n `20`; unknown avg `15.1242` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1894`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1808`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
