# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T22:07:26.356665+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0158` n `12`; crypto_alt avg `0.2738` n `231`; crypto_major avg `0.2008` n `8`; equity avg `-0.073` n `124`; fx avg `-0.0093` n `6`; index avg `0.023` n `25`; metal avg `0.0608` n `20`; unknown avg `-0.0422` n `795`
- 1h: commodity avg `-0.0422` n `12`; crypto_alt avg `1.0266` n `231`; crypto_major avg `0.9163` n `8`; equity avg `0.4655` n `124`; fx avg `0.0012` n `6`; index avg `0.1263` n `25`; metal avg `0.0855` n `20`; unknown avg `0.5249` n `795`
- 4h: commodity avg `-0.0792` n `12`; crypto_alt avg `1.512` n `231`; crypto_major avg `1.1097` n `8`; equity avg `1.6387` n `124`; fx avg `-0.0225` n `6`; index avg `0.283` n `25`; metal avg `0.0395` n `20`; unknown avg `0.3251` n `795`
- 24h: commodity avg `0.2881` n `12`; crypto_alt avg `0.7918` n `231`; crypto_major avg `0.4474` n `8`; equity avg `1.304` n `124`; fx avg `-0.0489` n `6`; index avg `0.2624` n `25`; metal avg `-0.3245` n `20`; unknown avg `0.9575` n `777`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
