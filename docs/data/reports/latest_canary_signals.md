# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T02:22:25.401837+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0141` n `13`; crypto_alt avg `0.2767` n `235`; crypto_major avg `0.2384` n `8`; equity avg `-0.0848` n `151`; fx avg `-0.0191` n `6`; index avg `0.0007` n `26`; metal avg `0.0417` n `20`; unknown avg `0.0746` n `1133`
- 1h: commodity avg `-0.0074` n `13`; crypto_alt avg `0.176` n `235`; crypto_major avg `0.1152` n `8`; equity avg `-0.1457` n `151`; fx avg `0.0138` n `6`; index avg `0.0378` n `26`; metal avg `0.03` n `20`; unknown avg `0.432` n `1131`
- 4h: commodity avg `-0.5595` n `13`; crypto_alt avg `0.2979` n `235`; crypto_major avg `0.4331` n `8`; equity avg `-0.0897` n `151`; fx avg `-0.0395` n `6`; index avg `-0.0123` n `26`; metal avg `0.2258` n `20`; unknown avg `1.3162` n `1109`
- 24h: commodity avg `-0.3948` n `13`; crypto_alt avg `1.692` n `235`; crypto_major avg `1.0264` n `8`; equity avg `0.1699` n `151`; fx avg `-0.051` n `6`; index avg `0.0208` n `26`; metal avg `0.2267` n `20`; unknown avg `0.8654` n `948`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
