# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T20:07:27.767762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0195` n `12`; crypto_alt avg `0.1383` n `232`; crypto_major avg `0.0751` n `8`; equity avg `0.0768` n `134`; fx avg `0.0012` n `6`; index avg `0.0088` n `26`; metal avg `0.0009` n `20`; unknown avg `22.8714` n `792`
- 1h: commodity avg `0.017` n `12`; crypto_alt avg `0.0727` n `232`; crypto_major avg `-0.2513` n `8`; equity avg `0.053` n `134`; fx avg `-0.0145` n `6`; index avg `0.002` n `26`; metal avg `-0.0045` n `20`; unknown avg `2.9888` n `792`
- 4h: commodity avg `0.045` n `12`; crypto_alt avg `0.6117` n `232`; crypto_major avg `0.7457` n `8`; equity avg `0.1093` n `134`; fx avg `-0.0137` n `6`; index avg `0.0557` n `26`; metal avg `0.0201` n `20`; unknown avg `1.5753` n `786`
- 24h: commodity avg `0.0778` n `12`; crypto_alt avg `2.7823` n `232`; crypto_major avg `2.4866` n `8`; equity avg `0.2475` n `134`; fx avg `-0.0397` n `6`; index avg `0.0388` n `26`; metal avg `0.0371` n `20`; unknown avg `0.0927` n `658`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
