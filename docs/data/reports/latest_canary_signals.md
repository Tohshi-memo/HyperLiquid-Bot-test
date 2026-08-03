# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T23:52:32.605948+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0907` n `12`; crypto_alt avg `0.0461` n `230`; crypto_major avg `0.0165` n `8`; equity avg `0.1165` n `107`; fx avg `0.0165` n `6`; index avg `0.026` n `25`; metal avg `0.0232` n `20`; unknown avg `-0.0396` n `780`
- 1h: commodity avg `0.1186` n `12`; crypto_alt avg `-0.0666` n `230`; crypto_major avg `-0.079` n `8`; equity avg `0.1689` n `107`; fx avg `0.0326` n `6`; index avg `0.0463` n `25`; metal avg `0.0299` n `20`; unknown avg `-0.1185` n `780`
- 4h: commodity avg `0.0219` n `12`; crypto_alt avg `-0.1875` n `230`; crypto_major avg `-0.5249` n `8`; equity avg `0.5108` n `107`; fx avg `0.0757` n `6`; index avg `0.1241` n `25`; metal avg `0.0355` n `20`; unknown avg `0.1173` n `780`
- 24h: commodity avg `0.0373` n `12`; crypto_alt avg `0.1854` n `230`; crypto_major avg `-0.0441` n `8`; equity avg `2.145` n `107`; fx avg `-0.2316` n `6`; index avg `0.1423` n `25`; metal avg `-0.2408` n `20`; unknown avg `0.0498` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
