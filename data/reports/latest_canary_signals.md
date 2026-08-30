# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T20:52:25.478781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `-0.2315` n `231`; crypto_major avg `-0.2254` n `8`; equity avg `-0.017` n `128`; fx avg `-0.0018` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0037` n `20`; unknown avg `0.1293` n `793`
- 1h: commodity avg `0.1701` n `12`; crypto_alt avg `-0.3296` n `231`; crypto_major avg `-0.3669` n `8`; equity avg `-0.0752` n `128`; fx avg `-0.0031` n `6`; index avg `-0.0273` n `26`; metal avg `-0.0348` n `20`; unknown avg `-0.0543` n `791`
- 4h: commodity avg `0.4619` n `12`; crypto_alt avg `-0.6113` n `231`; crypto_major avg `-0.9773` n `8`; equity avg `-0.1611` n `128`; fx avg `-0.007` n `6`; index avg `-0.0417` n `26`; metal avg `-0.0768` n `20`; unknown avg `0.3202` n `791`
- 24h: commodity avg `0.4942` n `12`; crypto_alt avg `1.2016` n `231`; crypto_major avg `0.3611` n `8`; equity avg `0.0558` n `128`; fx avg `0.0258` n `6`; index avg `0.0205` n `26`; metal avg `0.0535` n `20`; unknown avg `0.1615` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
