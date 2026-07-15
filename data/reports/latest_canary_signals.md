# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T00:07:24.051196+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0631` n `12`; crypto_alt avg `0.0476` n `230`; crypto_major avg `0.0443` n `8`; equity avg `0.0576` n `92`; fx avg `0.0217` n `6`; index avg `-0.0375` n `25`; metal avg `0.0257` n `20`; unknown avg `-0.2381` n `768`
- 1h: commodity avg `0.031` n `12`; crypto_alt avg `0.15` n `230`; crypto_major avg `0.1838` n `8`; equity avg `0.3353` n `92`; fx avg `0.0293` n `6`; index avg `0.0453` n `25`; metal avg `0.0744` n `20`; unknown avg `-0.2934` n `766`
- 4h: commodity avg `0.0067` n `12`; crypto_alt avg `0.4636` n `230`; crypto_major avg `0.5135` n `8`; equity avg `0.4697` n `92`; fx avg `0.0179` n `6`; index avg `0.0636` n `25`; metal avg `0.0102` n `20`; unknown avg `-0.3629` n `766`
- 24h: commodity avg `0.0124` n `12`; crypto_alt avg `2.3291` n `230`; crypto_major avg `3.706` n `8`; equity avg `2.4861` n `92`; fx avg `0.0065` n `6`; index avg `0.7018` n `25`; metal avg `0.7254` n `20`; unknown avg `0.2407` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
