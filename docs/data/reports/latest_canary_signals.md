# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T01:37:27.919957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0379` n `12`; crypto_alt avg `-0.3763` n `232`; crypto_major avg `-0.3272` n `8`; equity avg `-0.1738` n `132`; fx avg `-0.0326` n `6`; index avg `-0.0299` n `26`; metal avg `-0.1227` n `20`; unknown avg `-0.0253` n `792`
- 1h: commodity avg `0.0759` n `12`; crypto_alt avg `-0.6014` n `232`; crypto_major avg `-0.4361` n `8`; equity avg `-0.3172` n `132`; fx avg `-0.029` n `6`; index avg `-0.049` n `26`; metal avg `-0.1799` n `20`; unknown avg `-0.2164` n `790`
- 4h: commodity avg `0.3338` n `12`; crypto_alt avg `-0.2506` n `232`; crypto_major avg `-0.0509` n `8`; equity avg `-0.1969` n `132`; fx avg `-0.0716` n `6`; index avg `-0.0246` n `26`; metal avg `-0.2408` n `20`; unknown avg `0.2678` n `790`
- 24h: commodity avg `1.0334` n `12`; crypto_alt avg `-1.4165` n `232`; crypto_major avg `-2.0792` n `8`; equity avg `-2.3111` n `130`; fx avg `-0.0708` n `6`; index avg `-0.4088` n `26`; metal avg `-1.1525` n `20`; unknown avg `-0.2649` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0452`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0408`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0382`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0314`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0303`, n `668`, weak_sample_signal
