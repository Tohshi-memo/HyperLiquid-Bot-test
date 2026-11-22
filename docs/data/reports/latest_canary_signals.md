# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T22:22:26.869435+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0133` n `13`; crypto_alt avg `-0.1787` n `239`; crypto_major avg `-0.1021` n `8`; equity avg `-0.1459` n `166`; fx avg `0.0013` n `6`; index avg `-0.0495` n `27`; metal avg `-0.0146` n `20`; unknown avg `-0.0607` n `1256`
- 1h: commodity avg `-0.0287` n `13`; crypto_alt avg `-0.3642` n `239`; crypto_major avg `-0.2955` n `8`; equity avg `-0.158` n `166`; fx avg `0.1011` n `6`; index avg `-0.0124` n `27`; metal avg `0.0043` n `20`; unknown avg `169.9991` n `1242`
- 4h: commodity avg `-0.0311` n `13`; crypto_alt avg `-0.0737` n `239`; crypto_major avg `-0.088` n `8`; equity avg `-0.1839` n `166`; fx avg `0.0944` n `6`; index avg `-0.0516` n `27`; metal avg `-0.0942` n `20`; unknown avg `-0.0927` n `1210`
- 24h: commodity avg `-0.141` n `13`; crypto_alt avg `0.4913` n `239`; crypto_major avg `0.6327` n `8`; equity avg `0.5939` n `166`; fx avg `0.0873` n `6`; index avg `0.0593` n `27`; metal avg `0.002` n `20`; unknown avg `240.3125` n `1048`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
