# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T03:07:26.681577+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `12`; crypto_alt avg `0.0171` n `230`; crypto_major avg `0.0714` n `8`; equity avg `0.0268` n `112`; fx avg `0.0043` n `6`; index avg `0.0001` n `25`; metal avg `-0.0013` n `20`; unknown avg `0.029` n `783`
- 1h: commodity avg `0.0185` n `12`; crypto_alt avg `0.0226` n `230`; crypto_major avg `0.0298` n `8`; equity avg `-0.1211` n `112`; fx avg `-0.0012` n `6`; index avg `-0.0014` n `25`; metal avg `-0.0113` n `20`; unknown avg `0.1171` n `783`
- 4h: commodity avg `0.0269` n `12`; crypto_alt avg `0.2128` n `230`; crypto_major avg `0.2138` n `8`; equity avg `0.1375` n `112`; fx avg `-0.0035` n `6`; index avg `0.0054` n `25`; metal avg `-0.0199` n `20`; unknown avg `-0.2086` n `783`
- 24h: commodity avg `-0.1258` n `12`; crypto_alt avg `-0.4013` n `230`; crypto_major avg `0.1315` n `8`; equity avg `1.558` n `112`; fx avg `-0.084` n `6`; index avg `0.1884` n `25`; metal avg `0.3313` n `20`; unknown avg `-0.0591` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
