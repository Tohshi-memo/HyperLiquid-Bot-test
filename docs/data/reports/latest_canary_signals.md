# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T10:04:18.047233+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0109` n `12`; crypto_alt avg `0.0633` n `230`; crypto_major avg `0.0187` n `8`; equity avg `-0.02` n `114`; fx avg `-0.0107` n `6`; index avg `-0.0024` n `25`; metal avg `-0.0167` n `20`; unknown avg `0.0125` n `792`
- 1h: commodity avg `0.0822` n `12`; crypto_alt avg `-0.0768` n `230`; crypto_major avg `-0.0058` n `8`; equity avg `-0.0718` n `114`; fx avg `0.0198` n `6`; index avg `-0.011` n `25`; metal avg `-0.0291` n `20`; unknown avg `0.059` n `792`
- 4h: commodity avg `0.2084` n `12`; crypto_alt avg `-0.259` n `230`; crypto_major avg `-0.1158` n `8`; equity avg `0.0889` n `114`; fx avg `-0.003` n `6`; index avg `-0.0103` n `25`; metal avg `-0.1466` n `20`; unknown avg `0.201` n `792`
- 24h: commodity avg `-0.0162` n `12`; crypto_alt avg `-0.2866` n `230`; crypto_major avg `0.5978` n `8`; equity avg `1.1391` n `114`; fx avg `-0.0169` n `6`; index avg `0.1275` n `25`; metal avg `0.1175` n `20`; unknown avg `0.068` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.167`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
