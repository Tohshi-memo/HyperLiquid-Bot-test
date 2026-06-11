# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T09:22:31.682374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0254` n `12`; crypto_alt avg `-0.204` n `228`; crypto_major avg `-0.1785` n `8`; equity avg `-0.1858` n `74`; fx avg `0.0021` n `6`; index avg `-0.0544` n `23`; metal avg `-0.0238` n `18`; unknown avg `0.0692` n `556`
- 1h: commodity avg `0.0738` n `12`; crypto_alt avg `-0.3504` n `228`; crypto_major avg `-0.2392` n `8`; equity avg `-0.1391` n `74`; fx avg `-0.0092` n `6`; index avg `-0.0104` n `23`; metal avg `-0.3864` n `18`; unknown avg `4.1386` n `556`
- 4h: commodity avg `-0.6951` n `12`; crypto_alt avg `-0.2022` n `228`; crypto_major avg `0.2848` n `8`; equity avg `0.5822` n `74`; fx avg `0.0107` n `6`; index avg `0.3542` n `23`; metal avg `0.0725` n `18`; unknown avg `4.3548` n `530`
- 24h: commodity avg `0.7998` n `12`; crypto_alt avg `1.9303` n `228`; crypto_major avg `2.0086` n `8`; equity avg `1.2445` n `74`; fx avg `0.0183` n `6`; index avg `0.2609` n `23`; metal avg `-0.3087` n `18`; unknown avg `8.1081` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
