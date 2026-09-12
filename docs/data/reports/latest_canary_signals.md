# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T22:37:27.377931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0119` n `12`; crypto_alt avg `-0.2385` n `233`; crypto_major avg `-0.182` n `8`; equity avg `-0.0231` n `136`; fx avg `0.0011` n `6`; index avg `-0.0033` n `26`; metal avg `-0.0006` n `20`; unknown avg `0.047` n `838`
- 1h: commodity avg `0.0091` n `12`; crypto_alt avg `-0.1411` n `233`; crypto_major avg `-0.1062` n `8`; equity avg `-0.0488` n `136`; fx avg `0.0021` n `6`; index avg `-0.001` n `26`; metal avg `-0.0033` n `20`; unknown avg `-0.0044` n `810`
- 4h: commodity avg `0.0008` n `12`; crypto_alt avg `-0.3866` n `233`; crypto_major avg `-0.2032` n `8`; equity avg `-0.3139` n `136`; fx avg `0.0001` n `6`; index avg `-0.0337` n `26`; metal avg `-0.0243` n `20`; unknown avg `0.1709` n `788`
- 24h: commodity avg `-0.0806` n `12`; crypto_alt avg `1.5571` n `233`; crypto_major avg `0.3214` n `8`; equity avg `-0.2853` n `136`; fx avg `-0.0108` n `6`; index avg `-0.005` n `26`; metal avg `0.0002` n `20`; unknown avg `0.453` n `720`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0494`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0455`, n `668`, weak_sample_signal
