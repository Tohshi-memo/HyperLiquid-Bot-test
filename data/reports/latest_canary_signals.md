# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T06:07:29.758809+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0455` n `12`; crypto_alt avg `0.2985` n `230`; crypto_major avg `0.4006` n `8`; equity avg `0.0738` n `100`; fx avg `-0.0078` n `6`; index avg `0.0281` n `25`; metal avg `0.0824` n `20`; unknown avg `-0.0007` n `759`
- 1h: commodity avg `-0.1264` n `12`; crypto_alt avg `0.3366` n `230`; crypto_major avg `0.4095` n `8`; equity avg `0.2158` n `100`; fx avg `-0.0027` n `6`; index avg `0.067` n `25`; metal avg `0.06` n `20`; unknown avg `0.0063` n `759`
- 4h: commodity avg `-0.2461` n `12`; crypto_alt avg `0.3261` n `230`; crypto_major avg `0.6579` n `8`; equity avg `0.7286` n `100`; fx avg `-0.0085` n `6`; index avg `0.1619` n `25`; metal avg `-0.0397` n `20`; unknown avg `-0.0079` n `759`
- 24h: commodity avg `-0.6304` n `12`; crypto_alt avg `1.32` n `230`; crypto_major avg `1.7703` n `8`; equity avg `1.1968` n `100`; fx avg `0.0697` n `6`; index avg `0.185` n `25`; metal avg `0.4181` n `20`; unknown avg `-0.0198` n `759`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
