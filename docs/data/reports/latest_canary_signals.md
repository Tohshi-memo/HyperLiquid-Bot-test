# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T04:22:26.749108+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `12`; crypto_alt avg `-0.1263` n `230`; crypto_major avg `-0.0552` n `8`; equity avg `-0.0726` n `94`; fx avg `0.0059` n `6`; index avg `-0.0448` n `25`; metal avg `-0.0097` n `20`; unknown avg `-0.0757` n `768`
- 1h: commodity avg `-0.0074` n `12`; crypto_alt avg `-0.1953` n `230`; crypto_major avg `-0.2126` n `8`; equity avg `-0.1565` n `94`; fx avg `0.0005` n `6`; index avg `-0.0088` n `25`; metal avg `0.057` n `20`; unknown avg `-0.1222` n `768`
- 4h: commodity avg `-0.0459` n `12`; crypto_alt avg `-0.1954` n `230`; crypto_major avg `-0.2792` n `8`; equity avg `-0.0844` n `94`; fx avg `-0.0181` n `6`; index avg `-0.0699` n `25`; metal avg `-0.1605` n `20`; unknown avg `-0.5995` n `768`
- 24h: commodity avg `-0.0768` n `12`; crypto_alt avg `0.0585` n `230`; crypto_major avg `-0.0286` n `8`; equity avg `-2.489` n `93`; fx avg `0.1095` n `6`; index avg `-0.4816` n `25`; metal avg `0.0338` n `20`; unknown avg `-0.1733` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
