# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T15:52:33.634263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.8` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.8525` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0047` n `12`; crypto_alt avg `-0.1779` n `230`; crypto_major avg `-0.1311` n `8`; equity avg `-0.2088` n `102`; fx avg `-0.0416` n `6`; index avg `-0.0279` n `25`; metal avg `0.0152` n `20`; unknown avg `-0.0665` n `778`
- 1h: commodity avg `-0.0832` n `12`; crypto_alt avg `-0.1088` n `230`; crypto_major avg `-0.1397` n `8`; equity avg `-0.1923` n `102`; fx avg `-0.0667` n `6`; index avg `0.0427` n `25`; metal avg `0.0692` n `20`; unknown avg `-0.0348` n `778`
- 4h: commodity avg `0.5572` n `12`; crypto_alt avg `-0.6847` n `230`; crypto_major avg `-0.6693` n `8`; equity avg `-2.5218` n `102`; fx avg `-0.0624` n `6`; index avg `-0.3643` n `25`; metal avg `-0.16` n `20`; unknown avg `0.5904` n `777`
- 24h: commodity avg `1.3399` n `12`; crypto_alt avg `-2.5928` n `230`; crypto_major avg `-0.504` n `8`; equity avg `-2.3341` n `102`; fx avg `-0.108` n `6`; index avg `-0.5268` n `25`; metal avg `-0.3478` n `20`; unknown avg `-0.0016` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
