# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T15:52:33.462527+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.0152` n `232`; crypto_major avg `-0.1058` n `8`; equity avg `-0.0668` n `133`; fx avg `0.0123` n `6`; index avg `-0.0141` n `26`; metal avg `-0.0033` n `20`; unknown avg `0.1416` n `792`
- 1h: commodity avg `0.0602` n `12`; crypto_alt avg `-0.0067` n `232`; crypto_major avg `-0.1058` n `8`; equity avg `0.0267` n `133`; fx avg `0.0011` n `6`; index avg `0.0098` n `26`; metal avg `-0.0499` n `20`; unknown avg `0.4234` n `789`
- 4h: commodity avg `0.3843` n `12`; crypto_alt avg `0.3189` n `232`; crypto_major avg `0.5651` n `8`; equity avg `0.7264` n `133`; fx avg `-0.1088` n `6`; index avg `0.1659` n `26`; metal avg `0.3054` n `20`; unknown avg `0.9204` n `789`
- 24h: commodity avg `0.7122` n `12`; crypto_alt avg `-1.4506` n `232`; crypto_major avg `-1.8047` n `8`; equity avg `-0.8336` n `133`; fx avg `-0.3353` n `6`; index avg `-0.1341` n `26`; metal avg `-0.0071` n `20`; unknown avg `-0.0333` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
