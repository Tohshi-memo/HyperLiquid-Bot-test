# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T17:37:34.723127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0957` n `13`; crypto_alt avg `-0.216` n `235`; crypto_major avg `-0.2589` n `8`; equity avg `-0.064` n `150`; fx avg `-0.0027` n `6`; index avg `-0.0248` n `26`; metal avg `-0.0551` n `20`; unknown avg `-0.1061` n `1077`
- 1h: commodity avg `-0.3105` n `13`; crypto_alt avg `-0.3535` n `235`; crypto_major avg `-0.4185` n `8`; equity avg `0.1472` n `150`; fx avg `-0.0149` n `6`; index avg `0.0263` n `26`; metal avg `0.0133` n `20`; unknown avg `0.4347` n `1074`
- 4h: commodity avg `-0.6103` n `13`; crypto_alt avg `0.3297` n `235`; crypto_major avg `-0.118` n `8`; equity avg `0.5407` n `150`; fx avg `-0.0197` n `6`; index avg `0.1414` n `26`; metal avg `0.2455` n `20`; unknown avg `0.1866` n `1022`
- 24h: commodity avg `0.3031` n `13`; crypto_alt avg `-5.1346` n `235`; crypto_major avg `-3.6628` n `8`; equity avg `-1.6506` n `150`; fx avg `-0.1933` n `6`; index avg `-0.275` n `26`; metal avg `-0.5824` n `20`; unknown avg `15.3851` n `988`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1449`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1384`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1375`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.086`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0833`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0794`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0791`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0713`, n `669`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0711`, n `669`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0689`, n `669`, weak_sample_signal
