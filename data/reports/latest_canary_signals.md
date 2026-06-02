# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T04:07:19.925095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.12` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.03` n `12`; crypto_alt avg `-0.1183` n `228`; crypto_major avg `-0.1326` n `8`; equity avg `0.2805` n `69`; fx avg `0.0001` n `6`; index avg `0.0669` n `23`; metal avg `0.159` n `18`; unknown avg `0.4612` n `422`
- 1h: commodity avg `-0.1845` n `12`; crypto_alt avg `0.3044` n `228`; crypto_major avg `-0.1795` n `8`; equity avg `0.4606` n `69`; fx avg `0.0101` n `6`; index avg `-0.031` n `23`; metal avg `0.1589` n `18`; unknown avg `0.7894` n `422`
- 4h: commodity avg `-0.259` n `12`; crypto_alt avg `-0.0752` n `228`; crypto_major avg `-0.099` n `8`; equity avg `0.2745` n `69`; fx avg `0.0279` n `6`; index avg `-0.4279` n `23`; metal avg `0.4798` n `18`; unknown avg `0.3426` n `422`
- 24h: commodity avg `-0.6241` n `12`; crypto_alt avg `-0.7585` n `228`; crypto_major avg `-1.1438` n `8`; equity avg `-0.375` n `69`; fx avg `0.0517` n `6`; index avg `-0.9235` n `23`; metal avg `0.2081` n `18`; unknown avg `2.1817` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
