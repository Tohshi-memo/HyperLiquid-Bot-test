# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T17:52:26.874554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0115` n `13`; crypto_alt avg `-0.0585` n `239`; crypto_major avg `-0.0648` n `8`; equity avg `0.0033` n `166`; fx avg `0.0005` n `6`; index avg `0.0031` n `27`; metal avg `-0.0011` n `20`; unknown avg `-0.1063` n `1263`
- 1h: commodity avg `-0.0275` n `13`; crypto_alt avg `-0.0824` n `239`; crypto_major avg `-0.1909` n `8`; equity avg `0.0823` n `166`; fx avg `-0.0012` n `6`; index avg `0.0059` n `27`; metal avg `-0.001` n `20`; unknown avg `-0.0983` n `1251`
- 4h: commodity avg `-0.0271` n `13`; crypto_alt avg `0.0984` n `239`; crypto_major avg `0.543` n `8`; equity avg `0.207` n `166`; fx avg `0.0169` n `6`; index avg `0.012` n `27`; metal avg `0.0812` n `20`; unknown avg `162.1323` n `1231`
- 24h: commodity avg `-0.0532` n `13`; crypto_alt avg `0.8241` n `239`; crypto_major avg `1.0469` n `8`; equity avg `1.0767` n `166`; fx avg `0.009` n `6`; index avg `0.1844` n `27`; metal avg `0.0667` n `20`; unknown avg `187.5033` n `1066`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
