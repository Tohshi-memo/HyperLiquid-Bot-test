# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T08:07:26.786850+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0401` n `12`; crypto_alt avg `-0.2241` n `232`; crypto_major avg `-0.2211` n `8`; equity avg `0.0357` n `128`; fx avg `-0.0168` n `6`; index avg `0.0071` n `26`; metal avg `0.0268` n `20`; unknown avg `0.0077` n `791`
- 1h: commodity avg `0.0308` n `12`; crypto_alt avg `-0.0656` n `232`; crypto_major avg `-0.0649` n `8`; equity avg `0.0048` n `128`; fx avg `-0.0113` n `6`; index avg `0.0154` n `26`; metal avg `0.0392` n `20`; unknown avg `0.033` n `791`
- 4h: commodity avg `-0.0208` n `12`; crypto_alt avg `0.5397` n `232`; crypto_major avg `0.6134` n `8`; equity avg `1.0573` n `128`; fx avg `-0.0568` n `6`; index avg `0.2007` n `26`; metal avg `0.2505` n `20`; unknown avg `0.3482` n `773`
- 24h: commodity avg `0.3543` n `12`; crypto_alt avg `0.0471` n `231`; crypto_major avg `-1.4315` n `8`; equity avg `-0.1527` n `128`; fx avg `-0.1202` n `6`; index avg `-0.0253` n `26`; metal avg `-0.1956` n `20`; unknown avg `-0.4107` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
