# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T06:52:18.658917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.4` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0845` n `12`; crypto_alt avg `0.0555` n `228`; crypto_major avg `-0.1103` n `8`; equity avg `-0.004` n `67`; fx avg `0.0001` n `6`; index avg `0.0429` n `23`; metal avg `-0.0287` n `18`; unknown avg `-0.0796` n `386`
- 1h: commodity avg `0.1898` n `12`; crypto_alt avg `-0.5079` n `228`; crypto_major avg `-0.4406` n `8`; equity avg `-0.0932` n `67`; fx avg `-0.021` n `6`; index avg `-0.0891` n `23`; metal avg `-0.3816` n `18`; unknown avg `-0.5119` n `376`
- 4h: commodity avg `0.3788` n `12`; crypto_alt avg `-0.0596` n `228`; crypto_major avg `-0.4105` n `8`; equity avg `0.2286` n `67`; fx avg `0.0489` n `6`; index avg `0.1426` n `23`; metal avg `0.002` n `18`; unknown avg `-0.3564` n `376`
- 24h: commodity avg `-0.7043` n `12`; crypto_alt avg `1.7991` n `228`; crypto_major avg `0.3668` n `8`; equity avg `1.7011` n `66`; fx avg `0.1076` n `6`; index avg `0.8292` n `23`; metal avg `0.9302` n `18`; unknown avg `2.5227` n `375`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0493`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0465`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0426`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0416`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0409`, n `668`, weak_sample_signal
