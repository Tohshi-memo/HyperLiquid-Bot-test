# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T11:07:30.027617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0226` n `13`; crypto_alt avg `0.1468` n `235`; crypto_major avg `0.1492` n `8`; equity avg `0.0093` n `150`; fx avg `-0.0275` n `6`; index avg `-0.0002` n `26`; metal avg `0.0007` n `20`; unknown avg `0.3697` n `1076`
- 1h: commodity avg `0.0118` n `13`; crypto_alt avg `-0.6817` n `235`; crypto_major avg `-0.4399` n `8`; equity avg `-0.1312` n `150`; fx avg `-0.0464` n `6`; index avg `-0.029` n `26`; metal avg `-0.0402` n `20`; unknown avg `1.4986` n `1076`
- 4h: commodity avg `-0.0981` n `13`; crypto_alt avg `-0.6348` n `235`; crypto_major avg `-0.3121` n `8`; equity avg `-0.098` n `150`; fx avg `-0.0516` n `6`; index avg `-0.0122` n `26`; metal avg `-0.0785` n `20`; unknown avg `-0.0849` n `1006`
- 24h: commodity avg `-0.5678` n `13`; crypto_alt avg `-1.4679` n `235`; crypto_major avg `-1.5634` n `8`; equity avg `-0.1085` n `150`; fx avg `0.0331` n `6`; index avg `0.0968` n `26`; metal avg `0.5292` n `20`; unknown avg `7.7068` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
