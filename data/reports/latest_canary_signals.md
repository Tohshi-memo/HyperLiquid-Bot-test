# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T03:07:20.875053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.16` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0213` n `12`; crypto_alt avg `0.4448` n `228`; crypto_major avg `0.4983` n `8`; equity avg `0.003` n `69`; fx avg `0.0132` n `6`; index avg `-0.0111` n `23`; metal avg `0.2306` n `18`; unknown avg `-0.2509` n `422`
- 1h: commodity avg `0.0895` n `12`; crypto_alt avg `1.3493` n `228`; crypto_major avg `1.3966` n `8`; equity avg `0.4776` n `69`; fx avg `0.0179` n `6`; index avg `0.13` n `23`; metal avg `0.3964` n `18`; unknown avg `-0.1735` n `422`
- 4h: commodity avg `-0.2506` n `12`; crypto_alt avg `-0.4387` n `228`; crypto_major avg `-0.1039` n `8`; equity avg `-0.5344` n `69`; fx avg `0.0544` n `6`; index avg `-0.494` n `23`; metal avg `0.2391` n `18`; unknown avg `0.3838` n `422`
- 24h: commodity avg `-0.389` n `12`; crypto_alt avg `-1.3785` n `228`; crypto_major avg `-1.2498` n `8`; equity avg `-0.9347` n `69`; fx avg `0.009` n `6`; index avg `-0.837` n `23`; metal avg `-0.1145` n `18`; unknown avg `1.83` n `406`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
