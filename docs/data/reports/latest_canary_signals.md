# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T11:37:29.103700+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0431` n `12`; crypto_alt avg `-0.0176` n `228`; crypto_major avg `-0.0305` n `8`; equity avg `-0.0806` n `88`; fx avg `-0.0009` n `6`; index avg `-0.0155` n `23`; metal avg `0.0205` n `20`; unknown avg `-0.0253` n `765`
- 1h: commodity avg `0.0276` n `12`; crypto_alt avg `0.0657` n `228`; crypto_major avg `-0.1746` n `8`; equity avg `0.0321` n `88`; fx avg `-0.0077` n `6`; index avg `0.0292` n `23`; metal avg `0.3857` n `20`; unknown avg `0.2509` n `765`
- 4h: commodity avg `-0.2155` n `12`; crypto_alt avg `0.4327` n `228`; crypto_major avg `-0.4176` n `8`; equity avg `0.2938` n `88`; fx avg `0.0398` n `6`; index avg `0.0676` n `23`; metal avg `0.5797` n `20`; unknown avg `0.3013` n `765`
- 24h: commodity avg `-0.4618` n `12`; crypto_alt avg `0.4342` n `228`; crypto_major avg `-0.7154` n `8`; equity avg `0.6165` n `88`; fx avg `0.1444` n `6`; index avg `0.0214` n `23`; metal avg `-0.3657` n `20`; unknown avg `0.0324` n `743`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
