# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T01:07:29.290661+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0703` n `13`; crypto_alt avg `0.0273` n `239`; crypto_major avg `0.1136` n `8`; equity avg `0.422` n `157`; fx avg `0.0033` n `6`; index avg `0.0749` n `27`; metal avg `-0.0798` n `20`; unknown avg `1.1173` n `1258`
- 1h: commodity avg `0.1471` n `13`; crypto_alt avg `0.0024` n `239`; crypto_major avg `0.3747` n `8`; equity avg `0.313` n `157`; fx avg `-0.0169` n `6`; index avg `0.0616` n `27`; metal avg `-0.0411` n `20`; unknown avg `1.3906` n `1258`
- 4h: commodity avg `0.1638` n `13`; crypto_alt avg `0.2099` n `239`; crypto_major avg `0.5035` n `8`; equity avg `0.546` n `157`; fx avg `-0.0498` n `6`; index avg `0.0847` n `27`; metal avg `0.0065` n `20`; unknown avg `214.2953` n `1168`
- 24h: commodity avg `-1.2283` n `13`; crypto_alt avg `-2.7127` n `238`; crypto_major avg `-1.4073` n `8`; equity avg `-3.1001` n `157`; fx avg `0.1115` n `6`; index avg `-0.1231` n `27`; metal avg `0.021` n `20`; unknown avg `13.2285` n `1000`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
