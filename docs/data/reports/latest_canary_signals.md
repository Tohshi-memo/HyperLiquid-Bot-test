# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T19:37:29.214668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6573` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4942` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0237` n `13`; crypto_alt avg `-0.2517` n `239`; crypto_major avg `-0.2369` n `8`; equity avg `-0.2287` n `157`; fx avg `-0.0004` n `6`; index avg `-0.0454` n `27`; metal avg `-0.0482` n `20`; unknown avg `24.6652` n `1264`
- 1h: commodity avg `0.0836` n `13`; crypto_alt avg `-0.6154` n `239`; crypto_major avg `-0.4373` n `8`; equity avg `-1.2625` n `157`; fx avg `0.013` n `6`; index avg `-0.1625` n `27`; metal avg `-0.1322` n `20`; unknown avg `2.8441` n `1214`
- 4h: commodity avg `-0.4065` n `13`; crypto_alt avg `-2.1472` n `239`; crypto_major avg `-1.8192` n `8`; equity avg `-3.2609` n `157`; fx avg `0.005` n `6`; index avg `-0.325` n `27`; metal avg `-0.1619` n `20`; unknown avg `10.2808` n `1184`
- 24h: commodity avg `-1.3234` n `13`; crypto_alt avg `-2.9374` n `238`; crypto_major avg `-1.7174` n `8`; equity avg `-2.778` n `157`; fx avg `0.2567` n `6`; index avg `0.0181` n `27`; metal avg `0.194` n `20`; unknown avg `3.914` n `1012`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
