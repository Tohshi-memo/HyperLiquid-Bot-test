# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T04:52:28.794539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0137` n `12`; crypto_alt avg `0.1217` n `228`; crypto_major avg `0.2414` n `8`; equity avg `0.0435` n `78`; fx avg `-0.0205` n `6`; index avg `-0.0055` n `23`; metal avg `0.0061` n `18`; unknown avg `-0.0903` n `687`
- 1h: commodity avg `-0.052` n `12`; crypto_alt avg `0.3396` n `228`; crypto_major avg `0.4859` n `8`; equity avg `0.1078` n `78`; fx avg `-0.0276` n `6`; index avg `0.0152` n `23`; metal avg `0.045` n `18`; unknown avg `-0.2274` n `687`
- 4h: commodity avg `0.1719` n `12`; crypto_alt avg `-0.1598` n `228`; crypto_major avg `0.4683` n `8`; equity avg `0.2226` n `78`; fx avg `-0.029` n `6`; index avg `0.0316` n `23`; metal avg `-0.0259` n `18`; unknown avg `-0.6099` n `679`
- 24h: commodity avg `0.4023` n `12`; crypto_alt avg `-3.4488` n `228`; crypto_major avg `-3.9666` n `8`; equity avg `1.1576` n `78`; fx avg `-0.1218` n `6`; index avg `0.3067` n `23`; metal avg `-4.1154` n `18`; unknown avg `-0.3745` n `556`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0493`, n `668`, weak_sample_signal
