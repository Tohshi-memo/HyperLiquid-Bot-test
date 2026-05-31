# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T17:07:19.348962+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1332` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0224` n `12`; crypto_alt avg `0.0521` n `228`; crypto_major avg `0.1526` n `8`; equity avg `0.0076` n `69`; fx avg `0.0021` n `6`; index avg `0.0808` n `23`; metal avg `0.0057` n `18`; unknown avg `0.7011` n `421`
- 1h: commodity avg `-0.1047` n `12`; crypto_alt avg `-0.6026` n `228`; crypto_major avg `-0.5238` n `8`; equity avg `-0.1422` n `69`; fx avg `0.006` n `6`; index avg `0.0841` n `23`; metal avg `0.0391` n `18`; unknown avg `0.9673` n `421`
- 4h: commodity avg `0.1007` n `12`; crypto_alt avg `-1.5866` n `228`; crypto_major avg `-0.8753` n `8`; equity avg `-0.0033` n `69`; fx avg `-0.0099` n `6`; index avg `0.2579` n `23`; metal avg `-0.0366` n `18`; unknown avg `0.5141` n `421`
- 24h: commodity avg `0.5264` n `12`; crypto_alt avg `-1.5732` n `228`; crypto_major avg `-0.5259` n `8`; equity avg `0.8784` n `69`; fx avg `0.0143` n `6`; index avg `0.0813` n `23`; metal avg `-0.11` n `18`; unknown avg `0.0648` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2178`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
