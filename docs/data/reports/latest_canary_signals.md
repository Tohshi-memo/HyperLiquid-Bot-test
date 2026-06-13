# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T06:52:34.022372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0729` n `12`; crypto_alt avg `0.2961` n `228`; crypto_major avg `0.2296` n `8`; equity avg `0.0555` n `74`; fx avg `0.0005` n `6`; index avg `0.0184` n `23`; metal avg `0.006` n `18`; unknown avg `-0.0875` n `643`
- 1h: commodity avg `-0.1183` n `12`; crypto_alt avg `0.9477` n `228`; crypto_major avg `0.7156` n `8`; equity avg `0.131` n `74`; fx avg `-0.0202` n `6`; index avg `-0.0213` n `23`; metal avg `0.0074` n `18`; unknown avg `0.0174` n `627`
- 4h: commodity avg `-0.0986` n `12`; crypto_alt avg `0.4144` n `228`; crypto_major avg `0.105` n `8`; equity avg `-0.3065` n `74`; fx avg `0.0009` n `6`; index avg `-0.0167` n `23`; metal avg `-0.0473` n `18`; unknown avg `-0.3332` n `619`
- 24h: commodity avg `-0.789` n `12`; crypto_alt avg `1.6672` n `228`; crypto_major avg `1.2036` n `8`; equity avg `0.1201` n `74`; fx avg `0.0131` n `6`; index avg `1.0709` n `23`; metal avg `0.7958` n `18`; unknown avg `36.8394` n `507`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
