# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T22:52:25.952616+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0106` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0044` n `12`; crypto_alt avg `-0.0542` n `233`; crypto_major avg `-0.213` n `8`; equity avg `0.0061` n `136`; fx avg `-0.0097` n `6`; index avg `0.0066` n `27`; metal avg `-0.0035` n `20`; unknown avg `1.1262` n `906`
- 1h: commodity avg `-0.0056` n `12`; crypto_alt avg `-0.1995` n `233`; crypto_major avg `-0.3627` n `8`; equity avg `0.0012` n `136`; fx avg `-0.0249` n `6`; index avg `-0.0096` n `27`; metal avg `-0.0019` n `20`; unknown avg `1.4411` n `894`
- 4h: commodity avg `0.2106` n `12`; crypto_alt avg `-0.8963` n `233`; crypto_major avg `-1.0997` n `8`; equity avg `-0.4241` n `136`; fx avg `0.0025` n `6`; index avg `-0.0891` n `27`; metal avg `-0.0939` n `20`; unknown avg `1.6786` n `866`
- 24h: commodity avg `-0.0819` n `12`; crypto_alt avg `1.5605` n `233`; crypto_major avg `2.6105` n `8`; equity avg `-0.2806` n `136`; fx avg `-0.0027` n `6`; index avg `-0.1446` n `27`; metal avg `-0.3207` n `20`; unknown avg `2.0254` n `676`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
