# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T15:37:31.522541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0134` n `12`; crypto_alt avg `0.04` n `232`; crypto_major avg `0.2187` n `8`; equity avg `-0.0182` n `128`; fx avg `0.0132` n `6`; index avg `-0.0203` n `26`; metal avg `-0.0221` n `20`; unknown avg `0.0176` n `794`
- 1h: commodity avg `0.1106` n `12`; crypto_alt avg `0.2006` n `232`; crypto_major avg `0.5` n `8`; equity avg `-0.0045` n `128`; fx avg `0.0348` n `6`; index avg `-0.0532` n `26`; metal avg `-0.0399` n `20`; unknown avg `0.3841` n `792`
- 4h: commodity avg `-0.1798` n `12`; crypto_alt avg `-0.261` n `232`; crypto_major avg `0.1276` n `8`; equity avg `-0.0015` n `128`; fx avg `0.0737` n `6`; index avg `-0.1089` n `26`; metal avg `-0.3467` n `20`; unknown avg `0.3706` n `790`
- 24h: commodity avg `0.5572` n `12`; crypto_alt avg `-1.1402` n `231`; crypto_major avg `-1.4615` n `8`; equity avg `-0.4804` n `128`; fx avg `-0.0678` n `6`; index avg `-0.207` n `26`; metal avg `-0.5272` n `20`; unknown avg `0.3509` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
