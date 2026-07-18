# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T09:37:27.210232+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `0.0245` n `230`; crypto_major avg `-0.0122` n `8`; equity avg `0.009` n `96`; fx avg `-0.0029` n `6`; index avg `-0.0301` n `25`; metal avg `0.0011` n `20`; unknown avg `0.003` n `769`
- 1h: commodity avg `0.043` n `12`; crypto_alt avg `-0.4044` n `230`; crypto_major avg `-0.294` n `8`; equity avg `-0.085` n `96`; fx avg `0.0067` n `6`; index avg `0.0007` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.0306` n `769`
- 4h: commodity avg `0.0837` n `12`; crypto_alt avg `-0.503` n `230`; crypto_major avg `-0.2533` n `8`; equity avg `-0.1881` n `96`; fx avg `-0.0008` n `6`; index avg `-0.0126` n `25`; metal avg `0.0102` n `20`; unknown avg `-0.0719` n `737`
- 24h: commodity avg `0.6375` n `12`; crypto_alt avg `-0.6634` n `230`; crypto_major avg `0.1027` n `8`; equity avg `1.2202` n `96`; fx avg `-0.0071` n `6`; index avg `0.2336` n `25`; metal avg `0.1766` n `20`; unknown avg `0.2321` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
