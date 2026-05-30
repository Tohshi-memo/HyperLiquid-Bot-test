# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T04:07:30.437565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0756` n `12`; crypto_alt avg `-0.3127` n `228`; crypto_major avg `-0.2223` n `8`; equity avg `-0.0146` n `69`; fx avg `-0.0006` n `6`; index avg `-0.0143` n `23`; metal avg `-0.0354` n `18`; unknown avg `0.5876` n `419`
- 1h: commodity avg `0.0909` n `12`; crypto_alt avg `-0.7683` n `228`; crypto_major avg `-0.4913` n `8`; equity avg `-0.0635` n `69`; fx avg `0.0014` n `6`; index avg `-0.0046` n `23`; metal avg `-0.0535` n `18`; unknown avg `0.5638` n `419`
- 4h: commodity avg `-0.0744` n `12`; crypto_alt avg `0.7997` n `228`; crypto_major avg `0.7554` n `8`; equity avg `0.3209` n `69`; fx avg `0.0017` n `6`; index avg `-0.0834` n `23`; metal avg `-0.026` n `18`; unknown avg `-0.7655` n `419`
- 24h: commodity avg `-0.173` n `12`; crypto_alt avg `2.1183` n `228`; crypto_major avg `2.0786` n `8`; equity avg `1.0316` n `69`; fx avg `0.1067` n `6`; index avg `0.0944` n `23`; metal avg `0.093` n `18`; unknown avg `1.5747` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1877`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
