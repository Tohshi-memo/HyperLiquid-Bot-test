# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T20:22:37.140833+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0164` n `12`; crypto_alt avg `-0.0419` n `229`; crypto_major avg `0.0093` n `8`; equity avg `-0.0528` n `91`; fx avg `0.0119` n `6`; index avg `-0.0135` n `25`; metal avg `-0.0801` n `20`; unknown avg `-0.0304` n `763`
- 1h: commodity avg `-0.0282` n `12`; crypto_alt avg `0.2261` n `229`; crypto_major avg `0.2658` n `8`; equity avg `0.3087` n `91`; fx avg `-0.0027` n `6`; index avg `0.0745` n `25`; metal avg `0.1023` n `20`; unknown avg `0.0497` n `763`
- 4h: commodity avg `0.3306` n `12`; crypto_alt avg `-1.2732` n `229`; crypto_major avg `-0.9373` n `8`; equity avg `-0.624` n `91`; fx avg `0.0034` n `6`; index avg `-0.0644` n `25`; metal avg `-0.4109` n `20`; unknown avg `0.0891` n `761`
- 24h: commodity avg `0.8501` n `12`; crypto_alt avg `-1.8145` n `229`; crypto_major avg `-0.912` n `8`; equity avg `-3.2584` n `91`; fx avg `-0.2427` n `6`; index avg `-0.5974` n `25`; metal avg `-0.5463` n `20`; unknown avg `-0.2047` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
