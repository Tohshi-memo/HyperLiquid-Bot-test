# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T09:52:37.152091+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `13`; crypto_alt avg `-0.1591` n `239`; crypto_major avg `-0.1379` n `8`; equity avg `-0.2588` n `168`; fx avg `0.0224` n `6`; index avg `-0.0201` n `27`; metal avg `-0.0563` n `20`; unknown avg `0.5338` n `1263`
- 1h: commodity avg `-0.0807` n `13`; crypto_alt avg `0.0317` n `239`; crypto_major avg `0.1678` n `8`; equity avg `-0.1343` n `168`; fx avg `0.012` n `6`; index avg `-0.0594` n `27`; metal avg `-0.0766` n `20`; unknown avg `1.7792` n `1239`
- 4h: commodity avg `-0.2295` n `13`; crypto_alt avg `0.0749` n `239`; crypto_major avg `0.2215` n `8`; equity avg `-0.0159` n `168`; fx avg `-0.0558` n `6`; index avg `-0.0589` n `27`; metal avg `0.2048` n `20`; unknown avg `2.304` n `1101`
- 24h: commodity avg `0.3488` n `13`; crypto_alt avg `2.0104` n `239`; crypto_major avg `2.7148` n `8`; equity avg `3.9824` n `168`; fx avg `-0.0873` n `6`; index avg `0.2946` n `27`; metal avg `1.2082` n `20`; unknown avg `373.2739` n `1025`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
