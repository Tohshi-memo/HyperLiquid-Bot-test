# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T08:22:31.836005+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `12`; crypto_alt avg `0.0672` n `230`; crypto_major avg `0.0783` n `8`; equity avg `0.0311` n `92`; fx avg `0.0022` n `6`; index avg `-0.0003` n `25`; metal avg `-0.0015` n `20`; unknown avg `0.0029` n `765`
- 1h: commodity avg `0.013` n `12`; crypto_alt avg `0.0532` n `230`; crypto_major avg `0.0349` n `8`; equity avg `-0.0157` n `92`; fx avg `0.0047` n `6`; index avg `-0.0036` n `25`; metal avg `-0.0022` n `20`; unknown avg `0.0595` n `765`
- 4h: commodity avg `0.0084` n `12`; crypto_alt avg `-0.161` n `229`; crypto_major avg `0.0224` n `8`; equity avg `0.1241` n `92`; fx avg `0.0208` n `6`; index avg `0.0121` n `25`; metal avg `-0.0082` n `20`; unknown avg `-0.0192` n `733`
- 24h: commodity avg `-0.1005` n `12`; crypto_alt avg `0.1201` n `229`; crypto_major avg `-0.5381` n `8`; equity avg `0.2917` n `92`; fx avg `-0.0855` n `6`; index avg `0.1893` n `25`; metal avg `0.0968` n `20`; unknown avg `2.8863` n `730`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
