# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T23:52:27.575874+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0235` n `13`; crypto_alt avg `0.1622` n `235`; crypto_major avg `0.0209` n `8`; equity avg `0.0034` n `143`; fx avg `-0.0031` n `6`; index avg `0.0018` n `26`; metal avg `-0.0016` n `20`; unknown avg `0.0874` n `984`
- 1h: commodity avg `-0.0691` n `13`; crypto_alt avg `0.8013` n `235`; crypto_major avg `0.3893` n `8`; equity avg `0.0621` n `143`; fx avg `-0.0026` n `6`; index avg `-0.0045` n `26`; metal avg `-0.0114` n `20`; unknown avg `1.2252` n `982`
- 4h: commodity avg `0.1079` n `13`; crypto_alt avg `1.6245` n `235`; crypto_major avg `0.9288` n `8`; equity avg `0.0981` n `143`; fx avg `-0.0217` n `6`; index avg `0.0003` n `26`; metal avg `-0.014` n `20`; unknown avg `1.9058` n `906`
- 24h: commodity avg `0.0927` n `13`; crypto_alt avg `-0.2442` n `235`; crypto_major avg `-0.2624` n `8`; equity avg `0.726` n `142`; fx avg `-0.1426` n `6`; index avg `0.2917` n `26`; metal avg `-0.2954` n `20`; unknown avg `-0.3918` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
