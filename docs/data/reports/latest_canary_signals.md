# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T06:22:31.403726+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0438` n `12`; crypto_alt avg `0.0904` n `230`; crypto_major avg `0.0946` n `8`; equity avg `0.2481` n `102`; fx avg `-0.0149` n `6`; index avg `0.1191` n `25`; metal avg `-0.014` n `20`; unknown avg `0.0121` n `777`
- 1h: commodity avg `0.0302` n `12`; crypto_alt avg `0.1325` n `230`; crypto_major avg `0.2339` n `8`; equity avg `0.1446` n `102`; fx avg `0.0424` n `6`; index avg `0.1037` n `25`; metal avg `0.024` n `20`; unknown avg `0.0147` n `761`
- 4h: commodity avg `-0.0644` n `12`; crypto_alt avg `-0.5807` n `230`; crypto_major avg `0.3349` n `8`; equity avg `-0.2293` n `102`; fx avg `-0.0675` n `6`; index avg `-0.0528` n `25`; metal avg `-0.0075` n `20`; unknown avg `0.1088` n `761`
- 24h: commodity avg `-0.1943` n `12`; crypto_alt avg `-1.4606` n `230`; crypto_major avg `0.8702` n `8`; equity avg `-1.7448` n `102`; fx avg `-0.1427` n `6`; index avg `-0.3346` n `25`; metal avg `-0.0317` n `20`; unknown avg `0.6253` n `758`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
