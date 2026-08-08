# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T04:43:47.561220+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0106` n `12`; crypto_alt avg `0.0951` n `230`; crypto_major avg `0.0861` n `8`; equity avg `-0.0401` n `112`; fx avg `0.0` n `6`; index avg `-0.0096` n `25`; metal avg `-0.008` n `20`; unknown avg `0.3314` n `783`
- 1h: commodity avg `0.02` n `12`; crypto_alt avg `0.0832` n `230`; crypto_major avg `0.0553` n `8`; equity avg `-0.0146` n `112`; fx avg `-0.0033` n `6`; index avg `-0.0189` n `25`; metal avg `0.0021` n `20`; unknown avg `0.2938` n `783`
- 4h: commodity avg `0.0581` n `12`; crypto_alt avg `0.5452` n `230`; crypto_major avg `0.6127` n `8`; equity avg `-0.0676` n `112`; fx avg `0.0009` n `6`; index avg `-0.0099` n `25`; metal avg `-0.0212` n `20`; unknown avg `0.0711` n `783`
- 24h: commodity avg `-0.2247` n `12`; crypto_alt avg `0.3568` n `230`; crypto_major avg `0.7979` n `8`; equity avg `1.6713` n `112`; fx avg `-0.0761` n `6`; index avg `0.1855` n `25`; metal avg `0.3321` n `20`; unknown avg `0.0387` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
