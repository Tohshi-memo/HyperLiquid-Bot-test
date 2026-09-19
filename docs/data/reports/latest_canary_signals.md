# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T05:22:30.420459+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `0.0121` n `234`; crypto_major avg `0.0031` n `8`; equity avg `-0.014` n `140`; fx avg `-0.0034` n `6`; index avg `-0.0193` n `26`; metal avg `-0.0039` n `20`; unknown avg `-0.0819` n `942`
- 1h: commodity avg `-0.0132` n `12`; crypto_alt avg `-0.4087` n `234`; crypto_major avg `-0.2282` n `8`; equity avg `-0.0659` n `140`; fx avg `-0.0135` n `6`; index avg `-0.0046` n `26`; metal avg `-0.0066` n `20`; unknown avg `0.0565` n `940`
- 4h: commodity avg `-0.0462` n `12`; crypto_alt avg `0.4139` n `234`; crypto_major avg `0.2745` n `8`; equity avg `-0.0853` n `140`; fx avg `-0.013` n `6`; index avg `-0.0356` n `26`; metal avg `0.0064` n `20`; unknown avg `0.3182` n `914`
- 24h: commodity avg `0.1133` n `12`; crypto_alt avg `3.9517` n `234`; crypto_major avg `4.5871` n `8`; equity avg `0.4749` n `140`; fx avg `0.0049` n `6`; index avg `-0.0279` n `26`; metal avg `0.0036` n `20`; unknown avg `2.4501` n `767`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
