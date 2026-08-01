# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T18:07:24.491635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0099` n `12`; crypto_alt avg `0.1076` n `230`; crypto_major avg `0.0787` n `8`; equity avg `-0.0118` n `102`; fx avg `-0.0046` n `6`; index avg `-0.0017` n `25`; metal avg `-0.0065` n `20`; unknown avg `0.0751` n `782`
- 1h: commodity avg `0.0026` n `12`; crypto_alt avg `-0.4391` n `230`; crypto_major avg `-0.5258` n `8`; equity avg `-0.1034` n `102`; fx avg `-0.0091` n `6`; index avg `-0.0253` n `25`; metal avg `-0.0256` n `20`; unknown avg `0.0315` n `782`
- 4h: commodity avg `0.13` n `12`; crypto_alt avg `-0.5652` n `230`; crypto_major avg `-0.5825` n `8`; equity avg `-0.1841` n `102`; fx avg `-0.0127` n `6`; index avg `-0.0215` n `25`; metal avg `-0.0192` n `20`; unknown avg `-0.0212` n `782`
- 24h: commodity avg `0.6113` n `12`; crypto_alt avg `-0.6896` n `230`; crypto_major avg `-1.2508` n `8`; equity avg `-1.2953` n `102`; fx avg `-0.1241` n `6`; index avg `-0.1554` n `25`; metal avg `-0.0856` n `20`; unknown avg `4.2632` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
