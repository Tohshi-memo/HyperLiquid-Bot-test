# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T21:24:21.508772+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0264` n `13`; crypto_alt avg `0.2055` n `239`; crypto_major avg `0.1508` n `8`; equity avg `0.6433` n `158`; fx avg `0.0082` n `6`; index avg `0.0683` n `27`; metal avg `0.0294` n `20`; unknown avg `158.0165` n `1263`
- 1h: commodity avg `0.0565` n `13`; crypto_alt avg `0.5468` n `239`; crypto_major avg `0.5077` n `8`; equity avg `0.9364` n `158`; fx avg `0.0121` n `6`; index avg `0.0856` n `27`; metal avg `0.0387` n `20`; unknown avg `-0.4665` n `1233`
- 4h: commodity avg `0.2262` n `13`; crypto_alt avg `0.1067` n `239`; crypto_major avg `0.0929` n `8`; equity avg `0.7025` n `158`; fx avg `0.0234` n `6`; index avg `0.051` n `27`; metal avg `-0.0593` n `20`; unknown avg `-0.6297` n `1175`
- 24h: commodity avg `0.4583` n `13`; crypto_alt avg `1.4043` n `239`; crypto_major avg `1.7718` n `8`; equity avg `2.5592` n `158`; fx avg `0.0795` n `6`; index avg `0.2461` n `27`; metal avg `-0.4862` n `20`; unknown avg `-0.6514` n `1065`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
