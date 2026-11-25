# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T15:37:31.229880+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1082` n `13`; crypto_alt avg `0.7386` n `239`; crypto_major avg `0.9503` n `8`; equity avg `0.7661` n `168`; fx avg `0.0164` n `6`; index avg `0.0711` n `27`; metal avg `0.1945` n `20`; unknown avg `316.222` n `1266`
- 1h: commodity avg `0.1832` n `13`; crypto_alt avg `0.9219` n `239`; crypto_major avg `1.314` n `8`; equity avg `0.5885` n `168`; fx avg `0.02` n `6`; index avg `0.0633` n `27`; metal avg `-0.1077` n `20`; unknown avg `202.2249` n `1259`
- 4h: commodity avg `0.4039` n `13`; crypto_alt avg `-0.4843` n `239`; crypto_major avg `0.0375` n `8`; equity avg `-1.323` n `168`; fx avg `0.0496` n `6`; index avg `-0.0945` n `27`; metal avg `-0.4438` n `20`; unknown avg `201.7777` n `1239`
- 24h: commodity avg `0.5891` n `13`; crypto_alt avg `-1.5465` n `239`; crypto_major avg `-2.2274` n `8`; equity avg `-4.8866` n `168`; fx avg `-0.0269` n `6`; index avg `-0.4686` n `27`; metal avg `-1.1964` n `20`; unknown avg `819.4406` n `1067`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
