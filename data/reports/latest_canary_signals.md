# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T08:22:29.331399+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1586` n `12`; crypto_alt avg `0.0935` n `230`; crypto_major avg `0.1076` n `8`; equity avg `0.1456` n `92`; fx avg `-0.0` n `6`; index avg `0.0218` n `25`; metal avg `-0.02` n `20`; unknown avg `0.0148` n `766`
- 1h: commodity avg `-0.0366` n `12`; crypto_alt avg `-0.1108` n `230`; crypto_major avg `0.0071` n `8`; equity avg `0.0962` n `92`; fx avg `0.0363` n `6`; index avg `0.004` n `25`; metal avg `-0.0657` n `20`; unknown avg `-0.0432` n `766`
- 4h: commodity avg `0.1047` n `12`; crypto_alt avg `0.2161` n `230`; crypto_major avg `0.092` n `8`; equity avg `1.1355` n `92`; fx avg `0.0869` n `6`; index avg `0.2379` n `25`; metal avg `0.0828` n `20`; unknown avg `0.0999` n `750`
- 24h: commodity avg `1.3461` n `12`; crypto_alt avg `-0.775` n `230`; crypto_major avg `-0.8143` n `8`; equity avg `-0.4746` n `92`; fx avg `-0.1076` n `6`; index avg `-0.115` n `25`; metal avg `-0.2348` n `20`; unknown avg `-0.2364` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
