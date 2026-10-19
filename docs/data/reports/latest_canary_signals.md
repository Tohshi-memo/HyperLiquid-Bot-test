# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T12:37:24.392058+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0163` n `13`; crypto_alt avg `0.1572` n `237`; crypto_major avg `0.1146` n `8`; equity avg `0.0605` n `151`; fx avg `-0.0137` n `6`; index avg `0.0044` n `26`; metal avg `-0.0212` n `20`; unknown avg `0.044` n `1189`
- 1h: commodity avg `-0.0972` n `13`; crypto_alt avg `0.8457` n `237`; crypto_major avg `0.6863` n `8`; equity avg `0.6201` n `151`; fx avg `-0.0054` n `6`; index avg `0.0603` n `26`; metal avg `-0.05` n `20`; unknown avg `0.1988` n `1171`
- 4h: commodity avg `0.2585` n `13`; crypto_alt avg `-0.3912` n `237`; crypto_major avg `-0.2152` n `8`; equity avg `0.4893` n `151`; fx avg `0.011` n `6`; index avg `0.0092` n `26`; metal avg `-0.0055` n `20`; unknown avg `0.5614` n `1171`
- 24h: commodity avg `-0.2179` n `13`; crypto_alt avg `-0.2025` n `237`; crypto_major avg `0.7475` n `8`; equity avg `2.942` n `151`; fx avg `-0.053` n `6`; index avg `0.4704` n `26`; metal avg `0.1912` n `20`; unknown avg `1.1279` n `971`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1992`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1511`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1321`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1122`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0587`, n `666`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
