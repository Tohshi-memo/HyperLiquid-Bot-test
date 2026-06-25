# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T22:07:27.881229+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0015` n `12`; crypto_alt avg `0.1878` n `228`; crypto_major avg `0.0812` n `8`; equity avg `-0.1072` n `86`; fx avg `-0.0055` n `6`; index avg `-0.0322` n `23`; metal avg `-0.0677` n `20`; unknown avg `-0.3157` n `765`
- 1h: commodity avg `0.0288` n `12`; crypto_alt avg `0.9761` n `228`; crypto_major avg `1.0117` n `8`; equity avg `-0.143` n `86`; fx avg `-0.0021` n `6`; index avg `-0.0449` n `23`; metal avg `-0.0207` n `20`; unknown avg `0.8807` n `765`
- 4h: commodity avg `-0.1894` n `12`; crypto_alt avg `0.6158` n `228`; crypto_major avg `0.5147` n `8`; equity avg `-0.0934` n `86`; fx avg `-0.0121` n `6`; index avg `-0.0339` n `23`; metal avg `-0.095` n `20`; unknown avg `0.7798` n `765`
- 24h: commodity avg `0.4036` n `12`; crypto_alt avg `-1.2391` n `228`; crypto_major avg `-1.1939` n `8`; equity avg `-2.2717` n `86`; fx avg `0.1432` n `6`; index avg `-0.1994` n `23`; metal avg `0.2554` n `20`; unknown avg `0.7109` n `700`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
