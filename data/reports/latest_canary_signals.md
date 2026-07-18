# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T23:22:33.455819+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0357` n `12`; crypto_alt avg `0.042` n `230`; crypto_major avg `0.0813` n `8`; equity avg `0.0399` n `96`; fx avg `0.0003` n `6`; index avg `0.0061` n `25`; metal avg `0.0089` n `20`; unknown avg `0.173` n `770`
- 1h: commodity avg `0.0153` n `12`; crypto_alt avg `0.0925` n `230`; crypto_major avg `0.0825` n `8`; equity avg `0.039` n `96`; fx avg `-0.0027` n `6`; index avg `0.0107` n `25`; metal avg `0.003` n `20`; unknown avg `0.1002` n `770`
- 4h: commodity avg `-0.0182` n `12`; crypto_alt avg `0.289` n `230`; crypto_major avg `0.2151` n `8`; equity avg `0.0109` n `96`; fx avg `0.0134` n `6`; index avg `0.0038` n `25`; metal avg `-0.0151` n `20`; unknown avg `0.4685` n `770`
- 24h: commodity avg `0.3335` n `12`; crypto_alt avg `-0.1768` n `230`; crypto_major avg `0.6672` n `8`; equity avg `-0.1706` n `96`; fx avg `-0.0778` n `6`; index avg `0.0601` n `25`; metal avg `-0.0323` n `20`; unknown avg `0.1087` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
