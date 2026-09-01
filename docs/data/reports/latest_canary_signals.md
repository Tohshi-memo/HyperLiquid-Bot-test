# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T04:22:28.480384+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0173` n `12`; crypto_alt avg `0.1447` n `232`; crypto_major avg `0.0627` n `8`; equity avg `0.0584` n `130`; fx avg `0.0095` n `6`; index avg `0.0066` n `26`; metal avg `-0.0134` n `20`; unknown avg `0.6671` n `792`
- 1h: commodity avg `0.0149` n `12`; crypto_alt avg `0.3566` n `232`; crypto_major avg `0.3783` n `8`; equity avg `0.252` n `130`; fx avg `0.0283` n `6`; index avg `0.0316` n `26`; metal avg `0.0165` n `20`; unknown avg `0.254` n `790`
- 4h: commodity avg `0.0004` n `12`; crypto_alt avg `0.2719` n `232`; crypto_major avg `0.0473` n `8`; equity avg `0.1838` n `130`; fx avg `0.0752` n `6`; index avg `0.0537` n `26`; metal avg `-0.1241` n `20`; unknown avg `1.0195` n `790`
- 24h: commodity avg `0.3843` n `12`; crypto_alt avg `2.355` n `232`; crypto_major avg `2.2754` n `8`; equity avg `1.4609` n `130`; fx avg `0.0153` n `6`; index avg `0.1518` n `26`; metal avg `-0.0057` n `20`; unknown avg `0.2627` n `751`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
