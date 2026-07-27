# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T12:52:31.027831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0321` n `12`; crypto_alt avg `0.152` n `230`; crypto_major avg `0.2574` n `8`; equity avg `0.1267` n `100`; fx avg `0.0067` n `6`; index avg `0.0168` n `25`; metal avg `0.0171` n `20`; unknown avg `0.1106` n `776`
- 1h: commodity avg `0.1988` n `12`; crypto_alt avg `-0.0883` n `230`; crypto_major avg `-0.0034` n `8`; equity avg `0.0058` n `100`; fx avg `-0.0033` n `6`; index avg `0.0083` n `25`; metal avg `-0.0462` n `20`; unknown avg `0.1074` n `776`
- 4h: commodity avg `0.2327` n `12`; crypto_alt avg `-0.0998` n `230`; crypto_major avg `-0.0516` n `8`; equity avg `-0.2826` n `100`; fx avg `-0.0361` n `6`; index avg `-0.0486` n `25`; metal avg `-0.0443` n `20`; unknown avg `-0.0805` n `775`
- 24h: commodity avg `-0.3977` n `12`; crypto_alt avg `0.3915` n `230`; crypto_major avg `1.1343` n `8`; equity avg `0.9279` n `100`; fx avg `0.0791` n `6`; index avg `0.1063` n `25`; metal avg `0.269` n `20`; unknown avg `-0.1115` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1754`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
