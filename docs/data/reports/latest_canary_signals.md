# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T05:22:25.520814+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.1966` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `4.1012` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `3.4228` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0097` n `13`; crypto_alt avg `0.2807` n `239`; crypto_major avg `0.3149` n `8`; equity avg `0.0381` n `162`; fx avg `0.0057` n `6`; index avg `0.0001` n `27`; metal avg `0.0109` n `20`; unknown avg `0.131` n `1261`
- 1h: commodity avg `-0.0185` n `13`; crypto_alt avg `0.1766` n `239`; crypto_major avg `-0.0693` n `8`; equity avg `-0.0336` n `162`; fx avg `0.0021` n `6`; index avg `-0.0077` n `27`; metal avg `-0.0665` n `20`; unknown avg `108.515` n `1255`
- 4h: commodity avg `0.0364` n `13`; crypto_alt avg `3.1119` n `239`; crypto_major avg `4.233` n `8`; equity avg `0.8102` n `162`; fx avg `0.0129` n `6`; index avg `0.0315` n `27`; metal avg `0.1318` n `20`; unknown avg `98.0042` n `1242`
- 24h: commodity avg `0.0753` n `13`; crypto_alt avg `-5.2972` n `239`; crypto_major avg `-3.9519` n `8`; equity avg `-0.7627` n `162`; fx avg `0.0477` n `6`; index avg `-0.0778` n `27`; metal avg `-0.4474` n `20`; unknown avg `47.1083` n `1060`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
