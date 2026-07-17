# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T12:52:29.247468+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0506` n `12`; crypto_alt avg `-0.1008` n `230`; crypto_major avg `-0.1278` n `8`; equity avg `-0.1526` n `96`; fx avg `0.0079` n `6`; index avg `-0.0135` n `25`; metal avg `-0.0318` n `20`; unknown avg `0.0119` n `769`
- 1h: commodity avg `0.038` n `12`; crypto_alt avg `-0.2819` n `230`; crypto_major avg `-0.499` n `8`; equity avg `-0.6051` n `96`; fx avg `-0.0021` n `6`; index avg `-0.0618` n `25`; metal avg `-0.1442` n `20`; unknown avg `0.1212` n `769`
- 4h: commodity avg `0.2752` n `12`; crypto_alt avg `0.069` n `230`; crypto_major avg `0.0085` n `8`; equity avg `0.5732` n `96`; fx avg `-0.023` n `6`; index avg `0.0875` n `25`; metal avg `-0.1426` n `20`; unknown avg `0.2057` n `768`
- 24h: commodity avg `-0.1587` n `12`; crypto_alt avg `-1.5915` n `230`; crypto_major avg `-2.5489` n `8`; equity avg `-4.5626` n `94`; fx avg `-0.0562` n `6`; index avg `-0.5389` n `25`; metal avg `-0.5587` n `20`; unknown avg `-0.286` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
