# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T03:07:29.755533+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0098` n `13`; crypto_alt avg `0.0813` n `239`; crypto_major avg `-0.0713` n `8`; equity avg `0.0529` n `168`; fx avg `0.007` n `6`; index avg `0.0057` n `27`; metal avg `-0.0158` n `20`; unknown avg `0.1392` n `1251`
- 1h: commodity avg `0.0538` n `13`; crypto_alt avg `-0.4684` n `239`; crypto_major avg `-0.4333` n `8`; equity avg `0.0466` n `168`; fx avg `-0.0023` n `6`; index avg `-0.0014` n `27`; metal avg `0.0341` n `20`; unknown avg `1.135` n `1257`
- 4h: commodity avg `-0.0728` n `13`; crypto_alt avg `-0.3538` n `239`; crypto_major avg `0.1989` n `8`; equity avg `0.3057` n `168`; fx avg `-0.0049` n `6`; index avg `0.0383` n `27`; metal avg `0.0342` n `20`; unknown avg `-0.0` n `1239`
- 24h: commodity avg `-0.7104` n `13`; crypto_alt avg `-1.5216` n `239`; crypto_major avg `-1.607` n `8`; equity avg `1.3367` n `168`; fx avg `-0.2008` n `6`; index avg `0.1327` n `27`; metal avg `0.1025` n `20`; unknown avg `278.7185` n `983`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
