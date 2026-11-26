# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T09:07:31.005745+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0286` n `13`; crypto_alt avg `0.0396` n `239`; crypto_major avg `-0.0206` n `8`; equity avg `-0.0862` n `168`; fx avg `-0.0043` n `6`; index avg `-0.0164` n `27`; metal avg `-0.0241` n `20`; unknown avg `39.8833` n `1257`
- 1h: commodity avg `-0.0711` n `13`; crypto_alt avg `0.2394` n `239`; crypto_major avg `0.3203` n `8`; equity avg `0.1465` n `168`; fx avg `-0.0137` n `6`; index avg `0.0198` n `27`; metal avg `0.1224` n `20`; unknown avg `88.5764` n `1165`
- 4h: commodity avg `-0.3123` n `13`; crypto_alt avg `0.0573` n `239`; crypto_major avg `-0.2105` n `8`; equity avg `-0.5626` n `168`; fx avg `0.0371` n `6`; index avg `-0.0717` n `27`; metal avg `-0.1174` n `20`; unknown avg `90.0388` n `1131`
- 24h: commodity avg `0.46` n `13`; crypto_alt avg `3.0336` n `239`; crypto_major avg `3.369` n `8`; equity avg `3.2762` n `168`; fx avg `0.0539` n `6`; index avg `0.2422` n `27`; metal avg `0.6883` n `20`; unknown avg `283.5357` n `997`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
