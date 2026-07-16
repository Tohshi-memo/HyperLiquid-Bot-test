# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T02:52:23.845254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `12`; crypto_alt avg `0.0032` n `230`; crypto_major avg `0.0032` n `8`; equity avg `0.097` n `94`; fx avg `-0.0034` n `6`; index avg `0.0191` n `25`; metal avg `-0.0304` n `20`; unknown avg `-0.079` n `768`
- 1h: commodity avg `-0.0406` n `12`; crypto_alt avg `0.0176` n `230`; crypto_major avg `-0.0698` n `8`; equity avg `0.1415` n `94`; fx avg `-0.0307` n `6`; index avg `0.0406` n `25`; metal avg `-0.0426` n `20`; unknown avg `-0.1979` n `768`
- 4h: commodity avg `-0.1149` n `12`; crypto_alt avg `-0.0124` n `230`; crypto_major avg `-0.3121` n `8`; equity avg `-0.1429` n `94`; fx avg `-0.0229` n `6`; index avg `-0.0732` n `25`; metal avg `-0.2229` n `20`; unknown avg `-0.3119` n `766`
- 24h: commodity avg `-0.1282` n `12`; crypto_alt avg `0.5937` n `230`; crypto_major avg `0.6222` n `8`; equity avg `-2.0955` n `93`; fx avg `0.136` n `6`; index avg `-0.4047` n `25`; metal avg `-0.0962` n `20`; unknown avg `0.0243` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
