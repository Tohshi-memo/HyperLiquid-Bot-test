# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T20:52:33.013197+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.706` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6726` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0182` n `12`; crypto_alt avg `0.1797` n `233`; crypto_major avg `0.2428` n `8`; equity avg `0.0595` n `137`; fx avg `-0.0097` n `6`; index avg `0.0026` n `27`; metal avg `0.0224` n `20`; unknown avg `12.9773` n `920`
- 1h: commodity avg `-0.0295` n `12`; crypto_alt avg `-0.2525` n `233`; crypto_major avg `-0.2092` n `8`; equity avg `0.1535` n `137`; fx avg `-0.0072` n `6`; index avg `0.0397` n `27`; metal avg `0.0024` n `20`; unknown avg `4.0568` n `894`
- 4h: commodity avg `-0.0164` n `12`; crypto_alt avg `-1.6693` n `233`; crypto_major avg `-1.6528` n `8`; equity avg `-0.3489` n `137`; fx avg `-0.0069` n `6`; index avg `0.0198` n `27`; metal avg `0.0532` n `20`; unknown avg `1.6373` n `893`
- 24h: commodity avg `0.5057` n `12`; crypto_alt avg `-4.7463` n `233`; crypto_major avg `-5.4412` n `8`; equity avg `-1.202` n `137`; fx avg `0.211` n `6`; index avg `-0.0633` n `27`; metal avg `0.1702` n `20`; unknown avg `1.6328` n `843`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
