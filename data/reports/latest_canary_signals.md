# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T03:37:25.525503+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0147` n `13`; crypto_alt avg `-0.0043` n `239`; crypto_major avg `0.0655` n `8`; equity avg `0.0312` n `168`; fx avg `0.0046` n `6`; index avg `0.0012` n `27`; metal avg `-0.0114` n `20`; unknown avg `0.337` n `1265`
- 1h: commodity avg `-0.0007` n `13`; crypto_alt avg `-0.236` n `239`; crypto_major avg `-0.0759` n `8`; equity avg `-0.0048` n `168`; fx avg `0.0073` n `6`; index avg `-0.0057` n `27`; metal avg `-0.0361` n `20`; unknown avg `0.8695` n `1263`
- 4h: commodity avg `-0.0825` n `13`; crypto_alt avg `-0.578` n `239`; crypto_major avg `0.2966` n `8`; equity avg `0.2314` n `168`; fx avg `0.0112` n `6`; index avg `0.0301` n `27`; metal avg `0.0074` n `20`; unknown avg `1.0601` n `1245`
- 24h: commodity avg `-0.7403` n `13`; crypto_alt avg `-1.6272` n `239`; crypto_major avg `-1.7586` n `8`; equity avg `0.9048` n `168`; fx avg `-0.1454` n `6`; index avg `0.0965` n `27`; metal avg `0.1106` n `20`; unknown avg `290.3606` n `987`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
