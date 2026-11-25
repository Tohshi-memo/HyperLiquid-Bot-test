# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T07:52:29.526662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0229` n `13`; crypto_alt avg `0.492` n `239`; crypto_major avg `0.2443` n `8`; equity avg `0.3294` n `168`; fx avg `0.0124` n `6`; index avg `0.0219` n `27`; metal avg `0.015` n `20`; unknown avg `159.2164` n `1263`
- 1h: commodity avg `-0.1389` n `13`; crypto_alt avg `-0.7001` n `239`; crypto_major avg `-1.0102` n `8`; equity avg `-0.8892` n `168`; fx avg `-0.026` n `6`; index avg `-0.0952` n `27`; metal avg `0.0154` n `20`; unknown avg `0.3681` n `1255`
- 4h: commodity avg `-0.2424` n `13`; crypto_alt avg `0.4103` n `239`; crypto_major avg `-0.9096` n `8`; equity avg `-1.4884` n `168`; fx avg `-0.0571` n `6`; index avg `-0.1289` n `27`; metal avg `-0.248` n `20`; unknown avg `1.9562` n `1217`
- 24h: commodity avg `0.0455` n `13`; crypto_alt avg `-3.1806` n `239`; crypto_major avg `-3.6677` n `8`; equity avg `-6.2129` n `167`; fx avg `0.0679` n `6`; index avg `-0.6071` n `27`; metal avg `-1.1084` n `20`; unknown avg `694.0562` n `1027`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
