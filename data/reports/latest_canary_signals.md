# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T07:22:26.361945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.65` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0101` n `12`; crypto_alt avg `0.27` n `233`; crypto_major avg `0.1148` n `8`; equity avg `0.0224` n `136`; fx avg `0.0018` n `6`; index avg `-0.0009` n `26`; metal avg `-0.0054` n `20`; unknown avg `0.013` n `838`
- 1h: commodity avg `-0.0063` n `12`; crypto_alt avg `0.3928` n `233`; crypto_major avg `0.2353` n `8`; equity avg `-0.0124` n `136`; fx avg `0.0049` n `6`; index avg `0.0019` n `26`; metal avg `0.0005` n `20`; unknown avg `-0.1168` n `836`
- 4h: commodity avg `-0.094` n `12`; crypto_alt avg `0.5333` n `233`; crypto_major avg `0.2247` n `8`; equity avg `-0.0899` n `136`; fx avg `-0.001` n `6`; index avg `0.0079` n `26`; metal avg `0.0053` n `20`; unknown avg `1.9788` n `796`
- 24h: commodity avg `-0.4085` n `12`; crypto_alt avg `1.1539` n `233`; crypto_major avg `0.7956` n `8`; equity avg `0.2069` n `136`; fx avg `-0.1378` n `6`; index avg `0.1577` n `26`; metal avg `-0.0409` n `20`; unknown avg `0.8753` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
