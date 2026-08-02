# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T03:37:36.774822+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.505` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0424` n `12`; crypto_alt avg `-0.0559` n `230`; crypto_major avg `-0.0041` n `8`; equity avg `0.0168` n `102`; fx avg `-0.0181` n `6`; index avg `0.0358` n `25`; metal avg `0.0184` n `20`; unknown avg `-0.0729` n `782`
- 1h: commodity avg `-0.3283` n `12`; crypto_alt avg `0.0886` n `230`; crypto_major avg `0.2777` n `8`; equity avg `0.025` n `102`; fx avg `-0.035` n `6`; index avg `0.056` n `25`; metal avg `0.0662` n `20`; unknown avg `-0.3006` n `782`
- 4h: commodity avg `-1.2136` n `12`; crypto_alt avg `1.102` n `230`; crypto_major avg `1.2914` n `8`; equity avg `0.9692` n `102`; fx avg `0.018` n `6`; index avg `0.2513` n `25`; metal avg `0.1612` n `20`; unknown avg `2.2198` n `782`
- 24h: commodity avg `-1.2544` n `12`; crypto_alt avg `0.1099` n `230`; crypto_major avg `0.4067` n `8`; equity avg `0.7898` n `102`; fx avg `-0.0708` n `6`; index avg `0.2138` n `25`; metal avg `0.2248` n `20`; unknown avg `-0.0453` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
