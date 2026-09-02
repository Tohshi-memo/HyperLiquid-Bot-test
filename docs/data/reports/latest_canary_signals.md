# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T06:11:19.810591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0401` n `12`; crypto_alt avg `-0.1781` n `232`; crypto_major avg `-0.1198` n `8`; equity avg `-0.0921` n `132`; fx avg `-0.0459` n `6`; index avg `-0.041` n `26`; metal avg `-0.0132` n `20`; unknown avg `0.2971` n `774`
- 1h: commodity avg `0.0126` n `12`; crypto_alt avg `0.2971` n `232`; crypto_major avg `0.3247` n `8`; equity avg `0.1886` n `132`; fx avg `-0.0709` n `6`; index avg `0.0071` n `26`; metal avg `0.1373` n `20`; unknown avg `0.3302` n `774`
- 4h: commodity avg `-0.0441` n `12`; crypto_alt avg `1.3102` n `232`; crypto_major avg `0.93` n `8`; equity avg `0.2117` n `132`; fx avg `-0.1364` n `6`; index avg `-0.029` n `26`; metal avg `0.2123` n `20`; unknown avg `0.0847` n `774`
- 24h: commodity avg `0.8237` n `12`; crypto_alt avg `-0.7273` n `232`; crypto_major avg `-1.8397` n `8`; equity avg `-2.7008` n `130`; fx avg `-0.1862` n `6`; index avg `-0.5217` n `26`; metal avg `-0.9748` n `20`; unknown avg `-0.3506` n `754`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0525`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0458`, n `668`, weak_sample_signal
