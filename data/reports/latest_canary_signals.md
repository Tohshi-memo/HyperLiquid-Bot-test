# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T03:52:31.304183+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `13`; crypto_alt avg `-0.283` n `239`; crypto_major avg `-0.2786` n `8`; equity avg `-0.2881` n `168`; fx avg `-0.0328` n `6`; index avg `-0.0329` n `27`; metal avg `-0.0448` n `20`; unknown avg `1.6975` n `1265`
- 1h: commodity avg `-0.0566` n `13`; crypto_alt avg `0.2038` n `239`; crypto_major avg `0.2418` n `8`; equity avg `0.3247` n `168`; fx avg `-0.0221` n `6`; index avg `0.0427` n `27`; metal avg `-0.0636` n `20`; unknown avg `20.7487` n `1259`
- 4h: commodity avg `-0.2532` n `13`; crypto_alt avg `-0.3439` n `239`; crypto_major avg `-0.8537` n `8`; equity avg `-1.1115` n `168`; fx avg `-0.0423` n `6`; index avg `-0.1159` n `27`; metal avg `-0.1198` n `20`; unknown avg `83.5081` n `1227`
- 24h: commodity avg `0.4551` n `13`; crypto_alt avg `-2.7126` n `239`; crypto_major avg `-2.4952` n `8`; equity avg `-4.9251` n `167`; fx avg `0.1648` n `6`; index avg `-0.497` n `27`; metal avg `-0.9533` n `20`; unknown avg `493.8372` n `1027`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
