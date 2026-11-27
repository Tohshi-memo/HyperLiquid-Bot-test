# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T15:37:28.884498+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.8436` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.025` n `13`; crypto_alt avg `0.6984` n `239`; crypto_major avg `0.8264` n `8`; equity avg `0.7256` n `168`; fx avg `0.0038` n `6`; index avg `0.0709` n `27`; metal avg `0.0435` n `20`; unknown avg `0.7518` n `1264`
- 1h: commodity avg `0.0497` n `13`; crypto_alt avg `-0.6134` n `239`; crypto_major avg `-0.493` n `8`; equity avg `0.8853` n `168`; fx avg `-0.0196` n `6`; index avg `0.0988` n `27`; metal avg `-0.0456` n `20`; unknown avg `1.6103` n `1262`
- 4h: commodity avg `-0.2734` n `13`; crypto_alt avg `-1.3996` n `239`; crypto_major avg `-1.8931` n `8`; equity avg `-0.8855` n `168`; fx avg `-0.02` n `6`; index avg `-0.0495` n `27`; metal avg `-0.483` n `20`; unknown avg `1.6722` n `1251`
- 24h: commodity avg `-0.3033` n `13`; crypto_alt avg `0.9848` n `239`; crypto_major avg `1.5153` n `8`; equity avg `2.7776` n `168`; fx avg `-0.118` n `6`; index avg `0.2488` n `27`; metal avg `0.6827` n `20`; unknown avg `89.3046` n `1025`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
