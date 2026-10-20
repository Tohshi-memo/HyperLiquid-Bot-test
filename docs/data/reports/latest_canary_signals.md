# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T08:07:28.254264+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0156` n `13`; crypto_alt avg `-0.3397` n `237`; crypto_major avg `-0.2239` n `8`; equity avg `-0.1057` n `151`; fx avg `-0.007` n `6`; index avg `-0.017` n `26`; metal avg `0.001` n `20`; unknown avg `-0.1626` n `1180`
- 1h: commodity avg `0.0851` n `13`; crypto_alt avg `-0.5048` n `237`; crypto_major avg `-0.4228` n `8`; equity avg `-0.4037` n `151`; fx avg `-0.007` n `6`; index avg `-0.0855` n `26`; metal avg `-0.1106` n `20`; unknown avg `0.5813` n `1180`
- 4h: commodity avg `0.1386` n `13`; crypto_alt avg `-0.9406` n `237`; crypto_major avg `-0.8221` n `8`; equity avg `-0.5985` n `151`; fx avg `-0.0299` n `6`; index avg `-0.0423` n `26`; metal avg `-0.1286` n `20`; unknown avg `2.7162` n `1158`
- 24h: commodity avg `0.4949` n `13`; crypto_alt avg `-0.4555` n `237`; crypto_major avg `-1.005` n `8`; equity avg `-1.6941` n `151`; fx avg `0.0142` n `6`; index avg `-0.2479` n `26`; metal avg `-0.2484` n `20`; unknown avg `4.7349` n `1041`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1849`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
