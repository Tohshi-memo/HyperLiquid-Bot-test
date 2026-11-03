# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T22:36:27.454180+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `13`; crypto_alt avg `-0.0343` n `239`; crypto_major avg `-0.0881` n `8`; equity avg `0.0239` n `158`; fx avg `-0.002` n `6`; index avg `0.0015` n `27`; metal avg `-0.002` n `20`; unknown avg `-0.0985` n `1264`
- 1h: commodity avg `-0.0019` n `13`; crypto_alt avg `-0.232` n `239`; crypto_major avg `-0.35` n `8`; equity avg `-0.156` n `158`; fx avg `-0.0264` n `6`; index avg `-0.011` n `27`; metal avg `0.0031` n `20`; unknown avg `159.5168` n `1256`
- 4h: commodity avg `0.202` n `13`; crypto_alt avg `0.1263` n `239`; crypto_major avg `-0.1593` n `8`; equity avg `0.7894` n `158`; fx avg `-0.016` n `6`; index avg `0.0509` n `27`; metal avg `-0.0181` n `20`; unknown avg `19.113` n `1215`
- 24h: commodity avg `0.3624` n `13`; crypto_alt avg `1.238` n `239`; crypto_major avg `1.4029` n `8`; equity avg `2.8099` n `158`; fx avg `0.0714` n `6`; index avg `0.3038` n `27`; metal avg `-0.487` n `20`; unknown avg `-0.8144` n `1065`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
