# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T23:22:27.076191+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0136` n `12`; crypto_alt avg `0.1545` n `233`; crypto_major avg `0.0255` n `8`; equity avg `-0.0086` n `136`; fx avg `-0.0027` n `6`; index avg `0.0014` n `26`; metal avg `-0.0044` n `20`; unknown avg `-0.0147` n `838`
- 1h: commodity avg `-0.0177` n `12`; crypto_alt avg `-0.0769` n `233`; crypto_major avg `-0.065` n `8`; equity avg `-0.0163` n `136`; fx avg `-0.0016` n `6`; index avg `-0.0047` n `26`; metal avg `-0.012` n `20`; unknown avg `-0.1219` n `836`
- 4h: commodity avg `-0.0174` n `12`; crypto_alt avg `-0.076` n `233`; crypto_major avg `0.017` n `8`; equity avg `-0.2906` n `136`; fx avg `-0.0026` n `6`; index avg `-0.0302` n `26`; metal avg `-0.0319` n `20`; unknown avg `0.2825` n `796`
- 24h: commodity avg `-0.0864` n `12`; crypto_alt avg `1.5307` n `233`; crypto_major avg `0.2998` n `8`; equity avg `-0.3001` n `136`; fx avg `-0.0172` n `6`; index avg `-0.0041` n `26`; metal avg `-0.0006` n `20`; unknown avg `0.4362` n `724`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.05`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0465`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0451`, n `668`, weak_sample_signal
