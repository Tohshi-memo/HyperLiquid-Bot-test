# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T20:28:10.305580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0219` n `12`; crypto_alt avg `0.0947` n `228`; crypto_major avg `0.2447` n `8`; equity avg `-0.0241` n `74`; fx avg `-0.0112` n `6`; index avg `-0.0156` n `23`; metal avg `-0.0504` n `18`; unknown avg `-0.0798` n `424`
- 1h: commodity avg `-0.1388` n `12`; crypto_alt avg `-0.9814` n `228`; crypto_major avg `-0.6236` n `8`; equity avg `-0.6118` n `74`; fx avg `-0.0157` n `6`; index avg `-0.1679` n `23`; metal avg `-0.1052` n `18`; unknown avg `-0.1689` n `424`
- 4h: commodity avg `0.0626` n `12`; crypto_alt avg `-0.9444` n `228`; crypto_major avg `-0.6122` n `8`; equity avg `-0.6652` n `74`; fx avg `-0.0546` n `6`; index avg `0.0686` n `23`; metal avg `-0.0991` n `18`; unknown avg `0.8403` n `424`
- 24h: commodity avg `-0.7959` n `12`; crypto_alt avg `-5.3306` n `228`; crypto_major avg `-3.7119` n `8`; equity avg `-1.323` n `73`; fx avg `0.0029` n `6`; index avg `-0.0498` n `23`; metal avg `0.8859` n `18`; unknown avg `-0.1584` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
