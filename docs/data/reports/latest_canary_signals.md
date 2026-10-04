# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T05:53:25.284442+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `13`; crypto_alt avg `-0.0555` n `235`; crypto_major avg `0.0201` n `8`; equity avg `0.0036` n `143`; fx avg `-0.002` n `6`; index avg `0.0042` n `26`; metal avg `0.0019` n `20`; unknown avg `-0.1863` n `1079`
- 1h: commodity avg `0.0177` n `13`; crypto_alt avg `0.1524` n `235`; crypto_major avg `0.1127` n `8`; equity avg `0.0101` n `143`; fx avg `-0.0215` n `6`; index avg `0.0065` n `26`; metal avg `0.0002` n `20`; unknown avg `0.0563` n `1077`
- 4h: commodity avg `-0.0426` n `13`; crypto_alt avg `0.6792` n `235`; crypto_major avg `0.2116` n `8`; equity avg `0.0709` n `143`; fx avg `-0.0198` n `6`; index avg `0.0062` n `26`; metal avg `0.0103` n `20`; unknown avg `-0.0122` n `1071`
- 24h: commodity avg `0.1991` n `13`; crypto_alt avg `1.8068` n `235`; crypto_major avg `0.8531` n `8`; equity avg `0.2728` n `143`; fx avg `-0.0315` n `6`; index avg `0.0136` n `26`; metal avg `0.008` n `20`; unknown avg `0.3939` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.19`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
