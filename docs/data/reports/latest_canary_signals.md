# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T01:07:26.822337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0771` n `12`; crypto_alt avg `-0.0757` n `230`; crypto_major avg `-0.1846` n `8`; equity avg `-0.2175` n `92`; fx avg `0.002` n `6`; index avg `-0.0622` n `25`; metal avg `-0.0108` n `20`; unknown avg `0.0706` n `768`
- 1h: commodity avg `0.0181` n `12`; crypto_alt avg `-0.1521` n `230`; crypto_major avg `-0.4041` n `8`; equity avg `-0.1198` n `92`; fx avg `0.0109` n `6`; index avg `-0.0082` n `25`; metal avg `0.0268` n `20`; unknown avg `-0.0403` n `768`
- 4h: commodity avg `0.1104` n `12`; crypto_alt avg `0.2317` n `230`; crypto_major avg `-0.0623` n `8`; equity avg `0.3129` n `92`; fx avg `0.0202` n `6`; index avg `0.0618` n `25`; metal avg `0.0717` n `20`; unknown avg `0.3852` n `766`
- 24h: commodity avg `0.1087` n `12`; crypto_alt avg `1.6082` n `230`; crypto_major avg `2.9253` n `8`; equity avg `1.2303` n `92`; fx avg `0.058` n `6`; index avg `0.3794` n `25`; metal avg `0.7493` n `20`; unknown avg `0.1428` n `740`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
