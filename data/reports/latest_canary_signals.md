# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T04:07:29.544700+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0038` n `13`; crypto_alt avg `-0.1248` n `235`; crypto_major avg `-0.0438` n `8`; equity avg `-0.0189` n `151`; fx avg `0.009` n `6`; index avg `0.005` n `26`; metal avg `-0.0252` n `20`; unknown avg `-0.0433` n `1125`
- 1h: commodity avg `0.0407` n `13`; crypto_alt avg `-0.0788` n `235`; crypto_major avg `-0.0982` n `8`; equity avg `-0.0758` n `151`; fx avg `0.0041` n `6`; index avg `-0.0045` n `26`; metal avg `-0.022` n `20`; unknown avg `1.2346` n `1125`
- 4h: commodity avg `-0.1306` n `13`; crypto_alt avg `-0.2715` n `235`; crypto_major avg `0.0068` n `8`; equity avg `-0.7884` n `151`; fx avg `-0.0314` n `6`; index avg `-0.0418` n `26`; metal avg `0.0475` n `20`; unknown avg `0.2949` n `1097`
- 24h: commodity avg `-0.4559` n `13`; crypto_alt avg `3.2628` n `235`; crypto_major avg `1.4658` n `8`; equity avg `-0.2062` n `151`; fx avg `-0.0607` n `6`; index avg `0.0252` n `26`; metal avg `0.1409` n `20`; unknown avg `1.1337` n `928`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
