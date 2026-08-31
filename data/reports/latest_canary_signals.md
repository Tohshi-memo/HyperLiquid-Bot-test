# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T14:37:29.362844+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0278` n `12`; crypto_alt avg `0.1366` n `232`; crypto_major avg `0.2008` n `8`; equity avg `0.0988` n `128`; fx avg `0.0058` n `6`; index avg `0.0152` n `26`; metal avg `0.0493` n `20`; unknown avg `0.5095` n `794`
- 1h: commodity avg `-0.1886` n `12`; crypto_alt avg `0.1673` n `232`; crypto_major avg `0.1603` n `8`; equity avg `-0.0449` n `128`; fx avg `0.0081` n `6`; index avg `-0.027` n `26`; metal avg `-0.0877` n `20`; unknown avg `0.1223` n `790`
- 4h: commodity avg `-0.1789` n `12`; crypto_alt avg `-0.3709` n `232`; crypto_major avg `-0.2603` n `8`; equity avg `-0.0096` n `128`; fx avg `0.0267` n `6`; index avg `-0.056` n `26`; metal avg `-0.2078` n `20`; unknown avg `0.2996` n `790`
- 24h: commodity avg `0.4837` n `12`; crypto_alt avg `-1.3984` n `231`; crypto_major avg `-2.0027` n `8`; equity avg `-0.4868` n `128`; fx avg `-0.1011` n `6`; index avg `-0.1553` n `26`; metal avg `-0.5026` n `20`; unknown avg `0.072` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0531`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0481`, n `668`, weak_sample_signal
