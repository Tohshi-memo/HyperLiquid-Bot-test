# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T17:22:29.250596+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2326` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0052` n `13`; crypto_alt avg `0.1247` n `239`; crypto_major avg `0.1234` n `8`; equity avg `0.3129` n `163`; fx avg `0.0052` n `6`; index avg `0.0493` n `27`; metal avg `0.0514` n `20`; unknown avg `158.1199` n `1263`
- 1h: commodity avg `-0.0909` n `13`; crypto_alt avg `-0.3176` n `239`; crypto_major avg `-0.0229` n `8`; equity avg `0.623` n `163`; fx avg `0.0062` n `6`; index avg `0.0781` n `27`; metal avg `0.0782` n `20`; unknown avg `0.0379` n `1259`
- 4h: commodity avg `-0.0382` n `13`; crypto_alt avg `-1.4619` n `239`; crypto_major avg `-1.358` n `8`; equity avg `-1.6011` n `163`; fx avg `0.0638` n `6`; index avg `-0.1254` n `27`; metal avg `0.0356` n `20`; unknown avg `2.3645` n `1245`
- 24h: commodity avg `0.0014` n `13`; crypto_alt avg `-0.5933` n `239`; crypto_major avg `-0.5156` n `8`; equity avg `-1.8935` n `163`; fx avg `0.0041` n `6`; index avg `-0.2288` n `27`; metal avg `-0.0286` n `20`; unknown avg `13.8788` n `1098`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
