# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T01:07:26.652188+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0256` n `12`; crypto_alt avg `0.1825` n `230`; crypto_major avg `0.2714` n `8`; equity avg `0.1821` n `94`; fx avg `0.0046` n `6`; index avg `-0.0208` n `25`; metal avg `0.0406` n `20`; unknown avg `0.1897` n `768`
- 1h: commodity avg `0.0556` n `12`; crypto_alt avg `0.4928` n `230`; crypto_major avg `0.4933` n `8`; equity avg `-0.1059` n `94`; fx avg `-0.0439` n `6`; index avg `-0.0436` n `25`; metal avg `0.0493` n `20`; unknown avg `0.0951` n `768`
- 4h: commodity avg `0.0338` n `12`; crypto_alt avg `-0.5902` n `230`; crypto_major avg `-0.4877` n `8`; equity avg `-0.8151` n `94`; fx avg `-0.0174` n `6`; index avg `-0.1522` n `25`; metal avg `0.0503` n `20`; unknown avg `-0.4162` n `768`
- 24h: commodity avg `-0.117` n `12`; crypto_alt avg `-1.3376` n `230`; crypto_major avg `-2.147` n `8`; equity avg `-4.1081` n `94`; fx avg `-0.1925` n `6`; index avg `-0.507` n `25`; metal avg `-0.6506` n `20`; unknown avg `-0.6197` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
