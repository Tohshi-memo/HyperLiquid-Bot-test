# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T03:07:30.394506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0319` n `12`; crypto_alt avg `0.0585` n `234`; crypto_major avg `0.0737` n `8`; equity avg `-0.0154` n `137`; fx avg `-0.0122` n `6`; index avg `-0.0047` n `27`; metal avg `0.0451` n `20`; unknown avg `-0.2096` n `919`
- 1h: commodity avg `0.0288` n `12`; crypto_alt avg `0.2959` n `234`; crypto_major avg `0.3638` n `8`; equity avg `0.1915` n `137`; fx avg `-0.044` n `6`; index avg `0.0254` n `27`; metal avg `0.0453` n `20`; unknown avg `-0.1175` n `917`
- 4h: commodity avg `0.0865` n `12`; crypto_alt avg `1.8431` n `234`; crypto_major avg `1.302` n `8`; equity avg `0.4484` n `137`; fx avg `0.0019` n `6`; index avg `0.086` n `27`; metal avg `0.266` n `20`; unknown avg `1.0185` n `909`
- 24h: commodity avg `-0.3687` n `12`; crypto_alt avg `2.1685` n `234`; crypto_major avg `1.42` n `8`; equity avg `1.2633` n `137`; fx avg `-0.0057` n `6`; index avg `0.1053` n `27`; metal avg `-0.2898` n `20`; unknown avg `1.3052` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
