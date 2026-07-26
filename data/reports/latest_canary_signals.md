# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T23:52:27.276329+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0196` n `12`; crypto_alt avg `0.0298` n `230`; crypto_major avg `0.0337` n `8`; equity avg `0.1605` n `100`; fx avg `-0.0184` n `6`; index avg `0.0616` n `25`; metal avg `0.0771` n `20`; unknown avg `-0.0835` n `775`
- 1h: commodity avg `0.0077` n `12`; crypto_alt avg `0.0713` n `230`; crypto_major avg `0.0574` n `8`; equity avg `0.2401` n `100`; fx avg `-0.0233` n `6`; index avg `0.0931` n `25`; metal avg `0.0026` n `20`; unknown avg `-0.1429` n `775`
- 4h: commodity avg `-0.3637` n `12`; crypto_alt avg `0.9551` n `230`; crypto_major avg `1.1001` n `8`; equity avg `0.741` n `100`; fx avg `-0.0248` n `6`; index avg `0.2054` n `25`; metal avg `0.2151` n `20`; unknown avg `0.1645` n `775`
- 24h: commodity avg `-0.5435` n `12`; crypto_alt avg `1.8775` n `230`; crypto_major avg `2.0597` n `8`; equity avg `1.2593` n `100`; fx avg `0.0132` n `6`; index avg `0.29` n `25`; metal avg `0.4315` n `20`; unknown avg `0.1364` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1811`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.167`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
