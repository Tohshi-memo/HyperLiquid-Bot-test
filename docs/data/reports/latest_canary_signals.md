# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T10:37:26.127142+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `12`; crypto_alt avg `0.0407` n `228`; crypto_major avg `-0.0149` n `8`; equity avg `0.0246` n `88`; fx avg `-0.0098` n `6`; index avg `0.0007` n `23`; metal avg `-0.0028` n `20`; unknown avg `-0.0185` n `764`
- 1h: commodity avg `0.0464` n `12`; crypto_alt avg `0.1819` n `228`; crypto_major avg `0.1537` n `8`; equity avg `0.0005` n `88`; fx avg `-0.0101` n `6`; index avg `-0.0001` n `23`; metal avg `-0.0024` n `20`; unknown avg `-0.0407` n `764`
- 4h: commodity avg `0.1201` n `12`; crypto_alt avg `-0.1494` n `228`; crypto_major avg `-0.1225` n `8`; equity avg `0.1166` n `88`; fx avg `-0.0002` n `6`; index avg `0.0021` n `23`; metal avg `-0.0333` n `20`; unknown avg `-0.2519` n `748`
- 24h: commodity avg `0.1633` n `12`; crypto_alt avg `1.6357` n `228`; crypto_major avg `1.7141` n `8`; equity avg `1.9472` n `87`; fx avg `0.0193` n `6`; index avg `0.0916` n `23`; metal avg `0.3666` n `20`; unknown avg `-0.0242` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2057`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
