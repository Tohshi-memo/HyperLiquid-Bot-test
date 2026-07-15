# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T22:07:32.356594+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0334` n `12`; crypto_alt avg `-0.0227` n `230`; crypto_major avg `0.0109` n `8`; equity avg `0.0354` n `94`; fx avg `-0.0044` n `6`; index avg `0.0307` n `25`; metal avg `0.0191` n `20`; unknown avg `0.0252` n `768`
- 1h: commodity avg `-0.0238` n `12`; crypto_alt avg `0.0243` n `230`; crypto_major avg `-0.0034` n `8`; equity avg `0.0828` n `94`; fx avg `-0.0073` n `6`; index avg `0.0299` n `25`; metal avg `0.0124` n `20`; unknown avg `0.0683` n `768`
- 4h: commodity avg `0.1677` n `12`; crypto_alt avg `-0.1253` n `230`; crypto_major avg `-0.325` n `8`; equity avg `-0.158` n `94`; fx avg `0.0022` n `6`; index avg `0.0051` n `25`; metal avg `0.1001` n `20`; unknown avg `-0.1397` n `768`
- 24h: commodity avg `0.0402` n `12`; crypto_alt avg `0.5315` n `230`; crypto_major avg `0.7514` n `8`; equity avg `-0.4967` n `93`; fx avg `0.2145` n `6`; index avg `-0.1145` n `25`; metal avg `0.1613` n `20`; unknown avg `0.0725` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
