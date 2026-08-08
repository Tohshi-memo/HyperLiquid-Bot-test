# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T04:22:22.868493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `-0.044` n `230`; crypto_major avg `-0.0571` n `8`; equity avg `-0.027` n `112`; fx avg `0.0` n `6`; index avg `-0.0186` n `25`; metal avg `-0.0013` n `20`; unknown avg `0.0195` n `783`
- 1h: commodity avg `-0.0146` n `12`; crypto_alt avg `0.1509` n `230`; crypto_major avg `0.1627` n `8`; equity avg `-0.0458` n `112`; fx avg `-0.0021` n `6`; index avg `-0.0111` n `25`; metal avg `0.0151` n `20`; unknown avg `-0.0487` n `783`
- 4h: commodity avg `0.0563` n `12`; crypto_alt avg `0.4264` n `230`; crypto_major avg `0.4986` n `8`; equity avg `-0.0126` n `112`; fx avg `-0.0012` n `6`; index avg `0.0111` n `25`; metal avg `-0.0161` n `20`; unknown avg `-0.1723` n `783`
- 24h: commodity avg `-0.2792` n `12`; crypto_alt avg `0.0797` n `230`; crypto_major avg `0.6565` n `8`; equity avg `1.6827` n `112`; fx avg `-0.0756` n `6`; index avg `0.178` n `25`; metal avg `0.316` n `20`; unknown avg `0.0368` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
