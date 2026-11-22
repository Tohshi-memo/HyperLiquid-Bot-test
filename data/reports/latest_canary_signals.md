# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T05:22:29.599620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `71.57` - News risk is high; compare crypto drawdown vs metal/index behavior.
- 4h_index_leads_crypto: score `1.7421` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6999` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.011` n `13`; crypto_alt avg `-0.1853` n `239`; crypto_major avg `-0.294` n `8`; equity avg `-0.0535` n `166`; fx avg `-0.0009` n `6`; index avg `-0.0066` n `27`; metal avg `-0.0016` n `20`; unknown avg `-0.1124` n `1261`
- 1h: commodity avg `0.0174` n `13`; crypto_alt avg `-0.3174` n `239`; crypto_major avg `-0.5292` n `8`; equity avg `-0.1361` n `166`; fx avg `-0.0087` n `6`; index avg `-0.019` n `27`; metal avg `-0.0199` n `20`; unknown avg `318.1918` n `1257`
- 4h: commodity avg `-0.118` n `13`; crypto_alt avg `-1.113` n `239`; crypto_major avg `-1.8456` n `8`; equity avg `-0.6742` n `166`; fx avg `-0.0067` n `6`; index avg `-0.1035` n `27`; metal avg `-0.1457` n `20`; unknown avg `8.8733` n `1255`
- 24h: commodity avg `-0.0087` n `13`; crypto_alt avg `2.5523` n `239`; crypto_major avg `3.9527` n `8`; equity avg `1.3475` n `166`; fx avg `-0.0235` n `6`; index avg `0.1668` n `27`; metal avg `0.1313` n `20`; unknown avg `790.3747` n `1078`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
