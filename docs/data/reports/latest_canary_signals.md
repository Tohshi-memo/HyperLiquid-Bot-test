# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T20:38:19.385078+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0209` n `13`; crypto_alt avg `0.1494` n `239`; crypto_major avg `0.1642` n `8`; equity avg `0.1112` n `158`; fx avg `0.0028` n `6`; index avg `-0.0089` n `27`; metal avg `-0.0137` n `20`; unknown avg `-0.2283` n `1263`
- 1h: commodity avg `0.0854` n `13`; crypto_alt avg `0.0324` n `239`; crypto_major avg `0.1741` n `8`; equity avg `0.1724` n `158`; fx avg `-0.0015` n `6`; index avg `-0.0085` n `27`; metal avg `-0.0335` n `20`; unknown avg `35.4601` n `1235`
- 4h: commodity avg `0.2286` n `13`; crypto_alt avg `-0.1312` n `239`; crypto_major avg `-0.0976` n `8`; equity avg `0.1403` n `158`; fx avg `0.0284` n `6`; index avg `-0.0276` n `27`; metal avg `-0.1335` n `20`; unknown avg `-0.6595` n `1201`
- 24h: commodity avg `0.3824` n `13`; crypto_alt avg `1.2447` n `239`; crypto_major avg `1.5684` n `8`; equity avg `1.9492` n `158`; fx avg `0.0793` n `6`; index avg `0.1789` n `27`; metal avg `-0.5337` n `20`; unknown avg `370.6787` n `1059`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
