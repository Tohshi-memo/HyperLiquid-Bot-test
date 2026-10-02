# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T02:37:28.812485+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `13`; crypto_alt avg `0.0204` n `234`; crypto_major avg `0.0284` n `8`; equity avg `0.0057` n `142`; fx avg `0.0091` n `6`; index avg `0.0024` n `26`; metal avg `-0.0025` n `20`; unknown avg `1.572` n `985`
- 1h: commodity avg `0.0035` n `13`; crypto_alt avg `0.5385` n `234`; crypto_major avg `0.406` n `8`; equity avg `0.289` n `142`; fx avg `-0.0294` n `6`; index avg `0.0695` n `26`; metal avg `0.0979` n `20`; unknown avg `2.1298` n `983`
- 4h: commodity avg `-0.1458` n `13`; crypto_alt avg `0.7524` n `234`; crypto_major avg `0.3603` n `8`; equity avg `0.1224` n `142`; fx avg `-0.037` n `6`; index avg `0.0486` n `26`; metal avg `-0.128` n `20`; unknown avg `0.2242` n `977`
- 24h: commodity avg `0.0235` n `13`; crypto_alt avg `-0.0776` n `234`; crypto_major avg `0.3472` n `8`; equity avg `0.7242` n `142`; fx avg `-0.2345` n `6`; index avg `0.0914` n `26`; metal avg `-0.1457` n `20`; unknown avg `0.4688` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
