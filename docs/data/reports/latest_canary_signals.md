# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T18:37:30.285216+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0153` n `12`; crypto_alt avg `0.0209` n `230`; crypto_major avg `0.0688` n `8`; equity avg `-0.0095` n `92`; fx avg `-0.0023` n `6`; index avg `-0.0067` n `25`; metal avg `0.0023` n `20`; unknown avg `-0.0267` n `765`
- 1h: commodity avg `0.0362` n `12`; crypto_alt avg `0.127` n `230`; crypto_major avg `0.0975` n `8`; equity avg `0.0651` n `92`; fx avg `-0.003` n `6`; index avg `0.0013` n `25`; metal avg `-0.0018` n `20`; unknown avg `-0.0685` n `765`
- 4h: commodity avg `0.0535` n `12`; crypto_alt avg `0.1171` n `230`; crypto_major avg `0.0683` n `8`; equity avg `0.1544` n `92`; fx avg `-0.0016` n `6`; index avg `0.0157` n `25`; metal avg `-0.0228` n `20`; unknown avg `0.229` n `765`
- 24h: commodity avg `0.0117` n `12`; crypto_alt avg `1.2106` n `229`; crypto_major avg `0.9348` n `8`; equity avg `0.2317` n `92`; fx avg `0.0055` n `6`; index avg `0.0305` n `25`; metal avg `0.0714` n `20`; unknown avg `2.4289` n `727`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
