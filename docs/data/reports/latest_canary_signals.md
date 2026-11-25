# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T06:07:24.136423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1192` n `13`; crypto_alt avg `-0.1174` n `239`; crypto_major avg `-0.1717` n `8`; equity avg `-0.1014` n `168`; fx avg `-0.0036` n `6`; index avg `-0.0063` n `27`; metal avg `-0.0357` n `20`; unknown avg `22.9741` n `1233`
- 1h: commodity avg `0.0887` n `13`; crypto_alt avg `-0.1758` n `239`; crypto_major avg `-0.2054` n `8`; equity avg `-0.4184` n `168`; fx avg `0.0058` n `6`; index avg `-0.0404` n `27`; metal avg `-0.2481` n `20`; unknown avg `1.0584` n `1233`
- 4h: commodity avg `0.0067` n `13`; crypto_alt avg `0.7945` n `239`; crypto_major avg `0.1046` n `8`; equity avg `-0.9532` n `168`; fx avg `-0.047` n `6`; index avg `-0.0288` n `27`; metal avg `-0.4746` n `20`; unknown avg `26.2452` n `1221`
- 24h: commodity avg `0.6338` n `13`; crypto_alt avg `-3.3744` n `239`; crypto_major avg `-3.3641` n `8`; equity avg `-5.4102` n `167`; fx avg `0.1279` n `6`; index avg `-0.5095` n `27`; metal avg `-1.0558` n `20`; unknown avg `695.7838` n `1029`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
