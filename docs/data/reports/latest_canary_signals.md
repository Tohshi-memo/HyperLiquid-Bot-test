# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T01:07:29.808799+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.7178` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.5262` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.5073` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0786` n `12`; crypto_alt avg `-0.7794` n `230`; crypto_major avg `-0.6144` n `8`; equity avg `-0.3146` n `102`; fx avg `0.0147` n `6`; index avg `-0.0258` n `25`; metal avg `-0.0763` n `20`; unknown avg `0.2557` n `774`
- 1h: commodity avg `-0.0439` n `12`; crypto_alt avg `-0.8744` n `230`; crypto_major avg `-0.8251` n `8`; equity avg `-0.8814` n `102`; fx avg `0.0056` n `6`; index avg `-0.1699` n `25`; metal avg `-0.1493` n `20`; unknown avg `0.4522` n `774`
- 4h: commodity avg `-0.0747` n `12`; crypto_alt avg `-2.9673` n `230`; crypto_major avg `-2.7925` n `8`; equity avg `-1.5463` n `102`; fx avg `0.0725` n `6`; index avg `-0.2852` n `25`; metal avg `-0.2663` n `20`; unknown avg `1.9703` n `774`
- 24h: commodity avg `-0.7841` n `12`; crypto_alt avg `-4.4447` n `230`; crypto_major avg `-3.7158` n `8`; equity avg `-2.7328` n `102`; fx avg `-0.0446` n `6`; index avg `-0.6434` n `25`; metal avg `-0.3011` n `20`; unknown avg `1161.7453` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.3436`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.3121`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1931`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
