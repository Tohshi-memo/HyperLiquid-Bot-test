# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T08:22:26.888424+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0271` n `13`; crypto_alt avg `0.185` n `237`; crypto_major avg `0.1945` n `8`; equity avg `-0.0577` n `151`; fx avg `-0.0079` n `6`; index avg `-0.0027` n `26`; metal avg `-0.008` n `20`; unknown avg `0.0135` n `1195`
- 1h: commodity avg `-0.0148` n `13`; crypto_alt avg `0.0481` n `237`; crypto_major avg `-0.1022` n `8`; equity avg `-0.1069` n `151`; fx avg `-0.0198` n `6`; index avg `-0.0188` n `26`; metal avg `-0.0996` n `20`; unknown avg `0.1203` n `1149`
- 4h: commodity avg `-0.0722` n `13`; crypto_alt avg `0.5361` n `237`; crypto_major avg `0.2611` n `8`; equity avg `0.0049` n `151`; fx avg `-0.0656` n `6`; index avg `-0.0068` n `26`; metal avg `-0.0832` n `20`; unknown avg `0.0867` n `1124`
- 24h: commodity avg `-0.4754` n `13`; crypto_alt avg `0.6423` n `237`; crypto_major avg `1.1943` n `8`; equity avg `2.5177` n `151`; fx avg `-0.0748` n `6`; index avg `0.4652` n `26`; metal avg `0.2246` n `20`; unknown avg `2.5329` n `875`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1966`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1443`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1241`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0634`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0588`, n `666`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
