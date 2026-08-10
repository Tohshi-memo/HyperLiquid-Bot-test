# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T09:37:32.081437+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0434` n `12`; crypto_alt avg `-0.0864` n `230`; crypto_major avg `-0.1656` n `8`; equity avg `-0.0499` n `112`; fx avg `-0.009` n `6`; index avg `-0.0042` n `25`; metal avg `-0.0298` n `20`; unknown avg `-0.0049` n `785`
- 1h: commodity avg `0.0873` n `12`; crypto_alt avg `-0.1884` n `230`; crypto_major avg `-0.1991` n `8`; equity avg `-0.1279` n `112`; fx avg `0.008` n `6`; index avg `-0.0141` n `25`; metal avg `-0.0339` n `20`; unknown avg `0.0484` n `785`
- 4h: commodity avg `0.182` n `12`; crypto_alt avg `0.1172` n `230`; crypto_major avg `0.0297` n `8`; equity avg `0.2166` n `112`; fx avg `0.0897` n `6`; index avg `0.0328` n `25`; metal avg `-0.0885` n `20`; unknown avg `57.2904` n `753`
- 24h: commodity avg `0.4022` n `12`; crypto_alt avg `0.9007` n `230`; crypto_major avg `0.1244` n `8`; equity avg `-0.0553` n `112`; fx avg `0.2272` n `6`; index avg `0.069` n `25`; metal avg `-0.1235` n `20`; unknown avg `56.9883` n `753`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1852`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
