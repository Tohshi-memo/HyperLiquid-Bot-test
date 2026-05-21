# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T01:22:16.846262+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0278` n `12`; crypto_alt avg `-0.0124` n `228`; crypto_major avg `0.1546` n `8`; equity avg `0.1714` n `66`; fx avg `0.0053` n `6`; index avg `0.0651` n `23`; metal avg `0.4723` n `18`; unknown avg `0.4517` n `384`
- 1h: commodity avg `-0.3704` n `12`; crypto_alt avg `0.6265` n `228`; crypto_major avg `0.7385` n `8`; equity avg `0.5932` n `66`; fx avg `0.0257` n `6`; index avg `0.2825` n `23`; metal avg `0.672` n `18`; unknown avg `1.0646` n `384`
- 4h: commodity avg `-0.1843` n `12`; crypto_alt avg `0.7305` n `228`; crypto_major avg `1.4717` n `8`; equity avg `0.4878` n `66`; fx avg `0.0587` n `6`; index avg `0.1495` n `23`; metal avg `0.4861` n `18`; unknown avg `2.0676` n `384`
- 24h: commodity avg `-2.3764` n `12`; crypto_alt avg `3.6753` n `228`; crypto_major avg `3.7674` n `8`; equity avg `2.1812` n `66`; fx avg `-0.0216` n `6`; index avg `1.3816` n `23`; metal avg `1.7101` n `18`; unknown avg `3.5287` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0489`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0463`, n `668`, weak_sample_signal
