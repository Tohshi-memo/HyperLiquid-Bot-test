# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T06:07:25.883893+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `13`; crypto_alt avg `-0.0152` n `235`; crypto_major avg `-0.0254` n `8`; equity avg `-0.0057` n `143`; fx avg `-0.0003` n `6`; index avg `-0.0027` n `26`; metal avg `0.001` n `20`; unknown avg `0.1534` n `1049`
- 1h: commodity avg `0.0128` n `13`; crypto_alt avg `0.0942` n `235`; crypto_major avg `0.054` n `8`; equity avg `-0.0123` n `143`; fx avg `-0.0217` n `6`; index avg `0.0001` n `26`; metal avg `0.0044` n `20`; unknown avg `0.2347` n `1049`
- 4h: commodity avg `-0.0399` n `13`; crypto_alt avg `0.647` n `235`; crypto_major avg `0.1776` n `8`; equity avg `0.0656` n `143`; fx avg `-0.0199` n `6`; index avg `0.0008` n `26`; metal avg `0.0129` n `20`; unknown avg `0.1367` n `1043`
- 24h: commodity avg `0.2129` n `13`; crypto_alt avg `1.8886` n `235`; crypto_major avg `0.8382` n `8`; equity avg `0.2768` n `143`; fx avg `-0.0433` n `6`; index avg `0.0166` n `26`; metal avg `0.0024` n `20`; unknown avg `0.2641` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1875`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
