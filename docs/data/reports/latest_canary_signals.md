# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T23:51:38.483431+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0051` n `13`; crypto_alt avg `-0.0043` n `239`; crypto_major avg `0.1473` n `8`; equity avg `0.1139` n `162`; fx avg `-0.0138` n `6`; index avg `-0.002` n `27`; metal avg `0.0263` n `20`; unknown avg `-0.0973` n `1261`
- 1h: commodity avg `0.0098` n `13`; crypto_alt avg `0.0494` n `239`; crypto_major avg `0.3358` n `8`; equity avg `0.5804` n `162`; fx avg `-0.0051` n `6`; index avg `0.0657` n `27`; metal avg `0.0569` n `20`; unknown avg `1.0951` n `1257`
- 4h: commodity avg `-0.0132` n `13`; crypto_alt avg `0.3882` n `239`; crypto_major avg `0.2658` n `8`; equity avg `0.774` n `162`; fx avg `-0.0168` n `6`; index avg `0.0806` n `27`; metal avg `0.0291` n `20`; unknown avg `0.0754` n `1187`
- 24h: commodity avg `0.9073` n `13`; crypto_alt avg `-0.7833` n `239`; crypto_major avg `-1.5909` n `8`; equity avg `-0.1616` n `162`; fx avg `-0.1264` n `6`; index avg `0.0829` n `27`; metal avg `-0.5491` n `20`; unknown avg `50.599` n `1121`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
