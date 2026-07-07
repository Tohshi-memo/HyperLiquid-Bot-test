# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T22:07:33.043968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3175` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `-0.1596` n `229`; crypto_major avg `-0.0467` n `8`; equity avg `-0.0481` n `91`; fx avg `-0.0009` n `6`; index avg `-0.0029` n `25`; metal avg `-0.1056` n `20`; unknown avg `-0.0001` n `763`
- 1h: commodity avg `-0.006` n `12`; crypto_alt avg `-0.8446` n `229`; crypto_major avg `-0.7181` n `8`; equity avg `-0.4212` n `91`; fx avg `-0.0246` n `6`; index avg `-0.0262` n `25`; metal avg `-0.0774` n `20`; unknown avg `0.1879` n `763`
- 4h: commodity avg `0.4386` n `12`; crypto_alt avg `-1.7407` n `229`; crypto_major avg `-1.4683` n `8`; equity avg `-1.0258` n `91`; fx avg `-0.0189` n `6`; index avg `-0.1508` n `25`; metal avg `-0.4741` n `20`; unknown avg `0.8154` n `761`
- 24h: commodity avg `0.9485` n `12`; crypto_alt avg `-3.2378` n `229`; crypto_major avg `-2.2874` n `8`; equity avg `-3.6004` n `91`; fx avg `-0.267` n `6`; index avg `-0.637` n `25`; metal avg `-0.6633` n `20`; unknown avg `-0.3813` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
