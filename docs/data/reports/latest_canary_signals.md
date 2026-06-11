# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T12:37:41.306309+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0598` n `12`; crypto_alt avg `0.0432` n `228`; crypto_major avg `-0.09` n `8`; equity avg `-0.3337` n `74`; fx avg `-0.0092` n `6`; index avg `-0.2007` n `23`; metal avg `-0.0183` n `18`; unknown avg `0.162` n `556`
- 1h: commodity avg `0.868` n `12`; crypto_alt avg `-0.5572` n `228`; crypto_major avg `-0.6721` n `8`; equity avg `-0.824` n `74`; fx avg `-0.0244` n `6`; index avg `-0.3121` n `23`; metal avg `-0.4532` n `18`; unknown avg `0.1171` n `556`
- 4h: commodity avg `0.7164` n `12`; crypto_alt avg `-0.8473` n `228`; crypto_major avg `-0.6416` n `8`; equity avg `-0.8724` n `74`; fx avg `-0.0468` n `6`; index avg `-0.3439` n `23`; metal avg `-0.9497` n `18`; unknown avg `1.0078` n `556`
- 24h: commodity avg `0.1025` n `12`; crypto_alt avg `0.274` n `228`; crypto_major avg `0.371` n `8`; equity avg `-0.6542` n `74`; fx avg `0.0173` n `6`; index avg `-0.5738` n `23`; metal avg `-1.3084` n `18`; unknown avg `4.922` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
