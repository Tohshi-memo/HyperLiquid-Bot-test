# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T21:07:26.029917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6412` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0817` n `13`; crypto_alt avg `-0.3027` n `235`; crypto_major avg `-0.1234` n `8`; equity avg `0.0298` n `150`; fx avg `0.0121` n `6`; index avg `0.0111` n `26`; metal avg `0.0061` n `20`; unknown avg `-0.0525` n `1067`
- 1h: commodity avg `0.1831` n `13`; crypto_alt avg `0.1034` n `235`; crypto_major avg `0.1075` n `8`; equity avg `0.105` n `150`; fx avg `0.0041` n `6`; index avg `0.0114` n `26`; metal avg `-0.0089` n `20`; unknown avg `-0.2028` n `1021`
- 4h: commodity avg `0.2291` n `13`; crypto_alt avg `2.0913` n `235`; crypto_major avg `1.6492` n `8`; equity avg `0.658` n `150`; fx avg `0.0501` n `6`; index avg `0.1153` n `26`; metal avg `0.008` n `20`; unknown avg `0.4093` n `1007`
- 24h: commodity avg `0.7158` n `13`; crypto_alt avg `-2.8596` n `235`; crypto_major avg `-3.6266` n `8`; equity avg `-2.6988` n `150`; fx avg `0.0575` n `6`; index avg `-0.3441` n `26`; metal avg `-0.0112` n `20`; unknown avg `6.2228` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1806`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
