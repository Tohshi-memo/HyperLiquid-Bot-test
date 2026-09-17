# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T08:52:27.244194+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0681` n `12`; crypto_alt avg `0.1181` n `234`; crypto_major avg `0.0181` n `8`; equity avg `0.0902` n `137`; fx avg `-0.0183` n `6`; index avg `0.0067` n `27`; metal avg `-0.1249` n `20`; unknown avg `0.8928` n `921`
- 1h: commodity avg `-0.0875` n `12`; crypto_alt avg `0.3219` n `234`; crypto_major avg `0.2333` n `8`; equity avg `0.2743` n `137`; fx avg `0.0203` n `6`; index avg `-0.0067` n `27`; metal avg `-0.2315` n `20`; unknown avg `0.7671` n `911`
- 4h: commodity avg `-0.2096` n `12`; crypto_alt avg `0.7497` n `234`; crypto_major avg `0.3471` n `8`; equity avg `0.4983` n `137`; fx avg `0.0353` n `6`; index avg `0.0267` n `27`; metal avg `-0.0157` n `20`; unknown avg `0.4035` n `891`
- 24h: commodity avg `-0.5853` n `12`; crypto_alt avg `3.9669` n `234`; crypto_major avg `2.248` n `8`; equity avg `1.5841` n `137`; fx avg `0.0796` n `6`; index avg `0.1014` n `27`; metal avg `-0.123` n `20`; unknown avg `1.2703` n `721`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
