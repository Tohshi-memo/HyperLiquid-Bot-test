# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T23:31:06.192157+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0` n `12`; crypto_alt avg `0.0376` n `230`; crypto_major avg `0.077` n `8`; equity avg `0.0013` n `96`; fx avg `-0.0007` n `6`; index avg `-0.0048` n `25`; metal avg `0.0006` n `20`; unknown avg `-0.0648` n `769`
- 1h: commodity avg `0.0088` n `12`; crypto_alt avg `0.2489` n `230`; crypto_major avg `0.1319` n `8`; equity avg `-0.036` n `96`; fx avg `0.0085` n `6`; index avg `-0.0055` n `25`; metal avg `-0.0042` n `20`; unknown avg `-0.1099` n `769`
- 4h: commodity avg `0.2138` n `12`; crypto_alt avg `-0.0568` n `230`; crypto_major avg `-0.1092` n `8`; equity avg `-0.484` n `96`; fx avg `-0.0618` n `6`; index avg `-0.1061` n `25`; metal avg `0.0213` n `20`; unknown avg `-0.0517` n `769`
- 24h: commodity avg `0.7374` n `12`; crypto_alt avg `-0.3526` n `230`; crypto_major avg `-0.3561` n `8`; equity avg `-0.752` n `94`; fx avg `0.0392` n `6`; index avg `-0.2544` n `25`; metal avg `0.0236` n `20`; unknown avg `0.1018` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
