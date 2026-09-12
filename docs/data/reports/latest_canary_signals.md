# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T08:52:26.309937+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.64` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `-0.0137` n `233`; crypto_major avg `0.0642` n `8`; equity avg `-0.0017` n `136`; fx avg `0.0021` n `6`; index avg `0.0018` n `26`; metal avg `0.003` n `20`; unknown avg `-0.1311` n `838`
- 1h: commodity avg `-0.0057` n `12`; crypto_alt avg `-0.0335` n `233`; crypto_major avg `0.1512` n `8`; equity avg `-0.005` n `136`; fx avg `0.0048` n `6`; index avg `-0.0002` n `26`; metal avg `0.0062` n `20`; unknown avg `0.2928` n `830`
- 4h: commodity avg `-0.0254` n `12`; crypto_alt avg `0.5263` n `233`; crypto_major avg `0.3371` n `8`; equity avg `-0.0481` n `136`; fx avg `-0.0015` n `6`; index avg `0.0113` n `26`; metal avg `0.0188` n `20`; unknown avg `-0.0087` n `800`
- 24h: commodity avg `-0.2027` n `12`; crypto_alt avg `1.3912` n `233`; crypto_major avg `0.9275` n `8`; equity avg `-0.0305` n `136`; fx avg `-0.0758` n `6`; index avg `0.106` n `26`; metal avg `-0.0735` n `20`; unknown avg `0.8776` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
