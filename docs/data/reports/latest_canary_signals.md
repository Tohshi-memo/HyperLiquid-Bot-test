# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T05:22:26.323001+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0753` n `13`; crypto_alt avg `-0.1177` n `239`; crypto_major avg `-0.1871` n `8`; equity avg `-0.2249` n `168`; fx avg `0.0038` n `6`; index avg `-0.0306` n `27`; metal avg `-0.0128` n `20`; unknown avg `-0.1466` n `1263`
- 1h: commodity avg `-0.0609` n `13`; crypto_alt avg `-0.0176` n `239`; crypto_major avg `-0.3233` n `8`; equity avg `-0.6195` n `168`; fx avg `-0.0263` n `6`; index avg `-0.056` n `27`; metal avg `-0.1102` n `20`; unknown avg `-0.1597` n `1259`
- 4h: commodity avg `-0.2264` n `13`; crypto_alt avg `0.5529` n `239`; crypto_major avg `-0.5533` n `8`; equity avg `-1.3662` n `168`; fx avg `-0.0349` n `6`; index avg `-0.1042` n `27`; metal avg `0.0058` n `20`; unknown avg `25.3583` n `1247`
- 24h: commodity avg `0.5567` n `13`; crypto_alt avg `-3.2626` n `239`; crypto_major avg `-3.536` n `8`; equity avg `-5.4832` n `167`; fx avg `0.1353` n `6`; index avg `-0.5379` n `27`; metal avg `-0.9865` n `20`; unknown avg `507.1572` n `1027`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
