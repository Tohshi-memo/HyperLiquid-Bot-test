# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T21:37:39.252098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0319` n `12`; crypto_alt avg `0.1268` n `234`; crypto_major avg `0.0852` n `8`; equity avg `-0.0313` n `142`; fx avg `-0.0012` n `6`; index avg `-0.01` n `26`; metal avg `-0.0136` n `20`; unknown avg `0.0999` n `975`
- 1h: commodity avg `-0.0273` n `12`; crypto_alt avg `-0.1605` n `234`; crypto_major avg `0.1278` n `8`; equity avg `-0.2894` n `142`; fx avg `0.0147` n `6`; index avg `-0.0597` n `26`; metal avg `0.0108` n `20`; unknown avg `4.2777` n `971`
- 4h: commodity avg `-0.1191` n `12`; crypto_alt avg `-0.5693` n `234`; crypto_major avg `0.1693` n `8`; equity avg `-0.1154` n `142`; fx avg `0.0275` n `6`; index avg `-0.0779` n `26`; metal avg `0.0859` n `20`; unknown avg `1.9573` n `887`
- 24h: commodity avg `0.2044` n `12`; crypto_alt avg `0.1247` n `234`; crypto_major avg `1.0219` n `8`; equity avg `-0.5408` n `142`; fx avg `0.0952` n `6`; index avg `-0.0729` n `26`; metal avg `-0.2176` n `20`; unknown avg `788.6546` n `788`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
