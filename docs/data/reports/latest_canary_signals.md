# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T21:07:27.883886+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0063` n `13`; crypto_alt avg `-0.0057` n `239`; crypto_major avg `0.0792` n `8`; equity avg `0.0764` n `168`; fx avg `0.0014` n `6`; index avg `0.0041` n `27`; metal avg `0.02` n `20`; unknown avg `41.2426` n `1217`
- 1h: commodity avg `-0.0041` n `13`; crypto_alt avg `0.0099` n `239`; crypto_major avg `0.1696` n `8`; equity avg `0.127` n `168`; fx avg `0.0` n `6`; index avg `0.0087` n `27`; metal avg `0.0383` n `20`; unknown avg `1.2701` n `1199`
- 4h: commodity avg `0.1196` n `13`; crypto_alt avg `0.6007` n `239`; crypto_major avg `0.9266` n `8`; equity avg `0.3838` n `168`; fx avg `-0.0042` n `6`; index avg `0.0359` n `27`; metal avg `0.0041` n `20`; unknown avg `46.4542` n `1181`
- 24h: commodity avg `0.0572` n `13`; crypto_alt avg `1.6518` n `239`; crypto_major avg `0.9697` n `8`; equity avg `1.2178` n `168`; fx avg `-0.0209` n `6`; index avg `0.0743` n `27`; metal avg `0.1269` n `20`; unknown avg `17.4562` n `1019`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
