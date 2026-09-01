# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T20:37:32.320279+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.037` n `12`; crypto_alt avg `0.0067` n `232`; crypto_major avg `0.1101` n `8`; equity avg `-0.0374` n `131`; fx avg `0.0037` n `6`; index avg `0.0078` n `26`; metal avg `-0.0142` n `20`; unknown avg `0.1309` n `781`
- 1h: commodity avg `0.03` n `12`; crypto_alt avg `-0.0493` n `232`; crypto_major avg `0.1052` n `8`; equity avg `-0.0099` n `131`; fx avg `0.0092` n `6`; index avg `0.0134` n `26`; metal avg `-0.017` n `20`; unknown avg `0.0486` n `779`
- 4h: commodity avg `0.3234` n `12`; crypto_alt avg `0.0169` n `232`; crypto_major avg `-0.1825` n `8`; equity avg `-0.0586` n `131`; fx avg `0.0135` n `6`; index avg `-0.0425` n `26`; metal avg `-0.2646` n `20`; unknown avg `-0.2538` n `779`
- 24h: commodity avg `0.9043` n `12`; crypto_alt avg `-0.067` n `232`; crypto_major avg `-1.6873` n `8`; equity avg `-1.875` n `130`; fx avg `0.0459` n `6`; index avg `-0.3207` n `26`; metal avg `-0.9096` n `20`; unknown avg `-0.3611` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0454`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0444`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0376`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0314`, n `668`, weak_sample_signal
