# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T18:07:28.322409+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5884` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0287` n `12`; crypto_alt avg `0.1175` n `230`; crypto_major avg `0.0722` n `8`; equity avg `0.0197` n `98`; fx avg `0.0014` n `6`; index avg `0.0088` n `25`; metal avg `0.0335` n `20`; unknown avg `-0.0504` n `770`
- 1h: commodity avg `0.0059` n `12`; crypto_alt avg `0.0824` n `230`; crypto_major avg `0.0628` n `8`; equity avg `0.2232` n `98`; fx avg `0.007` n `6`; index avg `0.0173` n `25`; metal avg `-0.0125` n `20`; unknown avg `-0.0992` n `770`
- 4h: commodity avg `-0.0003` n `12`; crypto_alt avg `1.2748` n `230`; crypto_major avg `1.6523` n `8`; equity avg `0.2458` n `98`; fx avg `-0.0674` n `6`; index avg `-0.0555` n `25`; metal avg `0.0639` n `20`; unknown avg `0.249` n `770`
- 24h: commodity avg `-0.4804` n `12`; crypto_alt avg `2.1067` n `230`; crypto_major avg `1.8169` n `8`; equity avg `0.7813` n `98`; fx avg `-0.1485` n `6`; index avg `0.2018` n `25`; metal avg `0.1903` n `20`; unknown avg `0.4832` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0994`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0979`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0962`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0859`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0842`, n `666`, weak_sample_signal
