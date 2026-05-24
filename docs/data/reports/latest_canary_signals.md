# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T20:22:18.263779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0752` n `12`; crypto_alt avg `-0.0505` n `228`; crypto_major avg `0.029` n `8`; equity avg `0.0029` n `67`; fx avg `0.0065` n `6`; index avg `0.0017` n `23`; metal avg `-0.0053` n `18`; unknown avg `-0.01` n `396`
- 1h: commodity avg `-0.0847` n `12`; crypto_alt avg `-0.3031` n `228`; crypto_major avg `-0.2839` n `8`; equity avg `0.0708` n `67`; fx avg `0.0349` n `6`; index avg `-0.0373` n `23`; metal avg `-0.0402` n `18`; unknown avg `-0.0121` n `396`
- 4h: commodity avg `0.3469` n `12`; crypto_alt avg `-0.4407` n `228`; crypto_major avg `-0.3772` n `8`; equity avg `0.1685` n `67`; fx avg `0.0452` n `6`; index avg `0.0378` n `23`; metal avg `-0.1907` n `18`; unknown avg `-0.3921` n `396`
- 24h: commodity avg `0.2257` n `12`; crypto_alt avg `-0.8612` n `228`; crypto_major avg `1.0347` n `8`; equity avg `1.1209` n `67`; fx avg `0.1429` n `6`; index avg `0.1906` n `23`; metal avg `0.3034` n `18`; unknown avg `0.4` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
