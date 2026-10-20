# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T18:37:29.785758+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.151` n `13`; crypto_alt avg `-0.168` n `237`; crypto_major avg `-0.1523` n `8`; equity avg `-0.1999` n `151`; fx avg `0.0011` n `6`; index avg `-0.0414` n `26`; metal avg `-0.0309` n `20`; unknown avg `1.4619` n `1199`
- 1h: commodity avg `0.0943` n `13`; crypto_alt avg `-0.3417` n `237`; crypto_major avg `-0.3017` n `8`; equity avg `-0.2404` n `151`; fx avg `0.008` n `6`; index avg `-0.0439` n `26`; metal avg `-0.0138` n `20`; unknown avg `8.4358` n `1185`
- 4h: commodity avg `0.4045` n `13`; crypto_alt avg `-1.1373` n `237`; crypto_major avg `-1.0723` n `8`; equity avg `-0.6757` n `151`; fx avg `-0.0124` n `6`; index avg `-0.1042` n `26`; metal avg `-0.1989` n `20`; unknown avg `9.5424` n `1177`
- 24h: commodity avg `-0.1173` n `13`; crypto_alt avg `2.7143` n `237`; crypto_major avg `1.5655` n `8`; equity avg `0.2328` n `151`; fx avg `0.0266` n `6`; index avg `0.0189` n `26`; metal avg `-0.0061` n `20`; unknown avg `4.0928` n `1044`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1796`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
