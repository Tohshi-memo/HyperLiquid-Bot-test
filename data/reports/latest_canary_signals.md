# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T17:52:29.562609+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `13`; crypto_alt avg `-0.098` n `235`; crypto_major avg `-0.1794` n `8`; equity avg `-0.0172` n `150`; fx avg `-0.0022` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0043` n `20`; unknown avg `0.5586` n `1134`
- 1h: commodity avg `0.011` n `13`; crypto_alt avg `0.1198` n `235`; crypto_major avg `-0.037` n `8`; equity avg `0.0007` n `150`; fx avg `0.0053` n `6`; index avg `-0.0016` n `26`; metal avg `0.0142` n `20`; unknown avg `0.4597` n `1124`
- 4h: commodity avg `-0.0491` n `13`; crypto_alt avg `1.9861` n `235`; crypto_major avg `1.5658` n `8`; equity avg `0.2779` n `150`; fx avg `0.0128` n `6`; index avg `0.0365` n `26`; metal avg `0.0679` n `20`; unknown avg `22.5071` n `1102`
- 24h: commodity avg `0.2639` n `13`; crypto_alt avg `2.5048` n `235`; crypto_major avg `1.2033` n `8`; equity avg `0.3571` n `150`; fx avg `0.0206` n `6`; index avg `0.0418` n `26`; metal avg `0.0936` n `20`; unknown avg `0.7831` n `917`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
