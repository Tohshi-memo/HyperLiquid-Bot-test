# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T01:22:27.989774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0266` n `12`; crypto_alt avg `0.3748` n `232`; crypto_major avg `0.2648` n `8`; equity avg `0.0623` n `133`; fx avg `-0.0334` n `6`; index avg `0.0236` n `26`; metal avg `0.0389` n `20`; unknown avg `15.5886` n `792`
- 1h: commodity avg `0.0121` n `12`; crypto_alt avg `0.5199` n `232`; crypto_major avg `0.3909` n `8`; equity avg `0.2565` n `133`; fx avg `-0.065` n `6`; index avg `0.0765` n `26`; metal avg `0.0842` n `20`; unknown avg `15.6241` n `790`
- 4h: commodity avg `0.0837` n `12`; crypto_alt avg `0.6551` n `232`; crypto_major avg `0.3284` n `8`; equity avg `0.2038` n `133`; fx avg `-0.0222` n `6`; index avg `0.0209` n `26`; metal avg `0.0535` n `20`; unknown avg `15.2098` n `790`
- 24h: commodity avg `0.0051` n `12`; crypto_alt avg `0.6894` n `232`; crypto_major avg `0.2086` n `8`; equity avg `1.1928` n `133`; fx avg `-0.3784` n `6`; index avg `0.1193` n `26`; metal avg `0.6312` n `20`; unknown avg `-0.3441` n `751`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0478`, n `668`, weak_sample_signal
