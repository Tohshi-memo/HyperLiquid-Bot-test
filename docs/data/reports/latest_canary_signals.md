# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T19:37:27.690941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0547` n `12`; crypto_alt avg `0.1393` n `232`; crypto_major avg `-0.0048` n `8`; equity avg `0.0109` n `131`; fx avg `0.0009` n `6`; index avg `0.0022` n `26`; metal avg `-0.0374` n `20`; unknown avg `0.2596` n `793`
- 1h: commodity avg `0.1319` n `12`; crypto_alt avg `0.9602` n `232`; crypto_major avg `0.8599` n `8`; equity avg `0.3152` n `131`; fx avg `-0.01` n `6`; index avg `0.0372` n `26`; metal avg `-0.0222` n `20`; unknown avg `0.822` n `791`
- 4h: commodity avg `0.6222` n `12`; crypto_alt avg `-0.7652` n `232`; crypto_major avg `-1.0155` n `8`; equity avg `-0.5267` n `131`; fx avg `0.0087` n `6`; index avg `-0.1691` n `26`; metal avg `-0.339` n `20`; unknown avg `-1.0428` n `790`
- 24h: commodity avg `0.9464` n `12`; crypto_alt avg `-0.0078` n `232`; crypto_major avg `-1.9572` n `8`; equity avg `-1.571` n `130`; fx avg `0.0348` n `6`; index avg `-0.2863` n `26`; metal avg `-0.88` n `20`; unknown avg `0.5051` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0464`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0435`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0403`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0348`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.033`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0329`, n `668`, weak_sample_signal
