# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T14:07:40.438848+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1625` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0142` n `12`; crypto_alt avg `-0.0144` n `229`; crypto_major avg `-0.1704` n `8`; equity avg `0.029` n `88`; fx avg `0.0038` n `6`; index avg `-0.0083` n `25`; metal avg `-0.105` n `20`; unknown avg `-0.0578` n `765`
- 1h: commodity avg `0.189` n `12`; crypto_alt avg `0.8504` n `229`; crypto_major avg `0.5419` n `8`; equity avg `0.6673` n `88`; fx avg `0.0043` n `6`; index avg `0.0569` n `25`; metal avg `0.0578` n `20`; unknown avg `-0.0572` n `765`
- 4h: commodity avg `0.0561` n `12`; crypto_alt avg `-0.4277` n `229`; crypto_major avg `-1.0852` n `8`; equity avg `0.3549` n `88`; fx avg `0.0267` n `6`; index avg `0.0773` n `25`; metal avg `-0.0897` n `20`; unknown avg `-0.3292` n `765`
- 24h: commodity avg `-0.0477` n `12`; crypto_alt avg `-0.6722` n `229`; crypto_major avg `-1.0836` n `8`; equity avg `-0.3099` n `88`; fx avg `0.1434` n `6`; index avg `0.0591` n `25`; metal avg `-0.3893` n `20`; unknown avg `0.5679` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
