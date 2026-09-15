# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T20:08:06.019094+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5517` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4595` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0356` n `12`; crypto_alt avg `-0.1456` n `233`; crypto_major avg `-0.1537` n `8`; equity avg `0.1` n `137`; fx avg `-0.0073` n `6`; index avg `0.0339` n `27`; metal avg `0.0062` n `20`; unknown avg `220.8113` n `916`
- 1h: commodity avg `0.0983` n `12`; crypto_alt avg `-0.379` n `233`; crypto_major avg `-0.4391` n `8`; equity avg `-0.0115` n `137`; fx avg `-0.0094` n `6`; index avg `0.0232` n `27`; metal avg `-0.0636` n `20`; unknown avg `5.9551` n `916`
- 4h: commodity avg `0.1303` n `12`; crypto_alt avg `-1.1407` n `233`; crypto_major avg `-1.4119` n `8`; equity avg `-0.2364` n `137`; fx avg `-0.024` n `6`; index avg `0.0476` n `27`; metal avg `0.1398` n `20`; unknown avg `2.3484` n `901`
- 24h: commodity avg `0.5848` n `12`; crypto_alt avg `-4.1375` n `233`; crypto_major avg `-4.9406` n `8`; equity avg `-1.0032` n `137`; fx avg `0.2052` n `6`; index avg `-0.0335` n `27`; metal avg `0.2398` n `20`; unknown avg `0.6826` n `843`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
