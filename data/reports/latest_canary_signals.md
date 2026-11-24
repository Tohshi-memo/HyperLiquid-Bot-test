# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T19:37:32.936524+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0166` n `13`; crypto_alt avg `-0.2758` n `239`; crypto_major avg `-0.2398` n `8`; equity avg `-0.213` n `168`; fx avg `-0.0016` n `6`; index avg `-0.024` n `27`; metal avg `0.0151` n `20`; unknown avg `-0.1378` n `1265`
- 1h: commodity avg `-0.1079` n `13`; crypto_alt avg `-0.47` n `239`; crypto_major avg `-0.5482` n `8`; equity avg `-0.3078` n `168`; fx avg `-0.0226` n `6`; index avg `-0.0285` n `27`; metal avg `-0.0094` n `20`; unknown avg `176.5077` n `1259`
- 4h: commodity avg `0.3039` n `13`; crypto_alt avg `-0.0593` n `239`; crypto_major avg `-0.2539` n `8`; equity avg `-0.0759` n `168`; fx avg `0.0086` n `6`; index avg `0.0438` n `27`; metal avg `-0.218` n `20`; unknown avg `179.0583` n `1227`
- 24h: commodity avg `0.7269` n `13`; crypto_alt avg `-2.9685` n `239`; crypto_major avg `-2.8554` n `8`; equity avg `-3.6773` n `167`; fx avg `0.2551` n `6`; index avg `-0.213` n `27`; metal avg `-1.0643` n `20`; unknown avg `196.7007` n `1113`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
