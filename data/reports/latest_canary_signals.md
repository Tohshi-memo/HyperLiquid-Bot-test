# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T13:56:54.119131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0827` n `13`; crypto_alt avg `0.3319` n `235`; crypto_major avg `0.3499` n `8`; equity avg `0.102` n `150`; fx avg `-0.0023` n `6`; index avg `-0.0148` n `26`; metal avg `0.037` n `20`; unknown avg `1.0317` n `1042`
- 1h: commodity avg `0.0831` n `13`; crypto_alt avg `0.049` n `235`; crypto_major avg `0.042` n `8`; equity avg `-0.1734` n `150`; fx avg `0.0389` n `6`; index avg `-0.0946` n `26`; metal avg `0.0161` n `20`; unknown avg `12.4325` n `1040`
- 4h: commodity avg `0.1514` n `13`; crypto_alt avg `-0.7269` n `235`; crypto_major avg `-0.6185` n `8`; equity avg `-0.6476` n `150`; fx avg `-0.0332` n `6`; index avg `-0.2048` n `26`; metal avg `-0.2744` n `20`; unknown avg `3.5239` n `1034`
- 24h: commodity avg `1.2116` n `13`; crypto_alt avg `-5.5723` n `235`; crypto_major avg `-3.9945` n `8`; equity avg `-2.1075` n `150`; fx avg `-0.1467` n `6`; index avg `-0.4706` n `26`; metal avg `-0.6577` n `20`; unknown avg `826.0089` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
