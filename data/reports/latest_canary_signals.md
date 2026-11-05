# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T13:52:29.180251+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0161` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.088` n `13`; crypto_alt avg `-0.0389` n `239`; crypto_major avg `0.0349` n `8`; equity avg `-0.057` n `158`; fx avg `-0.0128` n `6`; index avg `0.0028` n `27`; metal avg `0.1323` n `20`; unknown avg `-0.1244` n `1256`
- 1h: commodity avg `-0.0893` n `13`; crypto_alt avg `0.2207` n `239`; crypto_major avg `0.0701` n `8`; equity avg `-0.0535` n `158`; fx avg `-0.0243` n `6`; index avg `0.0171` n `27`; metal avg `0.1781` n `20`; unknown avg `-0.213` n `1253`
- 4h: commodity avg `0.1886` n `13`; crypto_alt avg `-1.2275` n `239`; crypto_major avg `-1.0918` n `8`; equity avg `-1.3138` n `158`; fx avg `0.03` n `6`; index avg `-0.0757` n `27`; metal avg `0.2574` n `20`; unknown avg `15.764` n `1225`
- 24h: commodity avg `-0.9304` n `13`; crypto_alt avg `0.2458` n `239`; crypto_major avg `1.1545` n `8`; equity avg `-2.6472` n `158`; fx avg `-0.0464` n `6`; index avg `-0.268` n `27`; metal avg `0.8822` n `20`; unknown avg `18.1391` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2346`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2039`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1954`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
