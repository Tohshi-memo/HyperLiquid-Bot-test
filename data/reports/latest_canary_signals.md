# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T00:52:24.441332+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0417` n `12`; crypto_alt avg `0.4838` n `230`; crypto_major avg `0.3941` n `8`; equity avg `0.3158` n `94`; fx avg `-0.0383` n `6`; index avg `0.0642` n `25`; metal avg `0.077` n `20`; unknown avg `0.0132` n `768`
- 1h: commodity avg `0.0389` n `12`; crypto_alt avg `0.194` n `230`; crypto_major avg `0.1823` n `8`; equity avg `-0.2839` n `94`; fx avg `-0.026` n `6`; index avg `-0.0656` n `25`; metal avg `0.0286` n `20`; unknown avg `-0.2326` n `768`
- 4h: commodity avg `0.0264` n `12`; crypto_alt avg `-0.6276` n `230`; crypto_major avg `-0.6688` n `8`; equity avg `-1.0361` n `94`; fx avg `-0.0236` n `6`; index avg `-0.1126` n `25`; metal avg `0.0279` n `20`; unknown avg `-0.3846` n `768`
- 24h: commodity avg `-0.0829` n `12`; crypto_alt avg `-1.5068` n `230`; crypto_major avg `-2.3838` n `8`; equity avg `-4.2828` n `94`; fx avg `-0.1755` n `6`; index avg `-0.5191` n `25`; metal avg `-0.7979` n `20`; unknown avg `-0.6487` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
