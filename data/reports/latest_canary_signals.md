# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T01:22:49.339298+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0105` n `13`; crypto_alt avg `-0.0498` n `239`; crypto_major avg `-0.0581` n `8`; equity avg `0.0352` n `162`; fx avg `0.0078` n `6`; index avg `-0.0175` n `27`; metal avg `-0.0005` n `20`; unknown avg `2.1524` n `1260`
- 1h: commodity avg `0.0354` n `13`; crypto_alt avg `-0.1135` n `239`; crypto_major avg `-0.3274` n `8`; equity avg `-0.0808` n `162`; fx avg `-0.0071` n `6`; index avg `-0.0047` n `27`; metal avg `-0.0045` n `20`; unknown avg `2.0823` n `1260`
- 4h: commodity avg `0.0056` n `13`; crypto_alt avg `-0.3765` n `239`; crypto_major avg `-0.5018` n `8`; equity avg `-0.408` n `162`; fx avg `-0.0306` n `6`; index avg `-0.0076` n `27`; metal avg `-0.0261` n `20`; unknown avg `2.7496` n `1200`
- 24h: commodity avg `-0.194` n `13`; crypto_alt avg `-1.5576` n `239`; crypto_major avg `-2.9427` n `8`; equity avg `-4.1967` n `162`; fx avg `-0.0636` n `6`; index avg `-0.3918` n `27`; metal avg `-0.5705` n `20`; unknown avg `62.444` n `1036`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
