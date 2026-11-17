# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T17:37:31.185440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5208` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3101` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0128` n `13`; crypto_alt avg `-0.2055` n `239`; crypto_major avg `-0.1996` n `8`; equity avg `-0.1403` n `163`; fx avg `0.0025` n `6`; index avg `-0.0257` n `27`; metal avg `-0.0218` n `20`; unknown avg `0.3858` n `1265`
- 1h: commodity avg `-0.013` n `13`; crypto_alt avg `-0.0608` n `239`; crypto_major avg `0.2559` n `8`; equity avg `0.6367` n `163`; fx avg `0.0245` n `6`; index avg `0.068` n `27`; metal avg `0.0444` n `20`; unknown avg `1.1128` n `1261`
- 4h: commodity avg `-0.0161` n `13`; crypto_alt avg `-1.4405` n `239`; crypto_major avg `-1.4464` n `8`; equity avg `-1.6104` n `163`; fx avg `0.0794` n `6`; index avg `-0.1363` n `27`; metal avg `0.0744` n `20`; unknown avg `8.5011` n `1245`
- 24h: commodity avg `0.0051` n `13`; crypto_alt avg `-0.5067` n `239`; crypto_major avg `-0.413` n `8`; equity avg `-2.0483` n `163`; fx avg `0.0184` n `6`; index avg `-0.242` n `27`; metal avg `-0.0553` n `20`; unknown avg `8.3662` n `1096`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
