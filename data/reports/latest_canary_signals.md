# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T21:37:32.618392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `12`; crypto_alt avg `-0.0165` n `230`; crypto_major avg `0.0411` n `8`; equity avg `-0.0115` n `112`; fx avg `-0.0027` n `6`; index avg `-0.0071` n `25`; metal avg `0.0015` n `20`; unknown avg `-0.0627` n `782`
- 1h: commodity avg `-0.0315` n `12`; crypto_alt avg `0.0303` n `230`; crypto_major avg `-0.0764` n `8`; equity avg `0.0087` n `112`; fx avg `0.0147` n `6`; index avg `-0.0073` n `25`; metal avg `0.0839` n `20`; unknown avg `-0.0571` n `782`
- 4h: commodity avg `-0.2085` n `12`; crypto_alt avg `-0.0294` n `230`; crypto_major avg `0.4301` n `8`; equity avg `0.3864` n `112`; fx avg `0.0216` n `6`; index avg `0.0596` n `25`; metal avg `0.1024` n `20`; unknown avg `-0.0665` n `782`
- 24h: commodity avg `-0.0475` n `12`; crypto_alt avg `-0.2083` n `230`; crypto_major avg `-0.0872` n `8`; equity avg `2.1034` n `112`; fx avg `-0.1354` n `6`; index avg `0.1091` n `25`; metal avg `0.4049` n `20`; unknown avg `-0.0203` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
