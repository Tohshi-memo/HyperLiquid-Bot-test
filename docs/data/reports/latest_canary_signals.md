# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T01:52:27.376400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0012` n `13`; crypto_alt avg `0.0496` n `239`; crypto_major avg `0.07` n `8`; equity avg `0.2047` n `157`; fx avg `0.0049` n `6`; index avg `0.0237` n `27`; metal avg `0.0315` n `20`; unknown avg `0.4175` n `1264`
- 1h: commodity avg `0.0173` n `13`; crypto_alt avg `-0.0853` n `239`; crypto_major avg `0.0538` n `8`; equity avg `0.5335` n `157`; fx avg `0.0079` n `6`; index avg `0.0783` n `27`; metal avg `-0.0831` n `20`; unknown avg `0.4577` n `1258`
- 4h: commodity avg `0.0955` n `13`; crypto_alt avg `-0.3806` n `239`; crypto_major avg `0.1184` n `8`; equity avg `0.4378` n `157`; fx avg `-0.0432` n `6`; index avg `0.0817` n `27`; metal avg `-0.0251` n `20`; unknown avg `-0.1894` n `1246`
- 24h: commodity avg `-1.222` n `13`; crypto_alt avg `-2.9126` n `238`; crypto_major avg `-1.7845` n `8`; equity avg `-2.8842` n `157`; fx avg `0.1223` n `6`; index avg `-0.1197` n `27`; metal avg `0.1223` n `20`; unknown avg `12.6888` n `1000`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1668`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
