# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T09:07:28.817099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0958` n `13`; crypto_alt avg `0.0622` n `235`; crypto_major avg `0.0382` n `8`; equity avg `0.0073` n `144`; fx avg `-0.013` n `6`; index avg `-0.0094` n `26`; metal avg `0.0308` n `20`; unknown avg `0.0771` n `1077`
- 1h: commodity avg `0.2813` n `13`; crypto_alt avg `-0.378` n `235`; crypto_major avg `-0.2164` n `8`; equity avg `-0.1582` n `144`; fx avg `0.0401` n `6`; index avg `-0.0376` n `26`; metal avg `0.0283` n `20`; unknown avg `0.4355` n `1059`
- 4h: commodity avg `0.3014` n `13`; crypto_alt avg `0.8262` n `235`; crypto_major avg `0.8715` n `8`; equity avg `-0.0404` n `144`; fx avg `0.0069` n `6`; index avg `-0.0057` n `26`; metal avg `0.2978` n `20`; unknown avg `-0.1976` n `981`
- 24h: commodity avg `-0.0311` n `13`; crypto_alt avg `0.9216` n `235`; crypto_major avg `1.3795` n `8`; equity avg `0.2435` n `144`; fx avg `-0.0425` n `6`; index avg `-0.0512` n `26`; metal avg `0.3396` n `20`; unknown avg `0.0241` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2068`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1878`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
