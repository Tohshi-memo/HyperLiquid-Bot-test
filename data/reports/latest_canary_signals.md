# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T13:37:26.724397+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1076` n `12`; crypto_alt avg `-0.0773` n `232`; crypto_major avg `-0.1232` n `8`; equity avg `0.2924` n `128`; fx avg `-0.005` n `6`; index avg `0.0021` n `26`; metal avg `-0.0328` n `20`; unknown avg `0.0698` n `794`
- 1h: commodity avg `0.1298` n `12`; crypto_alt avg `-0.2845` n `232`; crypto_major avg `-0.2722` n `8`; equity avg `0.1267` n `128`; fx avg `0.0071` n `6`; index avg `-0.0252` n `26`; metal avg `-0.1202` n `20`; unknown avg `-0.0828` n `792`
- 4h: commodity avg `0.1011` n `12`; crypto_alt avg `-0.5199` n `232`; crypto_major avg `-0.3667` n `8`; equity avg `-0.1065` n `128`; fx avg `0.0217` n `6`; index avg `-0.0704` n `26`; metal avg `-0.1107` n `20`; unknown avg `0.272` n `792`
- 24h: commodity avg `0.6483` n `12`; crypto_alt avg `-1.5623` n `231`; crypto_major avg `-2.055` n `8`; equity avg `-0.4197` n `128`; fx avg `-0.1047` n `6`; index avg `-0.1468` n `26`; metal avg `-0.3502` n `20`; unknown avg `-0.2233` n `761`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
