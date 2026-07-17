# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T05:52:25.601272+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1106` n `12`; crypto_alt avg `-0.3961` n `230`; crypto_major avg `-0.3373` n `8`; equity avg `-0.0846` n `96`; fx avg `-0.0129` n `6`; index avg `0.0147` n `25`; metal avg `0.0793` n `20`; unknown avg `9.579` n `768`
- 1h: commodity avg `-0.155` n `12`; crypto_alt avg `-0.935` n `230`; crypto_major avg `-1.0287` n `8`; equity avg `-0.7584` n `96`; fx avg `-0.0191` n `6`; index avg `-0.0416` n `25`; metal avg `0.0362` n `20`; unknown avg `0.0459` n `768`
- 4h: commodity avg `-0.2265` n `12`; crypto_alt avg `-0.6003` n `230`; crypto_major avg `-0.8557` n `8`; equity avg `-1.26` n `94`; fx avg `-0.016` n `6`; index avg `-0.1871` n `25`; metal avg `-0.0236` n `20`; unknown avg `0.6032` n `768`
- 24h: commodity avg `-0.1894` n `12`; crypto_alt avg `-2.727` n `230`; crypto_major avg `-4.1901` n `8`; equity avg `-6.0942` n `94`; fx avg `-0.1578` n `6`; index avg `-0.7943` n `25`; metal avg `-0.7956` n `20`; unknown avg `-0.5972` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
