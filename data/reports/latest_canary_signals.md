# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T09:52:27.261173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2207` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0118` n `12`; crypto_alt avg `0.0355` n `233`; crypto_major avg `0.0591` n `8`; equity avg `0.0159` n `136`; fx avg `-0.0007` n `6`; index avg `0.0079` n `27`; metal avg `0.0033` n `20`; unknown avg `-0.0165` n `838`
- 1h: commodity avg `0.0014` n `12`; crypto_alt avg `-0.3664` n `233`; crypto_major avg `-0.5994` n `8`; equity avg `-0.4835` n `136`; fx avg `0.0068` n `6`; index avg `-0.0834` n `27`; metal avg `-0.0198` n `20`; unknown avg `0.0091` n `830`
- 4h: commodity avg `-0.0285` n `12`; crypto_alt avg `-1.0271` n `233`; crypto_major avg `-1.3812` n `8`; equity avg `-1.0122` n `136`; fx avg `0.0069` n `6`; index avg `-0.1605` n `26`; metal avg `-0.0497` n `20`; unknown avg `-0.0421` n `804`
- 24h: commodity avg `0.0757` n `12`; crypto_alt avg `-0.3626` n `233`; crypto_major avg `-1.5286` n `8`; equity avg `-1.5635` n `136`; fx avg `-0.0031` n `6`; index avg `-0.2498` n `26`; metal avg `-0.0177` n `20`; unknown avg `0.0473` n `708`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0857`, n `670`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0769`, n `670`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0749`, n `670`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0733`, n `670`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0662`, n `670`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0647`, n `670`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0636`, n `670`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0562`, n `670`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0553`, n `670`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0553`, n `670`, weak_sample_signal
