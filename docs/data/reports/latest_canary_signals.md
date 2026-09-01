# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T23:37:31.410721+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0226` n `12`; crypto_alt avg `0.3564` n `232`; crypto_major avg `0.3292` n `8`; equity avg `0.0458` n `132`; fx avg `-0.0086` n `6`; index avg `-0.0026` n `26`; metal avg `0.0416` n `20`; unknown avg `0.0093` n `792`
- 1h: commodity avg `-0.0353` n `12`; crypto_alt avg `0.382` n `232`; crypto_major avg `0.518` n `8`; equity avg `0.0145` n `132`; fx avg `-0.0118` n `6`; index avg `0.0022` n `26`; metal avg `0.0375` n `20`; unknown avg `-0.0613` n `790`
- 4h: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.1069` n `232`; crypto_major avg `0.1553` n `8`; equity avg `-0.2562` n `132`; fx avg `0.0098` n `6`; index avg `-0.0045` n `26`; metal avg `0.0321` n `20`; unknown avg `-0.3441` n `772`
- 24h: commodity avg `0.8377` n `12`; crypto_alt avg `-0.2162` n `232`; crypto_major avg `-1.4395` n `8`; equity avg `-2.119` n `130`; fx avg `0.0447` n `6`; index avg `-0.3461` n `26`; metal avg `-0.8459` n `20`; unknown avg `-0.309` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0443`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0424`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0392`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0327`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0311`, n `668`, weak_sample_signal
