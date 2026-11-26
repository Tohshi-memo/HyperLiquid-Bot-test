# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T08:37:28.036282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0309` n `13`; crypto_alt avg `0.0443` n `239`; crypto_major avg `0.1045` n `8`; equity avg `0.1107` n `168`; fx avg `-0.0036` n `6`; index avg `0.0185` n `27`; metal avg `0.0579` n `20`; unknown avg `0.7935` n `1199`
- 1h: commodity avg `0.0885` n `13`; crypto_alt avg `0.1279` n `239`; crypto_major avg `0.0641` n `8`; equity avg `-0.176` n `168`; fx avg `-0.0111` n `6`; index avg `-0.0115` n `27`; metal avg `-0.0097` n `20`; unknown avg `0.3573` n `1151`
- 4h: commodity avg `-0.2118` n `13`; crypto_alt avg `-0.2876` n `239`; crypto_major avg `-0.513` n `8`; equity avg `-0.9167` n `168`; fx avg `0.0304` n `6`; index avg `-0.0841` n `27`; metal avg `-0.2296` n `20`; unknown avg `0.3556` n `1133`
- 24h: commodity avg `0.7447` n `13`; crypto_alt avg `2.8565` n `239`; crypto_major avg `2.9179` n `8`; equity avg `2.3547` n `168`; fx avg `0.0521` n `6`; index avg `0.148` n `27`; metal avg `0.5577` n `20`; unknown avg `-0.3279` n `993`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
