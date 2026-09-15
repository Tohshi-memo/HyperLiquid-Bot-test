# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T14:52:30.300418+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.4518` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.1138` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.0335` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.3557` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0494` n `12`; crypto_alt avg `-1.0942` n `233`; crypto_major avg `-1.0655` n `8`; equity avg `-0.4895` n `137`; fx avg `0.0047` n `6`; index avg `-0.0598` n `27`; metal avg `-0.0525` n `20`; unknown avg `-0.1406` n `897`
- 1h: commodity avg `0.1171` n `12`; crypto_alt avg `-1.322` n `233`; crypto_major avg `-1.5001` n `8`; equity avg `-1.0211` n `137`; fx avg `0.0232` n `6`; index avg `-0.1444` n `27`; metal avg `-0.232` n `20`; unknown avg `0.9498` n `895`
- 4h: commodity avg `0.2747` n `12`; crypto_alt avg `-1.8227` n `233`; crypto_major avg `-2.1771` n `8`; equity avg `-1.0819` n `137`; fx avg `0.044` n `6`; index avg `-0.1436` n `27`; metal avg `-0.0633` n `20`; unknown avg `2.0892` n `873`
- 24h: commodity avg `0.0876` n `12`; crypto_alt avg `-2.6368` n `233`; crypto_major avg `-2.6717` n `8`; equity avg `-0.574` n `137`; fx avg `0.2177` n `6`; index avg `0.002` n `27`; metal avg `0.0496` n `20`; unknown avg `-0.2284` n `813`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
