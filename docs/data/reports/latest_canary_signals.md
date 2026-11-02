# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T07:37:29.571401+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3126` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0048` n `13`; crypto_alt avg `-0.1825` n `238`; crypto_major avg `-0.1337` n `8`; equity avg `-0.0552` n `156`; fx avg `0.0042` n `6`; index avg `-0.0069` n `27`; metal avg `-0.0479` n `20`; unknown avg `-0.0038` n `1264`
- 1h: commodity avg `-0.0592` n `13`; crypto_alt avg `-0.1894` n `238`; crypto_major avg `-0.3062` n `8`; equity avg `-0.0901` n `156`; fx avg `0.0265` n `6`; index avg `-0.0218` n `27`; metal avg `0.0006` n `20`; unknown avg `-0.1329` n `1258`
- 4h: commodity avg `-0.0452` n `13`; crypto_alt avg `-1.6513` n `238`; crypto_major avg `-1.3326` n `8`; equity avg `-0.3821` n `156`; fx avg `0.0143` n `6`; index avg `-0.02` n `27`; metal avg `0.0508` n `20`; unknown avg `0.1298` n `1201`
- 24h: commodity avg `-0.4219` n `13`; crypto_alt avg `-2.0384` n `238`; crypto_major avg `-0.4541` n `8`; equity avg `0.96` n `156`; fx avg `0.238` n `6`; index avg `0.2918` n `27`; metal avg `0.1162` n `20`; unknown avg `2.3315` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1956`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1909`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.177`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1692`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
