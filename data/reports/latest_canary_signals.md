# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T06:37:24.952072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0225` n `12`; crypto_alt avg `-0.0839` n `230`; crypto_major avg `-0.0573` n `8`; equity avg `-0.0672` n `96`; fx avg `-0.0033` n `6`; index avg `-0.014` n `25`; metal avg `0.0041` n `20`; unknown avg `0.0823` n `769`
- 1h: commodity avg `0.0397` n `12`; crypto_alt avg `-0.0894` n `230`; crypto_major avg `-0.1132` n `8`; equity avg `-0.1455` n `96`; fx avg `-0.0094` n `6`; index avg `-0.0282` n `25`; metal avg `-0.0156` n `20`; unknown avg `-0.0252` n `737`
- 4h: commodity avg `-0.0068` n `12`; crypto_alt avg `-0.5192` n `230`; crypto_major avg `-0.3578` n `8`; equity avg `-0.1704` n `96`; fx avg `-0.0067` n `6`; index avg `0.032` n `25`; metal avg `0.0023` n `20`; unknown avg `-0.0524` n `737`
- 24h: commodity avg `0.8946` n `12`; crypto_alt avg `-0.3608` n `230`; crypto_major avg `0.2878` n `8`; equity avg `0.9524` n `96`; fx avg `0.0086` n `6`; index avg `0.1402` n `25`; metal avg `0.1609` n `20`; unknown avg `0.2815` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
