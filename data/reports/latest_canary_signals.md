# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T12:58:07.317822+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0172` n `12`; crypto_alt avg `-0.0522` n `230`; crypto_major avg `-0.0191` n `8`; equity avg `-0.0113` n `94`; fx avg `0.0238` n `6`; index avg `0.0044` n `25`; metal avg `-0.1213` n `20`; unknown avg `-0.011` n `768`
- 1h: commodity avg `0.2001` n `12`; crypto_alt avg `-0.0806` n `230`; crypto_major avg `-0.3837` n `8`; equity avg `-0.1668` n `94`; fx avg `0.0303` n `6`; index avg `-0.0569` n `25`; metal avg `-0.2696` n `20`; unknown avg `0.1852` n `768`
- 4h: commodity avg `0.3283` n `12`; crypto_alt avg `0.0279` n `230`; crypto_major avg `-0.3569` n `8`; equity avg `-0.7503` n `94`; fx avg `-0.0052` n `6`; index avg `-0.2045` n `25`; metal avg `-0.3877` n `20`; unknown avg `0.0201` n `762`
- 24h: commodity avg `0.271` n `12`; crypto_alt avg `-1.6104` n `230`; crypto_major avg `-2.0165` n `8`; equity avg `-3.6375` n `93`; fx avg `0.0452` n `6`; index avg `-0.671` n `25`; metal avg `-0.5331` n `20`; unknown avg `-0.0319` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
