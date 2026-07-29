# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T07:26:33.207094+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0381` n `12`; crypto_alt avg `-0.0265` n `230`; crypto_major avg `-0.0783` n `8`; equity avg `0.1736` n `102`; fx avg `-0.0055` n `6`; index avg `-0.0131` n `25`; metal avg `0.0057` n `20`; unknown avg `0.1647` n `777`
- 1h: commodity avg `-0.012` n `12`; crypto_alt avg `0.0978` n `230`; crypto_major avg `0.2645` n `8`; equity avg `0.8165` n `102`; fx avg `0.0027` n `6`; index avg `0.2213` n `25`; metal avg `0.0975` n `20`; unknown avg `0.0645` n `777`
- 4h: commodity avg `-0.0779` n `12`; crypto_alt avg `-0.4146` n `230`; crypto_major avg `0.5709` n `8`; equity avg `0.9304` n `102`; fx avg `-0.0672` n `6`; index avg `0.2654` n `25`; metal avg `0.1522` n `20`; unknown avg `0.0604` n `761`
- 24h: commodity avg `0.0107` n `12`; crypto_alt avg `-1.4602` n `230`; crypto_major avg `0.9649` n `8`; equity avg `-1.2705` n `102`; fx avg `-0.1312` n `6`; index avg `-0.2014` n `25`; metal avg `-0.0192` n `20`; unknown avg `-0.1712` n `758`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
