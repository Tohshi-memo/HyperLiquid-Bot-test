# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T20:22:23.986122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0599` n `12`; crypto_alt avg `0.1979` n `228`; crypto_major avg `0.1747` n `8`; equity avg `0.0064` n `74`; fx avg `0.0031` n `6`; index avg `-0.034` n `23`; metal avg `-0.0054` n `18`; unknown avg `-0.0886` n `515`
- 1h: commodity avg `0.1178` n `12`; crypto_alt avg `-0.3608` n `228`; crypto_major avg `-0.2738` n `8`; equity avg `0.1025` n `74`; fx avg `-0.0163` n `6`; index avg `-0.0064` n `23`; metal avg `-0.0224` n `18`; unknown avg `4.2183` n `515`
- 4h: commodity avg `0.1176` n `12`; crypto_alt avg `-0.5262` n `228`; crypto_major avg `-0.6931` n `8`; equity avg `0.1348` n `74`; fx avg `0.0466` n `6`; index avg `-0.1526` n `23`; metal avg `0.045` n `18`; unknown avg `0.0695` n `515`
- 24h: commodity avg `0.4774` n `12`; crypto_alt avg `-1.7981` n `228`; crypto_major avg `-1.8259` n `8`; equity avg `-0.6027` n `74`; fx avg `0.0727` n `6`; index avg `0.1797` n `23`; metal avg `-0.2709` n `18`; unknown avg `-0.5447` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
