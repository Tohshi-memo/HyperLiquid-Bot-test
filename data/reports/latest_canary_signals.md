# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T14:37:34.952178+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0366` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.4947` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0071` n `13`; crypto_alt avg `-0.4754` n `239`; crypto_major avg `-0.6272` n `8`; equity avg `-1.158` n `168`; fx avg `-0.0086` n `6`; index avg `-0.104` n `27`; metal avg `-0.1008` n `20`; unknown avg `-0.2921` n `1259`
- 1h: commodity avg `0.1335` n `13`; crypto_alt avg `-0.9367` n `239`; crypto_major avg `-0.9231` n `8`; equity avg `-1.3827` n `168`; fx avg `0.009` n `6`; index avg `-0.1084` n `27`; metal avg `-0.2218` n `20`; unknown avg `-0.3866` n `1249`
- 4h: commodity avg `0.3055` n `13`; crypto_alt avg `-1.9521` n `239`; crypto_major avg `-1.7311` n `8`; equity avg `-2.1786` n `168`; fx avg `0.0235` n `6`; index avg `-0.2364` n `27`; metal avg `-0.4865` n `20`; unknown avg `41.5469` n `1177`
- 24h: commodity avg `0.2167` n `13`; crypto_alt avg `-3.3191` n `239`; crypto_major avg `-4.1677` n `8`; equity avg `-6.2959` n `168`; fx avg `-0.0512` n `6`; index avg `-0.5661` n `27`; metal avg `-1.4539` n `20`; unknown avg `615.6069` n `1065`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
