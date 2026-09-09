# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T07:22:32.757755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0639` n `12`; crypto_alt avg `-0.0768` n `233`; crypto_major avg `-0.0862` n `8`; equity avg `-0.031` n `134`; fx avg `0.0353` n `6`; index avg `-0.0006` n `26`; metal avg `0.0354` n `20`; unknown avg `0.421` n `798`
- 1h: commodity avg `0.1203` n `12`; crypto_alt avg `0.1848` n `233`; crypto_major avg `0.078` n `8`; equity avg `-0.019` n `134`; fx avg `0.0395` n `6`; index avg `0.0063` n `26`; metal avg `0.0794` n `20`; unknown avg `0.3342` n `796`
- 4h: commodity avg `0.0199` n `12`; crypto_alt avg `1.5619` n `233`; crypto_major avg `1.204` n `8`; equity avg `0.0419` n `134`; fx avg `-0.0173` n `6`; index avg `0.0006` n `26`; metal avg `0.2124` n `20`; unknown avg `0.6143` n `771`
- 24h: commodity avg `-0.1237` n `12`; crypto_alt avg `0.898` n `232`; crypto_major avg `1.7413` n `8`; equity avg `1.0926` n `134`; fx avg `-0.1058` n `6`; index avg `0.0313` n `26`; metal avg `0.0091` n `20`; unknown avg `0.679` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
