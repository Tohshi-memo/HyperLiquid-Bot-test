# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T16:37:25.361673+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `12`; crypto_alt avg `0.0942` n `231`; crypto_major avg `0.1549` n `8`; equity avg `0.0085` n `128`; fx avg `-0.0047` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0003` n `20`; unknown avg `-0.0268` n `792`
- 1h: commodity avg `0.0648` n `12`; crypto_alt avg `0.1445` n `231`; crypto_major avg `0.1728` n `8`; equity avg `0.0356` n `128`; fx avg `-0.004` n `6`; index avg `0.0016` n `26`; metal avg `0.0035` n `20`; unknown avg `-0.0812` n `788`
- 4h: commodity avg `-0.0162` n `12`; crypto_alt avg `0.9012` n `231`; crypto_major avg `0.9226` n `8`; equity avg `0.0508` n `128`; fx avg `-0.0013` n `6`; index avg `0.0055` n `26`; metal avg `0.0568` n `20`; unknown avg `0.3506` n `778`
- 24h: commodity avg `0.0312` n `12`; crypto_alt avg `0.7526` n `231`; crypto_major avg `0.301` n `8`; equity avg `0.1099` n `128`; fx avg `-0.0589` n `6`; index avg `-0.0022` n `26`; metal avg `-0.0488` n `20`; unknown avg `0.0108` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2172`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
