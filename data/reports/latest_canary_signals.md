# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T17:22:30.225939+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0992` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.6778` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5485` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `0.065` n `233`; crypto_major avg `0.2122` n `8`; equity avg `-0.0283` n `137`; fx avg `-0.0144` n `6`; index avg `-0.0126` n `27`; metal avg `0.0024` n `20`; unknown avg `-0.0637` n `917`
- 1h: commodity avg `0.1267` n `12`; crypto_alt avg `-0.1442` n `233`; crypto_major avg `-0.2174` n `8`; equity avg `-0.071` n `137`; fx avg `0.0011` n `6`; index avg `-0.0069` n `27`; metal avg `0.0122` n `20`; unknown avg `-0.3561` n `901`
- 4h: commodity avg `0.394` n `12`; crypto_alt avg `-1.2904` n `233`; crypto_major avg `-1.7052` n `8`; equity avg `-0.8078` n `137`; fx avg `0.0335` n `6`; index avg `-0.1567` n `27`; metal avg `-0.0274` n `20`; unknown avg `1.0697` n `873`
- 24h: commodity avg `0.4953` n `12`; crypto_alt avg `-2.7992` n `233`; crypto_major avg `-2.9164` n `8`; equity avg `-1.4351` n `137`; fx avg `0.2108` n `6`; index avg `-0.1813` n `27`; metal avg `-0.0292` n `20`; unknown avg `0.7403` n `831`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
