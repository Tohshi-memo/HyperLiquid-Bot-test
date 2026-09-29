# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T16:37:33.673286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.7028` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.6352` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6351` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0438` n `12`; crypto_alt avg `-0.1408` n `234`; crypto_major avg `-0.064` n `8`; equity avg `-0.0025` n `142`; fx avg `0.003` n `6`; index avg `0.0029` n `26`; metal avg `0.0376` n `20`; unknown avg `1.288` n `962`
- 1h: commodity avg `-0.1632` n `12`; crypto_alt avg `-0.0702` n `234`; crypto_major avg `0.066` n `8`; equity avg `-0.0314` n `142`; fx avg `-0.034` n `6`; index avg `-0.0018` n `26`; metal avg `0.0111` n `20`; unknown avg `3.2871` n `954`
- 4h: commodity avg `-0.1939` n `12`; crypto_alt avg `-1.2241` n `234`; crypto_major avg `-1.7068` n `8`; equity avg `-0.004` n `142`; fx avg `-0.0303` n `6`; index avg `-0.0716` n `26`; metal avg `-0.0717` n `20`; unknown avg `4.5953` n `892`
- 24h: commodity avg `-0.5429` n `12`; crypto_alt avg `0.4494` n `234`; crypto_major avg `-0.8473` n `8`; equity avg `0.2665` n `142`; fx avg `-0.1583` n `6`; index avg `-0.0619` n `26`; metal avg `-0.1817` n `20`; unknown avg `3.63` n `785`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1902`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1892`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1829`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
