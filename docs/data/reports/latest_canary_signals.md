# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T23:22:25.672225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0116` n `12`; crypto_alt avg `0.0648` n `230`; crypto_major avg `0.1615` n `8`; equity avg `0.0028` n `108`; fx avg `0.0058` n `6`; index avg `0.0066` n `25`; metal avg `0.0262` n `20`; unknown avg `0.1336` n `782`
- 1h: commodity avg `-0.0257` n `12`; crypto_alt avg `0.0546` n `230`; crypto_major avg `0.0006` n `8`; equity avg `0.0425` n `108`; fx avg `0.0043` n `6`; index avg `-0.0053` n `25`; metal avg `0.038` n `20`; unknown avg `0.0043` n `782`
- 4h: commodity avg `-0.0556` n `12`; crypto_alt avg `-0.1383` n `230`; crypto_major avg `-0.5371` n `8`; equity avg `-0.9634` n `108`; fx avg `0.0192` n `6`; index avg `-0.096` n `25`; metal avg `-0.0057` n `20`; unknown avg `0.0733` n `782`
- 24h: commodity avg `-0.0133` n `12`; crypto_alt avg `0.3359` n `230`; crypto_major avg `0.3868` n `8`; equity avg `-0.8596` n `108`; fx avg `-0.0467` n `6`; index avg `-0.1311` n `25`; metal avg `0.8816` n `20`; unknown avg `0.9654` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
