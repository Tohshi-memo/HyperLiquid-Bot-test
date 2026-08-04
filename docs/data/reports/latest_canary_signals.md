# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T02:52:36.718812+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0185` n `12`; crypto_alt avg `-0.0449` n `230`; crypto_major avg `-0.0917` n `8`; equity avg `-0.0358` n `107`; fx avg `0.0041` n `6`; index avg `-0.0265` n `25`; metal avg `0.0584` n `20`; unknown avg `-0.002` n `780`
- 1h: commodity avg `0.0358` n `12`; crypto_alt avg `0.1036` n `230`; crypto_major avg `0.0112` n `8`; equity avg `-0.3047` n `107`; fx avg `0.0372` n `6`; index avg `-0.0613` n `25`; metal avg `0.055` n `20`; unknown avg `-0.207` n `780`
- 4h: commodity avg `0.2798` n `12`; crypto_alt avg `0.2738` n `230`; crypto_major avg `0.335` n `8`; equity avg `-0.3276` n `107`; fx avg `0.0027` n `6`; index avg `-0.0526` n `25`; metal avg `0.2266` n `20`; unknown avg `-0.3269` n `780`
- 24h: commodity avg `0.2324` n `12`; crypto_alt avg `1.1574` n `230`; crypto_major avg `1.0082` n `8`; equity avg `1.3945` n `107`; fx avg `0.0275` n `6`; index avg `0.112` n `25`; metal avg `0.0111` n `20`; unknown avg `0.238` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
