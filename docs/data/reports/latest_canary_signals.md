# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T00:07:30.654483+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0982` n `12`; crypto_alt avg `0.0064` n `232`; crypto_major avg `0.0245` n `8`; equity avg `0.0157` n `132`; fx avg `-0.0239` n `6`; index avg `0.0081` n `26`; metal avg `-0.0596` n `20`; unknown avg `0.094` n `790`
- 1h: commodity avg `0.0853` n `12`; crypto_alt avg `0.2832` n `232`; crypto_major avg `0.2676` n `8`; equity avg `0.0384` n `132`; fx avg `-0.0485` n `6`; index avg `0.0191` n `26`; metal avg `-0.0393` n `20`; unknown avg `-0.1027` n `790`
- 4h: commodity avg `0.1054` n `12`; crypto_alt avg `0.1064` n `232`; crypto_major avg `0.2385` n `8`; equity avg `-0.0824` n `132`; fx avg `-0.0342` n `6`; index avg `0.0328` n `26`; metal avg `-0.0261` n `20`; unknown avg `-0.0552` n `772`
- 24h: commodity avg `0.892` n `12`; crypto_alt avg `-0.4748` n `232`; crypto_major avg `-1.6755` n `8`; equity avg `-2.0769` n `130`; fx avg `-0.015` n `6`; index avg `-0.3208` n `26`; metal avg `-1.0226` n `20`; unknown avg `-0.3152` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.044`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0424`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0407`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0322`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0297`, n `668`, weak_sample_signal
