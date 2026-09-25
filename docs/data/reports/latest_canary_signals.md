# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T18:52:37.773835+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0826` n `12`; crypto_alt avg `0.1731` n `234`; crypto_major avg `0.0133` n `8`; equity avg `0.0061` n `141`; fx avg `0.0036` n `6`; index avg `0.0027` n `26`; metal avg `0.0353` n `20`; unknown avg `-0.0806` n `960`
- 1h: commodity avg `-0.0948` n `12`; crypto_alt avg `0.7053` n `234`; crypto_major avg `0.4716` n `8`; equity avg `-0.0198` n `141`; fx avg `0.0025` n `6`; index avg `0.0028` n `26`; metal avg `0.0713` n `20`; unknown avg `2.9688` n `958`
- 4h: commodity avg `-0.299` n `12`; crypto_alt avg `1.3062` n `234`; crypto_major avg `0.5568` n `8`; equity avg `0.4428` n `141`; fx avg `-0.0314` n `6`; index avg `0.1524` n `26`; metal avg `0.2263` n `20`; unknown avg `0.7453` n `930`
- 24h: commodity avg `-0.8536` n `12`; crypto_alt avg `2.1822` n `234`; crypto_major avg `0.4472` n `8`; equity avg `-0.0421` n `141`; fx avg `-0.2558` n `6`; index avg `0.1861` n `26`; metal avg `0.145` n `20`; unknown avg `1595.0715` n `807`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1751`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
