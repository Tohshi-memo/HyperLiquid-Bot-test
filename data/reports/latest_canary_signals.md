# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T08:52:27.028673+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `-0.2008` n `230`; crypto_major avg `-0.2593` n `8`; equity avg `0.0014` n `94`; fx avg `0.0079` n `6`; index avg `-0.0009` n `25`; metal avg `0.0309` n `20`; unknown avg `-0.0847` n `768`
- 1h: commodity avg `0.0187` n `12`; crypto_alt avg `-0.3873` n `230`; crypto_major avg `-0.3189` n `8`; equity avg `-0.1348` n `94`; fx avg `-0.0093` n `6`; index avg `0.0136` n `25`; metal avg `0.0779` n `20`; unknown avg `-0.0784` n `768`
- 4h: commodity avg `-0.004` n `12`; crypto_alt avg `-0.9867` n `230`; crypto_major avg `-0.7897` n `8`; equity avg `-0.7049` n `94`; fx avg `-0.0514` n `6`; index avg `-0.0576` n `25`; metal avg `-0.0924` n `20`; unknown avg `-0.0878` n `752`
- 24h: commodity avg `0.0044` n `12`; crypto_alt avg `-0.6738` n `230`; crypto_major avg `-0.7825` n `8`; equity avg `-2.804` n `93`; fx avg `0.0584` n `6`; index avg `-0.4672` n `25`; metal avg `-0.1057` n `20`; unknown avg `-0.23` n `749`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
