# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T20:22:32.143222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0648` n `13`; crypto_alt avg `-0.152` n `237`; crypto_major avg `-0.0968` n `8`; equity avg `0.0514` n `151`; fx avg `-0.0057` n `6`; index avg `0.0123` n `26`; metal avg `0.0044` n `20`; unknown avg `0.9048` n `1181`
- 1h: commodity avg `-0.0818` n `13`; crypto_alt avg `0.3022` n `237`; crypto_major avg `0.4015` n `8`; equity avg `0.0447` n `151`; fx avg `-0.0107` n `6`; index avg `0.0408` n `26`; metal avg `0.0316` n `20`; unknown avg `89.2863` n `1161`
- 4h: commodity avg `0.1399` n `13`; crypto_alt avg `0.318` n `237`; crypto_major avg `0.5902` n `8`; equity avg `-0.0557` n `151`; fx avg `0.0032` n `6`; index avg `0.0308` n `26`; metal avg `0.012` n `20`; unknown avg `33.4266` n `1149`
- 24h: commodity avg `-0.1347` n `13`; crypto_alt avg `2.1698` n `237`; crypto_major avg `1.489` n `8`; equity avg `0.113` n `151`; fx avg `0.0255` n `6`; index avg `0.0213` n `26`; metal avg `0.034` n `20`; unknown avg `6.6914` n `1050`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1817`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
