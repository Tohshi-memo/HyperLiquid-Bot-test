# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T05:37:34.199238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0236` n `13`; crypto_alt avg `-0.2203` n `237`; crypto_major avg `-0.2708` n `8`; equity avg `-0.1535` n `151`; fx avg `-0.0172` n `6`; index avg `-0.014` n `26`; metal avg `-0.0212` n `20`; unknown avg `-0.2653` n `1198`
- 1h: commodity avg `-0.0111` n `13`; crypto_alt avg `-0.558` n `237`; crypto_major avg `-0.446` n `8`; equity avg `-0.4422` n `151`; fx avg `0.0006` n `6`; index avg `-0.0562` n `26`; metal avg `-0.0782` n `20`; unknown avg `-0.3744` n `1196`
- 4h: commodity avg `-0.0611` n `13`; crypto_alt avg `0.3261` n `237`; crypto_major avg `0.1946` n `8`; equity avg `-0.3678` n `151`; fx avg `0.0035` n `6`; index avg `-0.1038` n `26`; metal avg `0.1728` n `20`; unknown avg `1.942` n `1188`
- 24h: commodity avg `0.2499` n `13`; crypto_alt avg `0.0258` n `237`; crypto_major avg `-0.6618` n `8`; equity avg `-1.5387` n `151`; fx avg `-0.0031` n `6`; index avg `-0.2735` n `26`; metal avg `-0.2892` n `20`; unknown avg `5.4914` n `1010`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2022`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
